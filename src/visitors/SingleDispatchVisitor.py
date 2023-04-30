# from .AlgoPractiseVisitor import AlgoPractiseVisitor
from _parser.AlgoPractiseParser import AlgoPractiseParser
# from typing import List
# from antlr4.Token import CommonToken, Token
# from collections.abc import Iterable
# from antlr4 import ParserRuleContext
from abc import ABC, abstractmethod


from nodes.Node import Node
from nodes.StartNode import StartNode
from nodes.AssignmentStatementNode import AssignmentStatementNode
# from nodes.BinaryExpressionNode import BinaryExpressionNode
from nodes.BlockNode import BlockNode
# from nodes.BooleanNode import BooleanNode
from nodes.DeclarationStatementNode import DeclarationStatementNode
from nodes.ElseStatementNode import ElseStatementNode
from nodes.FunctionCallExpressionNode import FunctionCallExpressionNode
from nodes.FunctionCallStatementNode import FunctionCallStatementNode
from nodes.FunctionNode import FunctionNode
from nodes.IfStatementNode import IfStatementNode
from nodes.ListSubscriptValueNode import ListSubscriptValueNode
# from nodes.NumberNode import NumberNode
from nodes.ParameterNode import ParameterNode
from nodes.ReturnStatementNode import ReturnStatementNode
# from nodes.StringNode import StringNode
from nodes.TypeNode import TypeNode
# from nodes.UnaryExpressionNode import UnaryExpressionNode
from nodes.WhileStatementNode import WhileStatementNode
from nodes.StatementNode import StatementNode


class SingleDispatchVisitor(ABC):
    @abstractmethod
    def visit_element_list_node(self, cst_node: AlgoPractiseParser.Elmnt_listContext):
        pass

    @abstractmethod
    def visit_control_statement_node(self, node):
        pass

    @abstractmethod
    def visit_statement_node(self, node: StatementNode):
        pass

    @abstractmethod
    def visit_assignment_statement_node(self, node: AssignmentStatementNode):
        pass

    @abstractmethod
    def visit_start_node(self, node: StartNode):
        pass

    @abstractmethod
    def visit_block_node(self, node: BlockNode):
        pass

    @abstractmethod
    def visit_declaration_statement_node(self, node: DeclarationStatementNode):
        pass

    @abstractmethod
    def visit_else_statement_node(self, node: ElseStatementNode):
        pass

    @abstractmethod
    def visit_function_call_expression_node(self, node: FunctionCallExpressionNode):
        pass

    @abstractmethod
    def visit_function_call_statement_node(self, node: FunctionCallStatementNode):
        pass

    @abstractmethod
    def visit_function_node(self, node: FunctionNode):
        pass

    @abstractmethod
    def visit_if_statement_node(self, node: IfStatementNode):
        pass

    @abstractmethod
    def visit_list_subscript_value_node(self,identifier:str ,node: ListSubscriptValueNode):
        pass

    @abstractmethod
    def visit_parameter_node(self, node: ParameterNode):
        pass

    @abstractmethod
    def visit_return_statement_node(self, node: ReturnStatementNode):
        pass

    @abstractmethod
    def visit_type_node(self, node: TypeNode):
        pass

    @abstractmethod
    def visit_while_statement_node(self, node: WhileStatementNode):
        pass

    @abstractmethod
    def visit_expression_node(self, node: Node):
        pass

    @abstractmethod
    def visit_val_node(self, node: Node):
        pass
    
    @abstractmethod
    def visit_parameters_node(self, ctx):
        pass