from .ControlStatementNode import ControlStatementNode
from .BlockNode import BlockNode
from .ExpressionNode import ExpressionNode
from .ElseStatementNode import ElseStatementNode
from typing import Optional

class IfStatementNode(ControlStatementNode):
    def __init__(self, condition: ExpressionNode, block: BlockNode, else_node : Optional[ElseStatementNode] = None) -> None:
        self.condition = condition
        self.else_node = else_node
        self.block = block

    def __eq__(self, other):
        cond = self.condition == other.condition
        block = self.block == other.block
        else_node = self.else_node == other.else_node
        return isinstance(other, IfStatementNode) and cond and block and else_node
    
    def __repr__(self):
        return f"IfStatementNode(condition={self.condition}, block={self.block}, else_node={self.else_node})"