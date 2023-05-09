from .ExpressionNode import ExpressionNode
from .IDNode import IDNode
from typing import List, Optional

class FunctionCallExpressionNode(ExpressionNode):
    def __init__(self, line_number, identifier: IDNode, arguments: Optional[List[ExpressionNode]]) -> None:
        super().__init__(line_number = line_number)
        self.identifier = identifier
        self.arguments = arguments

        # From symboltabel
        self.dcl_type = None
        self.dcl_node = None

    def __eq__(self, other):
        return isinstance(other, FunctionCallExpressionNode) and self.identifier == other.identifier and self.arguments == other.arguments
    
    def __repr__(self):
        return f"FunctionCallExpressionNode(identifier={self.identifier}, arguments={self.arguments})"