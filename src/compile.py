
from antlr4 import *
from _lexer.AlgoPractiseLexer import AlgoPractiseLexer
from _parser.AlgoPractiseParser import AlgoPractiseParser
from visitors.ASTSingleDispatchVisitor import ASTSingleDispatchVisitor
from antlr4 import FileStream, CommonTokenStream

from symbol_table.symbol_tabel_visitor import SymbolTableVisitor
from TypeCheckVisitors.type_check_visitors import ASTTypeChecker
from code_generation.code_gen_visitors import CodeGeneratorASTVisitor
from errors.custom_lexer_listener import CustomErrorListener


def compile(source_path: str):
    lexer_error_listener = CustomErrorListener()

    input_stream = FileStream(source_path)
    lexer = AlgoPractiseLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = AlgoPractiseParser(stream)
    parser.addErrorListener(lexer_error_listener)
    parse_tree_start_node = parser.start()

    if lexer_error_listener.error_count != 0:
        exit(0)

    single_dispatch_visitor = ASTSingleDispatchVisitor()
    ast_root = single_dispatch_visitor.visit_start_node(parse_tree_start_node)

    symtbl = SymbolTableVisitor()
    symbol_table_errors = symtbl.do_visit(ast_root)
    if symbol_table_errors:
        for error in symbol_table_errors:
            print(error)
        return

    type_check = ASTTypeChecker()
    type_check_errors = type_check.do_visit(ast_root)
    if type_check_errors:
        for error in type_check_errors:
            print(error)
        return

    code_gen = CodeGeneratorASTVisitor()
    code_gen.do_visit(ast_root)

