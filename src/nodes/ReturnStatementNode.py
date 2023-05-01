from .StatementNode import StatementNode
from .ExpressionNode import ExpressionNode
from typing import Optional


class ReturnStatementNode(StatementNode):
    def __init__(self, line_number, expression: Optional[ExpressionNode] = None) -> None:
        super().__init__(line_number = line_number)
        self.expression = expression
