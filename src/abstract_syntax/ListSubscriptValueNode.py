from .ValueNode import ValueNode
from .ExpressionNode import ExpressionNode
from typing import List 

class ListSubscriptValueNode(ValueNode):
    def __init__(self, identifier: str, subscripts: List[ExpressionNode]) -> None:
        super().__init__()
        self.identifier = identifier
        self.subscripts = subscripts