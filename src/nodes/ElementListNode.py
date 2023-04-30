from .Node import Node 
from .ExpressionNode import ExpressionNode
from typing import List

class ElementListNode(Node):
    def __init__(self,expressions: List[ExpressionNode]):
        self.expressions = expressions