from Node import Node
from StatementNode import StatementNode
from typing import List

class BlockNode(Node):
    def __init__(self, statements: List[StatementNode]) -> None:
        super().__init__()
        self.statements = statements