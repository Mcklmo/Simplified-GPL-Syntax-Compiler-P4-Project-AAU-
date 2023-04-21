from .Node import Node
from .FunctionNode import FunctionNode
from .StatementNode import StatementNode
from typing import List, Optional

class StartNode(Node):
    def __init__(self, functions: Optional[List[FunctionNode]], statements: Optional[List[StatementNode]] ) -> None:
        super().__init__()
        self.functions: List[FunctionNode] = functions
        self.statements: List[StatementNode] = statements

      
    def __eq__(self, other):
        return isinstance(other, StartNode) and self.functions == other.functions and self.statements == other.statements
    
    def __repr__(self):
        return f"StartNode(functions={self.functions}, statements={self.statements})"
