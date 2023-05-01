from .ControlStatementNode import ControlStatementNode
from .BlockNode import BlockNode
from .ExpressionNode import ExpressionNode
from typing import Optional

class WhileStatementNode(ControlStatementNode):
    def __init__(self, line_number, condition: ExpressionNode, block: BlockNode) -> None:
        super().__init__(line_number = line_number)
        self.expression = condition
        self.block = block