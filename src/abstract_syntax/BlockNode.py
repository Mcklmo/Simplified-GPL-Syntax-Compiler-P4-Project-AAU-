from .Node import Node
from .StatementsNode import StatementsNode
from typing import List

class BlockNode(Node):
    def __init__(self, statements_node: StatementsNode) -> None:
        super().__init__()
        self.statements_node = statements_node