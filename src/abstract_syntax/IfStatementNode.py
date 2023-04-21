from .ControlStatementNode import ControlStatementNode
from .BlockNode import BlockNode
from .ExpressionNode import ExpressionNode
from .ElseStatementNode import ElseStatementNode
from typing import Optional

class IfStatementNode(ControlStatementNode):
    def __init__(self, condition: ExpressionNode, block: BlockNode, else_block : Optional[ElseStatementNode] = None) -> None:
        super().__init__(block)
        self.condition = condition
        self.else_block = else_block

