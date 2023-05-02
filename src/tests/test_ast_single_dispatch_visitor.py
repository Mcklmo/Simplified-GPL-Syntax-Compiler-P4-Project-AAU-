
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
            line_number=0,

            master_statement_nodes=[
                MasterStatementNode(
                    line_number=1,
                    statement_node =IfStatementNode(
                        line_number=1,
                        condition=BinaryExpressionNode(
                            line_number=1,
                            left=IDNode(
                                line_number=1,
                                identifier="a"),
                            right=NumberNode(1,0.0),
                            operator="<",
                        ),
                        block=BlockNode(
                            line_number=2,
                            statements_nodes=[
                                AssignmentStatementNode(
                                    2,
                                    IDNode(
                                        line_number=2,
                                        identifier="a"),
                                    expression=NumberNode(2,0.0),
                                )
                            ],
                        ),
                        else_node=ElseStatementNode(
                            line_number=4,
                            if_statement=IfStatementNode(
                                line_number=4,
                                condition=BinaryExpressionNode(
                                    line_number=4,
                                    left=IDNode(
                                        line_number=4,
                                        identifier="a"),
                                    right=NumberNode(4,0.0),
                                    operator="<",
                                ),
                                block=BlockNode(
                                    line_number=5,
                                    statements_nodes=[
                                        AssignmentStatementNode(
                                            5,
                                            IDNode(
                                                line_number=5,
                                                identifier="a"),
                                            expression=NumberNode(
                                                5,0.0),
                                        )
                                    ],
                                ),
                                else_node=ElseStatementNode(
                                    line_number=7,
                                    block=BlockNode(
                                        line_number=8,
                                        statements_nodes=[
                                            AssignmentStatementNode(
                                                8,
                                                IDNode(
                                                    line_number=8,
                                                    identifier="a"),
                                                expression=NumberNode(
                                                    8,0.0),
                                            )
                                        ],
                                    ),
                                ),
                            ),
                            block=None,
                        ),
                    ),
                ),
            ]
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
            line_number=0,

            master_statement_nodes=[
                MasterStatementNode(
                    1,
                    statement_node = IfStatementNode(
                        line_number=1,
                        condition=BinaryExpressionNode(
                            line_number=1,
                            left=IDNode(
                                line_number=1,
                                identifier="a"),
                            right=NumberNode(1,0.0),
                            operator="<",
                        ),
                        block=BlockNode(
                            line_number=2,
                            statements_nodes=[
                                AssignmentStatementNode(
                                    2,
                                    IDNode(
                                        line_number=2,
                                        identifier="a"),
                                    expression=NumberNode(2,0.0),
                                )
                            ],
                        ),
                        else_node=ElseStatementNode(
                            line_number=4,
                            if_statement=IfStatementNode(
                                line_number=4,
                                condition=BinaryExpressionNode(
                                    line_number=4,
                                    left=IDNode(
                                        line_number=4,
                                        identifier="a"),
                                    right=NumberNode(4,0.0),
                                    operator="<",
                                ),
                                block=BlockNode(
                                    line_number=5,
                                    statements_nodes=[
                                        AssignmentStatementNode(
                                            5,
                                            IDNode(
                                                line_number=5,
                                                identifier="a"),
                                            expression=NumberNode(5,0.0),
                                        )
                                    ],
                                ),
                            ),
                        ),
                    ),
                ),
            ]
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
            line_number=0,
            master_statement_nodes=[
                MasterStatementNode(
                    1,
                    statement_node = IfStatementNode(
                        line_number=1,
                        condition=BinaryExpressionNode(
                            line_number=1,
                            left=IDNode(
                                line_number=2,
                                identifier="a"),
                            right=NumberNode(1,0.0),
                            operator="<",
                        ),
                        block=BlockNode(
                            line_number=2,
                            statements_nodes=[
                                AssignmentStatementNode(
                                    2,
                                    IDNode(
                                        line_number=2,
                                        identifier="a"),
                                    expression=NumberNode(2,0.0),
                                )
                            ],
                        ),
                        else_node=ElseStatementNode(
                            line_number=4,
                            block=BlockNode(
                                line_number=5,
                                statements_nodes=[
                                    AssignmentStatementNode(
                                        5,
                                        IDNode(
                                            line_number=5,
                                            identifier="a"),
                                        expression=NumberNode(5,0.0),
                                    )
                                ],
                            ),
                        )
                    ),            
                ),
            ] 
        )

        self._test_expected_ast(expected_ast_if_else, if_else_source_code, "if else")

        if_source_code = ("""
        if a < 0 {
            a := 0
        }
        """)
        expected_ast_if = StartNode(
            line_number=0,
            master_statement_nodes=[
                MasterStatementNode(
                    1,
                    statement_node = IfStatementNode(
                        line_number=1,
                        condition=BinaryExpressionNode(
                            line_number=1,
                            left=IDNode(
                                line_number=1,
                                identifier="a"),
                            right=NumberNode(1, 0.0),
                            operator="<",
                        ),
                        block=BlockNode(
                            line_number=2,
                            statements_nodes=[
                                AssignmentStatementNode(
                                    2,
                                    IDNode(
                                        line_number=2,
                                        identifier="a"),
                                    expression=NumberNode(2, 0.0),
                                )
                            ],
                        ),
                    ),
                ),
            ],
        )
        self._test_expected_ast(expected_ast_if, if_source_code, "if")

        
    def test_visitStartNode(self):
        return
        source_code = """
        num a
        foo() {
        }
        """
        expected_ast = StartNode(
            line_number=0,

            master_statement_nodes=[
                MasterStatementNode(
                    1,
                    statement_node = DeclarationStatementNode(
                        TypeNode(1,"num", 0),
                        1,
                        identifier=IDNode(
                                line_number=1,
                                identifier="a"),
                    )
                ),

                MasterStatementNode(
                    2,
                    function_node = FunctionNode(
                    2,
                    IDNode(
                        line_number=2,
                        identifier="foo"),
                    params=[],
                    block=BlockNode(
                        3,
                        ),
                    )
                ),
            ],
        )
        self._test_expected_ast(expected_ast, source_code, "visitStartNode")

    def test_list_subscript(self):
        return
        source_code = """
        a := a[0][0]
        """
        expected_ast = StartNode(
            line_number=0,
            master_statement_nodes=[
                MasterStatementNode(1,statement_node=
                AssignmentStatementNode(
                    1,
                    identifier = IDNode(
                        1,
                        "a"),
                    expression=ListSubscriptValueNode(
                        1,
                        identifier = IDNode(
                            1,
                            "a"),
                        subscripts=[
                            NumberNode(1,0),
                            NumberNode(1,0)
                        ]
                    )
                )
            )
            ])
        self._test_expected_ast(expected_ast, source_code, "test_list_subscript")

    @ classmethod
    def tearDownClass(cls):
        cls.delete_input_file()


# if __name__ == '__main__':
#     unittest.main()
