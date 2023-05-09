from antlr4 import *
from _lexer.AlgoPractiseLexer import AlgoPractiseLexer
from _parser.AlgoPractiseParser import AlgoPractiseParser
from antlr4.tree.Trees import Trees
from visitors.ASTSingleDispatchVisitor import ASTSingleDispatchVisitor
from antlr4 import FileStream, CommonTokenStream

from nodes.Node import Node
from symbol_table.symbol_tabel_visitor import SymbolTableVisitor
from TypeCheckVisitors.type_check_visitors import ASTTypeChecker

SOURCE_CODE_FILE_NAME = r"././input_stream/malthe_test_err.txt"


def main(argv=None):
    input_stream = FileStream(SOURCE_CODE_FILE_NAME)
    lexer = AlgoPractiseLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = AlgoPractiseParser(stream)
    parse_tree_start_node = parser.start()

    single_dispatch_visitor = ASTSingleDispatchVisitor()
    ast_root = single_dispatch_visitor.visit_start_node(parse_tree_start_node)

    symtbl = SymbolTableVisitor()
    symbol_table_errors = symtbl.do_visit(ast_root)

    type_check = ASTTypeChecker()
    type_check_errors = type_check.do_visit(ast_root)
    if type_check_errors or symbol_table_errors:
        for error in symbol_table_errors:
            print(error)
        for error in type_check_errors:
            print(error)
    else:
        print_ast(ast_root)
    
    # print_cst(parser, parse_tree_start_node)
    
    # listener = AlgoPractiseListener()
    # walker = ParseTreeWalker()
    # walker.walk(listener, parse_tree)


def print_ast(node, indent=""):
    print(indent, node.__class__.__name__)
    indent += "    "

    for attribute_name, attribute_value in vars(node).items():
        if isinstance(attribute_value, Node):
            print_ast(attribute_value, indent)
        elif isinstance(attribute_value, list):
            print(indent, attribute_name, f"[{len(attribute_value)}]")
            indent += "    "
            for item in attribute_value:
                if isinstance(item, Node):
                    print_ast(item, indent)
                else:
                    print(indent, attribute_name, item)
            indent = indent[:-4]
        else:
            print(indent, attribute_name, attribute_value)

def print_cst(parser, parse_tree_start_node):
    print("CST:")
    tree_str = Trees.toStringTree(parse_tree_start_node, None, parser)
    print(tree_str)


if __name__ == "__main__":
    main()
# TODO:
# Migrate from camel-case to snake_case
