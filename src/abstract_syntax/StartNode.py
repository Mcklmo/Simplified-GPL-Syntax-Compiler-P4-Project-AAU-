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
        _=0
        funcs = self.functions == other.functions
        statements = True  
        for i in range(len(self.statements)):
            try:
                if self.statements[i] != other.statements[i]:
                    statements = False
            except:
                return False
        return isinstance(other, StartNode) and funcs and statements
    
    def __repr__(self):
        return f"StartNode(functions={self.functions}, statements={self.statements})"
