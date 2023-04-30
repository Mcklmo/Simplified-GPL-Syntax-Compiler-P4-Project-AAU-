from .ExpressionNode import ExpressionNode
from typing import List, Optional

class FunctionCallExpressionNode(ExpressionNode):
    def __init__(self, identifier: str, arguments: Optional[List[ExpressionNode]]) -> None:
        super().__init__()
        self.identifier = identifier
        self.arguments = arguments

        # From symboltabel
        self.dcl_type = None

    def __eq__(self, other):
        return isinstance(other, FunctionCallExpressionNode) and self.identifier == other.identifier and self.arguments == other.arguments
    
    def __repr__(self):
        return f"FunctionCallExpressionNode(identifier={self.identifier}, arguments={self.arguments})"