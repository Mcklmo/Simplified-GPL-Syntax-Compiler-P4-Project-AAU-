from .ValueNode import ValueNode
from .ExpressionNode import ExpressionNode
from typing import List 

class ListSubscriptValueNode(ValueNode):
    def __init__(self, identifier: str, subscripts: List[ExpressionNode]) -> None:
        super().__init__()
        self.identifier = identifier
        self.subscripts = subscripts

    def __eq__(self, other):
        instance = isinstance(other, ListSubscriptValueNode)
        identifier = self.identifier == other.identifier
        subscripts = self.subscripts == other.subscripts

        return instance and identifier and subscripts
    
    def __repr__(self):
        return f"ListSubscriptValueNode(identifier={self.identifier}, subscripts={self.subscripts})"