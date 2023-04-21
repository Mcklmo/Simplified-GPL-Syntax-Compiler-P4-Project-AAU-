from .Node import Node
from .FunctionNode import FunctionNode
from .StatementNode import StatementNode
from typing import List, Optional

class StartNode(Node):
    def __init__(self, functions: Optional[List[FunctionNode]], statements: Optional[List[StatementNode]] ) -> None:
        super().__init__()
        self.functions = functions
        self.statements_node = statements