
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

    def test_visit_if_statement_node(self):
        """runs 4 different test cases. Case 1: if else if else. Case 2: if else if. Case 3: if else. Case 4: if"""
        if_elseif_else_source_code = """
        if a < 0 {
            a := 0
        } 
        else if a < 0 {
            a := 0
        } 
        else {
            a := 0
        }"""
        expected_ast_if_elseif_else = StartNode(
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
        self._test_expected_ast(expected_ast_if_elseif_else, if_elseif_else_source_code, "if elseif else")
        
        if_else_if_source_code = """
        if a < 0 {
            a := 0
        } 
        else if a < 0 {
            a := 0
        }"""
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
        self._test_expected_ast(expected_ast_if_else_if, if_else_if_source_code, "if else if")
        
        if_else_source_code = """
        if a < 0 {
            a := 0
        } 
        else {
            a := 0
        }"""
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
        self._test_expected_ast(expected_ast_if_else, if_else_source_code, "if else")

        if_source_code = ("""
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
        self._test_expected_ast(expected_ast_if, if_source_code, "if")

        
    def test_visitStartNode(self):
        source_code = """
        num a
        foo() {
        }
        """
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
        self._test_expected_ast(expected_ast, source_code, "visitStartNode")

    def test_list_subscript(self):
        source_code = """
        a := a[0][0]
        """
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
        self._test_expected_ast(expected_ast, source_code, "test_list_subscript")

    @ classmethod
    def tearDownClass(cls):
        cls.delete_input_file()


# if __name__ == '__main__':
#     unittest.main()
