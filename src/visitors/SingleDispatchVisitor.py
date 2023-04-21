from .AlgoPractiseVisitor import AlgoPractiseVisitor
from _parser.AlgoPractiseParser import AlgoPractiseParser
from typing import List
from antlr4.Token import CommonToken, Token
from collections.abc import Iterable
from antlr4 import ParserRuleContext
from abc import ABC, abstractmethod


from abstract_syntax.Node import Node
from abstract_syntax.StartNode import StartNode
from abstract_syntax.AssignmentStatementNode import AssignmentStatementNode
from abstract_syntax.BinaryExpressionNode import BinaryExpressionNode
from abstract_syntax.BlockNode import BlockNode
from abstract_syntax.BooleanNode import BooleanNode
from abstract_syntax.DeclarationStatementNode import DeclarationStatementNode
from abstract_syntax.ElseStatementNode import ElseStatementNode
from abstract_syntax.FunctionCallExpressionNode import FunctionCallExpressionNode
from abstract_syntax.FunctionCallStatementNode import FunctionCallStatementNode
from abstract_syntax.FunctionNode import FunctionNode
from abstract_syntax.IfStatementNode import IfStatementNode
from abstract_syntax.ListSubscriptValueNode import ListSubscriptValueNode
from abstract_syntax.NumberNode import NumberNode
from abstract_syntax.ParameterNode import ParameterNode
from abstract_syntax.ReturnStatementNode import ReturnStatementNode
from abstract_syntax.StringNode import StringNode
from abstract_syntax.TypeNode import TypeNode
from abstract_syntax.UnaryExpressionNode import UnaryExpressionNode
from abstract_syntax.WhileStatementNode import WhileStatementNode
from abstract_syntax.StatementNode import StatementNode


class SingleDispatchVisitor(ABC):

    def dispatch(self, node: Node):
        node_type = type(node).__name__
        switcher = {
            "Assign_stmtContext": self.visit_assignment_statement_node,
            "StartContext": self.visit_start_node,
            "StatementContext": self.visit_statement_node,
            "ExprContext": self.visit_expression_node,
            # "BinaryExpressionNode": self.visitBinaryExpressionNode,
            # "UnaryExpressionNode": self.visitUnaryExpressionNode,
            "BlockContext": self.visit_block_node,
            "ValContext": self.visit_val_node,
            # "BooleanNode": self.visitBooleanNode,
            # "NumberNode": self.visitNumberNode,
            # "StringNode": self.visitStringNode,
            "DclContext": self.visit_declaration_statement_node,
            "Else_stmtContext": self.visit_else_statement_node,
            "Func_callContext": self.visit_function_call_statement_node,
            # "FunctionCallExpressionNode": self.visitFunctionCallExpressionNode,
            # "FunctionCallStatementNode": self.visitFunctionCallStatementNode,
            "Func_declContext": self.visit_function_node,
            "If_stmtContext": self.visit_if_statement_node,
            "List_subscriptContext": self.visit_list_subscript_value_node,
            "ParamContext": self.visit_parameter_node,
            # "ReturnStatementNode": self.visitReturnStatementNode,
            "TypeContext": self.visit_type_node,
            "While_stmtContext": self.visit_while_statement_node,
        }
        func = switcher.get(node_type, None)
        if func is None:
            raise NotImplementedError(
                f"Node type {node_type} not implemented in {self.__class__.__name__}")
        return func(node)
    
    @abstractmethod
    def visit_element_list_node(self, cst_node: AlgoPractiseParser.Elmnt_listContext):
        pass

    @abstractmethod
    def visit_statements_node(self):
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
    def visit_binary_expression_node(self, node: BinaryExpressionNode):
        pass

    @abstractmethod
    def visit_block_node(self, node: BlockNode):
        pass

    @abstractmethod
    def visitBooleanNode(self, node: BooleanNode):
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
    def visit_number_node(self, node: NumberNode):
        pass

    @abstractmethod
    def visit_parameter_node(self, node: ParameterNode):
        pass

    @abstractmethod
    def visit_return_statement_node(self, node: ReturnStatementNode):
        pass

    @abstractmethod
    def visit_string_node(self, node: StringNode):
        pass

    @abstractmethod
    def visit_type_node(self, node: TypeNode):
        pass

    @abstractmethod
    def visit_unary_expression_node(self, node: UnaryExpressionNode):
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
