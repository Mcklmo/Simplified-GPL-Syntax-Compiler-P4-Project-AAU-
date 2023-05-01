from .Node import Node
from .StatementsNode import StatementsNode
from typing import List

class BlockNode(Node):
    def __init__(self, line_number, statements_nodes: List[StatementsNode]=[]) -> None:
        super().__init__(line_number=line_number)
        self.statements_nodes = statements_nodes

    def __eq__(self, other):
        statements_nodes = self.statements_nodes == other.statements_nodes
        return isinstance(other, BlockNode) and statements_nodes
    
    def __repr__(self):
        return f"BlockNode(statements_nodes={self.statements_nodes})"