from .Node import Node
from .StatementNode import StatementNode
from typing import List 

class StatementsNode(Node):
    def __init__(self, line_number, statements: List[StatementNode]) -> None:
        super().__init__(line_number = line_number)
        self.statements = statements
        