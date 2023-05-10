
import os
import unittest
from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from _lexer.AlgoPractiseLexer import AlgoPractiseLexer
from _parser.AlgoPractiseParser import AlgoPractiseParser
from nodes.AssignmentStatementNode import AssignmentStatementNode
from nodes.BinaryExpressionNode import BinaryExpressionNode
from nodes.BlockNode import BlockNode
from nodes.DeclarationStatementNode import DeclarationStatementNode
from nodes.FunctionNode import FunctionNode
from nodes.ListSubscriptValueNode import ListSubscriptValueNode
from nodes.NumberNode import NumberNode
from nodes.ParameterNode import ParameterNode
from nodes.IfStatementNode import IfStatementNode
from nodes.ElseStatementNode import ElseStatementNode
from nodes.StartNode import StartNode
from nodes.TypeNode import TypeNode
from nodes.IDNode import IDNode
from nodes.master_statement_node import MasterStatementNode
from visitors.ASTSingleDispatchVisitor import ASTSingleDispatchVisitor


class TestASTSingleDispatchVisitor(unittest.TestCase):

    INPUT_FILE_NAME = "temp_test_input.txt"

    def _test_expected_ast(self, expected_ast, source_code, msg=""):
        actual_ast = self.create_and_parse_input_file(source_code)
        self.assertEqual(expected_ast, actual_ast, msg)

    def create_and_parse_input_file(self, input_string: str) -> None:
        with open(self.INPUT_FILE_NAME, "w") as input_file:
            input_file.write(input_string)
        return self.parse(self.INPUT_FILE_NAME)

    @classmethod
    def delete_input_file(cls) -> None:
        if os.path.isfile(cls.INPUT_FILE_NAME):
            os.remove(cls.INPUT_FILE_NAME)

    def setUp(self):
        self.visitor = ASTSingleDispatchVisitor()

    def parse(self, input_file):
        # Read input file and generate the corresponding concrete syntax tree
        input_stream = FileStream(input_file)
        lexer = AlgoPractiseLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = AlgoPractiseParser(token_stream)
        cst = parser.start()

        # Generate the corresponding abstract syntax tree
        ast = self.visitor.visit_start_node(cst)
        return ast
  

    @ classmethod
    def tearDownClass(cls):
        cls.delete_input_file()


# if __name__ == '__main__':
#     unittest.main()
