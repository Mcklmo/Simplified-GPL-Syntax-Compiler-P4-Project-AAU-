import nodes
from symbol_table.stack import Stack
from abc import ABC, abstractmethod

class AbstractSymbolTableVisitor(ABC):
    
    @abstractmethod
    def visitAssignmentStatementNode(self, node: nodes.AssignmentStatementNode):
        pass
    
    @abstractmethod
    def visitBinaryExpressionNode(self, node: nodes.BinaryExpressionNode):
        pass
    
    @abstractmethod
    def visitBlockNode(self, node: nodes.BlockNode):
        pass
    
    @abstractmethod
    def visitBooleanNode(self, node: nodes.BooleanNode):
        pass
    
    @abstractmethod
    def visitConstantNode(self, node: nodes.ConstantNode):
        pass
    
    @abstractmethod
    def visitControlStatementNode(self, node: nodes.ControlStatementNode):
        pass
    
    @abstractmethod
    def visitDeclarationStatementNode(self, node: nodes.DeclarationStatementNode):
        pass
    
    @abstractmethod
    def visitElementListNode(self, node: nodes.ElementListNode):
        pass
    
    @abstractmethod
    def visitElseStatementNode(self, node: nodes.ElseStatementNode):
        pass
    
    @abstractmethod
    def visitFunctionCallExpressionNode(self, node: nodes.FunctionCallExpressionNode):
        pass
    
    @abstractmethod
    def visitFunctionCallStatementNode(self, node: nodes.FunctionCallStatementNode):
        pass
    
    @abstractmethod
    def visitFunctionNode(self, node: nodes.FunctionNode):
        pass
    
    @abstractmethod
    def visitIfStatementNode(self, node: nodes.IfStatementNode):
        pass
    
    @abstractmethod
    def visitListSubscriptValueNode(self, node: nodes.ListSubscriptValueNode):
        pass
    
    @abstractmethod
    def visitMasterStatementNode(self, node: nodes.MasterStatementNode):
        pass
    
    @abstractmethod
    def visitNumberNode(self, node: nodes.NumberNode):
        pass
    
    @abstractmethod
    def visitParameterNode(self, node: nodes.ParameterNode):
        pass
    
    @abstractmethod
    def visitReturnStatementNode(self, node: nodes.ReturnStatementNode):
        pass
    
    @abstractmethod
    def visitStartNode(self, node: nodes.StartNode):
        pass
    
    @abstractmethod
    def visitStringNode(self, node: nodes.StringNode):
        pass
    
    @abstractmethod
    def visitTypeNode(self, node: nodes.TypeNode):
        pass
    
    @abstractmethod
    def visitUnaryExpressionNode(self, node: nodes.UnaryExpressionNode):
        pass
    
    @abstractmethod
    def visitValueNode(self, node: nodes.ValueNode):
        pass
    
    @abstractmethod
    def visitWhileStatementNode(self, node: nodes.WhileStatementNode):
        pass
    
    @abstractmethod
    def visitExprNode(self, node: nodes.ExpressionNode):
        pass