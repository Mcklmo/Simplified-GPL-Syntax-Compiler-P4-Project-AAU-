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
