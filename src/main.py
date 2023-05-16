import os
from antlr4 import *
from _lexer.AlgoPractiseLexer import AlgoPractiseLexer
from _parser.AlgoPractiseParser import AlgoPractiseParser
from antlr4.tree.Trees import Trees
from visitors.ASTSingleDispatchVisitor import ASTSingleDispatchVisitor
from antlr4 import FileStream, CommonTokenStream

from nodes.Node import Node
from symbol_table.symbol_tabel_visitor import SymbolTableVisitor
from TypeCheckVisitors.type_check_visitors import ASTTypeChecker  
from code_generation.code_gen_visitors import CodeGeneratorASTVisitor
from compile import compile

"""switch the method in main to compile the file you want to compile.
    compile_this(source_code) will compile the source code in the string source_code.
    compile_from_file(source_code_path) will compile the file at source_code_path."""

SOURCE_CODE_FILE_NAME = r"././input_stream/complete_noerr.txt"


def main(argv=None):
    source_code = """
    num a := 5
    num b := 6
    num c := a + b

    """
    compile_direct_input(source_code)
    # compile_from_file(SOURCE_CODE_FILE_NAME)
    
    print("Done")

def compile_from_file(source_code_path: str):
    compile(source_code_path)

def compile_direct_input(source_code: str):
    source_code_path = r"././input_stream/test.txt"
    write_file(source_code, source_code_path)
    compile(source_code_path)
    delete_file(source_code_path)

def delete_file( path: str):
    os.remove(path)
def write_file(content: str, path :str):
    with open(path, "w") as f:
        f.write(content)

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
