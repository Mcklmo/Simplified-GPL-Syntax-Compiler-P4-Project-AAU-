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

    def Dispatch(self, node: Node):
        node_type = type(node).__name__
        switcher = {
            "Assign_stmtContext": self.visitAssignmentStatementNode,
            "StartContext": self.visitStartNode,
            "StatementContext": self.visitStatementNode,
            "ExprContext": self.visitExpressionNode,
            # "BinaryExpressionNode": self.visitBinaryExpressionNode,
            # "UnaryExpressionNode": self.visitUnaryExpressionNode,
            "BlockContext": self.visitBlockNode,
            "ValContext": self.visitValNode,
            # "BooleanNode": self.visitBooleanNode,
            # "NumberNode": self.visitNumberNode,
            # "StringNode": self.visitStringNode,
            "DclContext": self.visitDeclarationStatementNode,
            "Else_stmtContext": self.visitElseStatementNode,
            "Func_callContext": self.visitFunctionCallStatementNode,
            # "FunctionCallExpressionNode": self.visitFunctionCallExpressionNode,
            # "FunctionCallStatementNode": self.visitFunctionCallStatementNode,
            "Func_declContext": self.visitFunctionNode,
            "If_stmtContext": self.visitIfStatementNode,
            "List_subscriptContext": self.visitListSubscriptValueNode,
            "ParamContext": self.visitParameterNode,
            # "ReturnStatementNode": self.visitReturnStatementNode,
            "TypeContext": self.visitTypeNode,
            "While_stmtContext": self.visitWhileStatementNode,
        }
        func = switcher.get(node_type, None)
        if func is None:
            raise NotImplementedError(
                f"Node type {node_type} not implemented in {self.__class__.__name__}")
        return func(node)
    
    @abstractmethod
    def visitElementListNode(self, cst_node: AlgoPractiseParser.Elmnt_listContext):
        pass

    @abstractmethod
    def visitStatementsNode(self):
        pass

    @abstractmethod
    def visitControlStatementNode(self, node):
        pass

    @abstractmethod
    def visitStatementNode(self, node: StatementNode):
        pass

    @abstractmethod
    def visitAssignmentStatementNode(self, node: AssignmentStatementNode):
        pass

    @abstractmethod
    def visitStartNode(self, node: StartNode):
        pass

    @abstractmethod
    def visitBinaryExpressionNode(self, node: BinaryExpressionNode):
        pass

    @abstractmethod
    def visitBlockNode(self, node: BlockNode):
        pass

    @abstractmethod
    def visitBooleanNode(self, node: BooleanNode):
        pass

    @abstractmethod
    def visitDeclarationStatementNode(self, node: DeclarationStatementNode):
        pass

    @abstractmethod
    def visitElseStatementNode(self, node: ElseStatementNode):
        pass

    @abstractmethod
    def visitFunctionCallExpressionNode(self, node: FunctionCallExpressionNode):
        pass

    @abstractmethod
    def visitFunctionCallStatementNode(self, node: FunctionCallStatementNode):
        pass

    @abstractmethod
    def visitFunctionNode(self, node: FunctionNode):
        pass

    @abstractmethod
    def visitIfStatementNode(self, node: IfStatementNode):
        pass

    @abstractmethod
    def visitListSubscriptValueNode(self,identifier:str ,node: ListSubscriptValueNode):
        pass

    @abstractmethod
    def visitNumberNode(self, node: NumberNode):
        pass

    @abstractmethod
    def visitParameterNode(self, node: ParameterNode):
        pass

    @abstractmethod
    def visitReturnStatementNode(self, node: ReturnStatementNode):
        pass

    @abstractmethod
    def visitStringNode(self, node: StringNode):
        pass

    @abstractmethod
    def visitTypeNode(self, node: TypeNode):
        pass

    @abstractmethod
    def visitUnaryExpressionNode(self, node: UnaryExpressionNode):
        pass

    @abstractmethod
    def visitWhileStatementNode(self, node: WhileStatementNode):
        pass

    @abstractmethod
    def visitExpressionNode(self, node: Node):
        pass

    @abstractmethod
    def visitValNode(self, node: Node):
        pass
