
import os
import unittest
from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from _lexer.AlgoPractiseLexer import AlgoPractiseLexer
from _parser.AlgoPractiseParser import AlgoPractiseParser
from abstract_syntax.AssignmentStatementNode import AssignmentStatementNode
from abstract_syntax.BinaryExpressionNode import BinaryExpressionNode
from abstract_syntax.BlockNode import BlockNode
from abstract_syntax.DeclarationStatementNode import DeclarationStatementNode
from abstract_syntax.FunctionNode import FunctionNode
from abstract_syntax.ListSubscriptValueNode import ListSubscriptValueNode
from abstract_syntax.NumberNode import NumberNode
from abstract_syntax.ParameterNode import ParameterNode
from abstract_syntax.ReturnStatementNode import ReturnStatementNode
from abstract_syntax.StartNode import StartNode
from abstract_syntax.TypeNode import TypeNode
from visitors.ASTSingleDispatchVisitor import ASTSingleDispatchVisitor


class TestASTSingleDispatchVisitor(unittest.TestCase):

    INPUT_FILE_NAME = "temp_test_input.txt"

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

    def test_visitStartNode(self):
        # Call create_input_file with the input string for this test
        ast = self.create_and_parse_input_file("""
        num a
        foo() {
        }
        """)

        # Add assertions to test the generated abstract syntax tree after calling visitStartNode
        expected_ast = StartNode(
            functions=[
                FunctionNode(
                    identifier="foo",
                    params=[
                    ],
                    block=BlockNode(
                    ),
                )
            ],
            statements=[
                DeclarationStatementNode(
                    TypeNode("num", 0),
                    identifier="a",
                )
            ]
        )
        self.assertEqual(ast, expected_ast)

    def test_visitStatementNode(self):
        return
        # Call create_input_file with the input string for this test
        self.create_and_parse_input_file("your_input_string_here")

        ast = self.parse(self.INPUT_FILE_NAME)
        # Add assertions to test the generated abstract syntax tree after calling visitStatementNode

    def test_list_subscript(self):
        ast = self.create_and_parse_input_file("a := a[0][0]")
        expected_ast = StartNode(
            functions=[],
            statements=[
                AssignmentStatementNode(
                    identifier="a",
                    subscripts=None,
                    expression=ListSubscriptValueNode(
                        identifier="a",
                        subscripts=[
                            NumberNode(0),
                            NumberNode(0)
                        ]
                    )
                )
            ])
        self.assertEqual(ast, expected_ast)

    @ classmethod
    def tearDownClass(cls):
        cls.delete_input_file()


# if __name__ == '__main__':
#     unittest.main()
