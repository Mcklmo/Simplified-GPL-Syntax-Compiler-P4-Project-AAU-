from ValueNode import ValueNode
from ExpressionNode import ExpressionNode
from typing import List, Optional

class FunctionCallExpressionNode(ExpressionNode):
    def __init__(self, identifier: str, arguments: Optional[List[ExpressionNode]]) -> None:
        super().__init__()
        self.identifier = identifier
        self.arguments = arguments