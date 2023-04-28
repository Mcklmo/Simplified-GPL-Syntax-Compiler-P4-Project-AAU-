from .Node import Node
from .StatementsNode import StatementsNode
from typing import List

class BlockNode(Node):
    def __init__(self, statements_nodes: List[StatementsNode]=[]) -> None:
        super().__init__()
        self.statements_nodes = statements_nodes

    def __eq__(self, other):
        return isinstance(other, BlockNode) and self.statements_nodes == other.statements_nodes
    
    def __repr__(self):
        return f"BlockNode(statements_nodes={self.statements_nodes})"