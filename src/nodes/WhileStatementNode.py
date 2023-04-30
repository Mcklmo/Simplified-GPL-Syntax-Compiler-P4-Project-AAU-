from .ControlStatementNode import ControlStatementNode
from .BlockNode import BlockNode
from .ExpressionNode import ExpressionNode
from typing import Optional

class WhileStatementNode(ControlStatementNode):
    def __init__(self, condition: ExpressionNode, block: BlockNode) -> None:
        self.expression = condition
        self.block = block