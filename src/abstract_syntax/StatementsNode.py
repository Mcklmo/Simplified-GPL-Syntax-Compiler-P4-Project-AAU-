from .Node import Node
from .StatementNode import StatementNode
from typing import List 

class StatementsNode(Node):
    def __init__(self,statements: List[StatementNode]):
        self.statements = statements