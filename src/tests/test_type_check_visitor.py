
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
from nodes.ElementListNode import ElementListNode
from nodes.master_statement_node import MasterStatementNode
from nodes.StringNode import StringNode
from visitors.ASTSingleDispatchVisitor import ASTSingleDispatchVisitor
from TypeCheckVisitors.type_check_visitors import ASTTypeChecker
from TypeCheckVisitors.type_check_utils import TypeCheckUtils

class TestTypeCheckVisitor(unittest.TestCase):

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
        self.visitor= ASTTypeChecker()

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

    def test_extract_type_node_from_elem_list(self):
        element_list_1d_ok = ElementListNode([NumberNode(0,0), NumberNode(0,0)],0)
        expected_typenode = TypeNode(0,"num",1)
        actual_typenode = self.visitor.extract_type_node_from_elem_list(element_list_1d_ok,self.new_default_element_list_type_node(),TypeNode(0,"num",3))
        self.assertEqual(expected_typenode, actual_typenode,"1d list no error")

        element_list_1d_err = ElementListNode([NumberNode(0,0), NumberNode(0,0), ElementListNode([],0)],0)
        expected_typenode = None 
        actual_typenode = self.visitor.extract_type_node_from_elem_list(element_list_1d_err,self.new_default_element_list_type_node(),TypeNode(0,"num",3))
        self.assertEqual(expected_typenode, actual_typenode,"1d list expected none")

        element_list_2d_ok = ElementListNode([ElementListNode([NumberNode(0,0), NumberNode(0,0)],0), ElementListNode([NumberNode(0,0), NumberNode(0,0)],0)],0)
        expected_typenode = TypeNode(0,"num",2)
        actual_typenode = self.visitor.extract_type_node_from_elem_list(element_list_2d_ok,self.new_default_element_list_type_node(),TypeNode(0,"num",3))
        self.assertEqual(expected_typenode, actual_typenode,"2d list no error")

        element_list_2d_err = ElementListNode([ElementListNode([NumberNode(0,0), NumberNode(0,0)],0), ElementListNode([NumberNode(0,0), NumberNode(0,0), ElementListNode([],0)],0)],0)
        expected_typenode = None
        actual_typenode = self.visitor.extract_type_node_from_elem_list(element_list_2d_err,self.new_default_element_list_type_node(),TypeNode(0,"num",3))
        self.assertEqual(expected_typenode, actual_typenode,"2d list expected none")
        # Test empty list
        element_list_empty = ElementListNode([], 0)
        expected_typenode = TypeNode(0, "num", 1)
        actual_typenode = self.visitor.extract_type_node_from_elem_list(element_list_empty, self.new_default_element_list_type_node(),TypeNode(0,"num",3))
        self.assertEqual(expected_typenode, actual_typenode, "Empty list no error")

        # Test list with another empty list
        element_list_nested_empty = ElementListNode([ElementListNode([], 0)], 0)
        expected_typenode = TypeNode(0, "num", 2)
        actual_typenode = self.visitor.extract_type_node_from_elem_list(element_list_nested_empty, self.new_default_element_list_type_node(),TypeNode(0,"num",3))
        self.assertEqual(expected_typenode, actual_typenode, "List with empty list no error")

        # test 3d list of empty lists 
        element_list_3d_empty = ElementListNode([ElementListNode([ElementListNode([], 0)], 0)], 0)
        expected_typenode = TypeNode(0, "num", 3)
        actual_typenode = self.visitor.extract_type_node_from_elem_list(element_list_3d_empty, self.new_default_element_list_type_node(),TypeNode(0,"num",3))
        self.assertEqual(expected_typenode, actual_typenode, "3d list of empty lists no error")

        # Test list with mixed types (num and string)
        element_list_mixed_types = ElementListNode([NumberNode(0, 0), StringNode(0, "")], 0)
        expected_typenode = None
        actual_typenode = self.visitor.extract_type_node_from_elem_list(element_list_mixed_types, self.new_default_element_list_type_node(),TypeNode(0,"num",3))
        self.assertEqual(expected_typenode, actual_typenode, "List with mixed types expected None")

    def new_default_element_list_type_node(self):
        return TypeNode(0,"list",1)
    



if __name__ == '__main__':
    unittest.main()
