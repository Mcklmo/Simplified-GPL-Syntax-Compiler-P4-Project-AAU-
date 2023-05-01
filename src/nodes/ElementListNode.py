from .Node import Node 
from .ExpressionNode import ExpressionNode
from typing import List

class ElementListNode(Node):
    def __init__(self,expressions: List[ExpressionNode], line_number) -> None:
        super().__init__(line_number = line_number)
        self.expressions = expressions