from nodes import Node 
from nodes import TypeNode

class ExpressionNode(Node):
    def __init__(self, line_number,type_node:TypeNode=None) -> None:
        super().__init__(line_number = line_number)
        self.type_node = type_node