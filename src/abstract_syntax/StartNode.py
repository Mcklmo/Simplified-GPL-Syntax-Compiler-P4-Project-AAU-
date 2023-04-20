from Node import Node
from FunctionNode import FunctionNode
from StatementNode import StatementNode
from typing import List


class StartNode(Node):
    def __init__(self, functions: List[FunctionNode], statements: List[StatementNode]) -> None:
        super().__init__()
        self.functions: List[FunctionNode] = functions
        self.statements: List[StatementNode] = statements
