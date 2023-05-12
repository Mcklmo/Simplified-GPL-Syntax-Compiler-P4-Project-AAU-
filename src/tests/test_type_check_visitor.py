
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
        # nested lists have one dimension less than the list itself
        element_list_1d = ElementListNode([],0)
        element_list_2d = ElementListNode([element_list_1d],0)
        element_list_3d = ElementListNode([element_list_2d],0)
        expected_typenode_1d = TypeNode(0,"num",1)
        expected_typenode_2d = TypeNode(0,"num",2)
        expected_typenode_3d = TypeNode(0,"num",3)
        self.visitor.extract_type_node_from_elem_list(element_list_3d,TypeNode(0,"num",3))
        self.assertEqual(expected_typenode_3d, element_list_3d.type,"3d list has 3 dimensions")
        self.assertEqual(expected_typenode_2d,element_list_2d.type,"2d list has 2 dimensions")
        self.assertEqual(expected_typenode_1d,element_list_1d.type,"1d list has 1 dimension")

        element_list_1d_ok = ElementListNode([NumberNode(0,0), NumberNode(0,0)],0)
        expected_typenode = TypeNode(0,"num",1)
        self.visitor.extract_type_node_from_elem_list(element_list_1d_ok,TypeNode(0,"num",3))
        self.assertEqual(expected_typenode, element_list_1d_ok.type,"1d list no error")

        element_list_1d_err = ElementListNode([NumberNode(0,0), NumberNode(0,0), ElementListNode([],0)],0)
        expected_typenode = None 
        self.visitor.extract_type_node_from_elem_list(element_list_1d_err,TypeNode(0,"num",3))
        self.assertEqual(expected_typenode, element_list_1d_err.type,"1d list expected none")

        element_list_2d_ok = ElementListNode([ElementListNode([NumberNode(0,0), NumberNode(0,0)],0), ElementListNode([NumberNode(0,0), NumberNode(0,0)],0)],0)
        expected_typenode = TypeNode(0,"num",2)
        self.visitor.extract_type_node_from_elem_list(element_list_2d_ok,TypeNode(0,"num",3))
        self.assertEqual(expected_typenode, element_list_2d_ok.type,"2d list no error")

        element_list_2d_err = ElementListNode([ElementListNode([NumberNode(0,0), NumberNode(0,0)],0), ElementListNode([NumberNode(0,0), NumberNode(0,0), ElementListNode([],0)],0)],0)
        expected_typenode = None
        self.visitor.extract_type_node_from_elem_list(element_list_2d_err,TypeNode(0,"num",3))
        self.assertEqual(expected_typenode, element_list_2d_err.type,"2d list expected none")

        # Test empty list
        element_list_empty = ElementListNode([], 0)
        expected_typenode = TypeNode(0, "num", 1)
        self.visitor.extract_type_node_from_elem_list(element_list_empty, TypeNode(0,"num",3))
        self.assertEqual(expected_typenode, element_list_empty.type, "Empty list no error")

        # Test list with another empty list
        element_list_nested_empty = ElementListNode([ElementListNode([], 0)], 0)
        expected_typenode = TypeNode(0, "num", 2)
        self.visitor.extract_type_node_from_elem_list(element_list_nested_empty, TypeNode(0,"num",3))
        self.assertEqual(expected_typenode, element_list_nested_empty.type, "List with empty list no error")

        # test 3d list of empty lists 
        element_list_3d_empty = ElementListNode([ElementListNode([ElementListNode([], 0)], 0)], 0)
        expected_typenode = TypeNode(0, "num", 3)
        self.visitor.extract_type_node_from_elem_list(element_list_3d_empty, TypeNode(0,"num",3))
        self.assertEqual(expected_typenode, element_list_3d_empty.type, "3d list of empty lists no error")

        # Test list with mixed types (num and string)
        element_list_mixed_types = ElementListNode([NumberNode(0, 0), StringNode(0, "")], 0)
        expected_typenode = None
        self.visitor.extract_type_node_from_elem_list(element_list_mixed_types, TypeNode(0,"num",3))
        self.assertEqual(expected_typenode, element_list_mixed_types.type, "List with mixed types expected None")



if __name__ == '__main__':
    unittest.main()
