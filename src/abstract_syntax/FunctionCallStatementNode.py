from .StatementNode import StatementNode
from .ExpressionNode import ExpressionNode
from typing import List, Optional

class FunctionCallStatementNode(StatementNode):
    def __init__(self, identifier: str, arguments: Optional[List[ExpressionNode]]) -> None:
        super().__init__()
        self.identifier = identifier
        self.arguments = arguments
