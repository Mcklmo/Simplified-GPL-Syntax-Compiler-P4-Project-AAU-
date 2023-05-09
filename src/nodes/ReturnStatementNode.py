from .StatementNode import StatementNode
from .ExpressionNode import ExpressionNode
from .TypeNode import TypeNode
from typing import Optional


class ReturnStatementNode(StatementNode):
    def __init__(self, line_number, expression: Optional[ExpressionNode] = None, expected_return_type:TypeNode=None) -> None:
        super().__init__(line_number = line_number)
        self.expression = expression
        self.expected_return_type = expected_return_type
