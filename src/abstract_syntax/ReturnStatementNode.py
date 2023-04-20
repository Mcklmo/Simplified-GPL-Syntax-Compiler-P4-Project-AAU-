from .StatementNode import StatementNode
from .ExpressionNode import ExpressionNode
from typing import Optional

class ReturnStatementNode(StatementNode):
    def __init__(self, expression: Optional[ExpressionNode]) -> None:
        super().__init__()
        self.expression = expression