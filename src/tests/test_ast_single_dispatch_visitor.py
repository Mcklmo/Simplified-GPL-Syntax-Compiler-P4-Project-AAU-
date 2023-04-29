
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
from abstract_syntax.IfStatementNode import IfStatementNode
from abstract_syntax.ElseStatementNode import ElseStatementNode
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

    def test_visit_if_statement_node(self):
        actual_ast_if_else_if_else = self.create_and_parse_input_file("""
        if a < 0 {
            a := 0
        } 
        else if a < 0 {
            a := 0
        } 
        else {
            a := 0
        }""")
        expected_ast_if_else_if_else = StartNode(
            functions=[],
            statements=[
                IfStatementNode(
                    condition=BinaryExpressionNode(
                        left="a",
                        right=NumberNode(0.0),
                        operator="<",
                    ),
                    block=BlockNode(
                        statements_nodes=[
                            AssignmentStatementNode(
                                "a",
                                expression=NumberNode(0.0),
                            )
                        ],
                    ),
                    else_node=ElseStatementNode(
                        if_statement=IfStatementNode(
                            condition=BinaryExpressionNode(
                                left="a",
                                right=NumberNode(0.0),
                                operator="<",
                            ),
                            block=BlockNode(
                                statements_nodes=[
                                    AssignmentStatementNode(
                                        "a",
                                        expression=NumberNode(
                                            0.0),
                                    )
                                ],
                            ),
                            else_node=ElseStatementNode(
                                block=BlockNode(
                                    statements_nodes=[
                                        AssignmentStatementNode(
                                            "a",
                                            expression=NumberNode(
                                                0.0),
                                        )
                                    ],
                                ),
                            ),
                        ),
                        block=None,
                    ),
                ),
            ],
        )
        self.assertEqual(actual_ast_if_else_if_else,
                         expected_ast_if_else_if_else)
        
        actual_ast_if_else_if = self.create_and_parse_input_file("""
        if a < 0 {
            a := 0
        } 
        else if a < 0 {
            a := 0
        }""")
        expected_ast_if_else_if = StartNode(
            functions=[],
            statements=[

                IfStatementNode(
                    condition=BinaryExpressionNode(
                        left="a",
                        right=NumberNode(0.0),
                        operator="<",
                    ),
                    block=BlockNode(
                        statements_nodes=[
                            AssignmentStatementNode(
                                "a",
                                expression=NumberNode(0.0),
                            )
                        ],
                    ),
                    else_node=ElseStatementNode(
                        if_statement=IfStatementNode(
                            condition=BinaryExpressionNode(

                                left="a",
                                right=NumberNode(0.0),
                                operator="<",
                            ),
                            block=BlockNode(
                                statements_nodes=[
                                    AssignmentStatementNode(
                                        "a",
                                        expression=NumberNode(
                                            0.0),
                                    )
                                ],
                            ),
                        ),

                    ),
                ),
            ],
        )
        self.assertEqual(actual_ast_if_else_if, expected_ast_if_else_if)
        
        actual_ast_if_else = self.create_and_parse_input_file("""
        if a < 0 {
            a := 0
        } 
        else {
            a := 0
        }""")
        expected_ast_if_else = StartNode(
            functions=[],
            statements=[

                IfStatementNode(
                    condition=BinaryExpressionNode(
                        left="a",
                        right=NumberNode(0.0),
                        operator="<",
                    ),
                    block=BlockNode(
                        statements_nodes=[
                            AssignmentStatementNode(
                                "a",
                                expression=NumberNode(0.0),
                            )
                        ],
                    ),
                    else_node=ElseStatementNode(
                        block=BlockNode(
                            statements_nodes=[
                                AssignmentStatementNode(

                                    "a",
                                    expression=NumberNode(0.0),
                                )
                            ],
                        ),
                    )
                ),
            ],
        )
        self.assertEqual(actual_ast_if_else, expected_ast_if_else)

        actual_ast_if = self.create_and_parse_input_file("""
        if a < 0 {
            a := 0
        }""")
        expected_ast_if = StartNode(
            functions=[],
            statements=[
                IfStatementNode(
                    condition=BinaryExpressionNode(
                        left="a",
                        right=NumberNode(0.0),
                        operator="<",
                    ),
                    block=BlockNode(
                        statements_nodes=[
                            AssignmentStatementNode(
                                "a",
                                expression=NumberNode(0.0),
                            )
                        ],
                    ),
                ),
            ],
        )
        self.assertEqual(actual_ast_if, expected_ast_if)
       
    def test_visitStartNode(self):
        # Call create_input_file with the input string for this test
        actual_ast = self.create_and_parse_input_file("""
        num a
        foo() {
        }
        """)

        # Add assertions to test the generated abstract syntax tree after calling visitStartNode
        expected_ast = StartNode(
            functions=[
                FunctionNode(
                    "foo",
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
        self.assertEqual(actual_ast, expected_ast)

    def test_list_subscript(self):
        actual_ast = self.create_and_parse_input_file("a := a[0][0]")
        expected_ast = StartNode(
            functions=[],
            statements=[
                AssignmentStatementNode(
                    "a",
                    subscripts=None,
                    expression=ListSubscriptValueNode(
                        "a",
                        subscripts=[
                            NumberNode(0),
                            NumberNode(0)
                        ]
                    )
                )
            ])
        self.assertEqual(actual_ast, expected_ast)

    @ classmethod
    def tearDownClass(cls):
        cls.delete_input_file()


# if __name__ == '__main__':
#     unittest.main()
