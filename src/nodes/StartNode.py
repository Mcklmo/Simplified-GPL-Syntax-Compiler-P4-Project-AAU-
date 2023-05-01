from .Node import Node
from .master_statement_node import MasterStatementNode
from typing import List, Optional

class StartNode(Node):
    def __init__(self, line_number, master_statement_nodes: Optional[List[MasterStatementNode]]=None) -> None:
        super().__init__(line_number = line_number)
        self.master_statement_nodes: List[MasterStatementNode] = master_statement_nodes
      
    def __eq__(self, other):
        _=0
        master_statement_nodes = self.master_statement_nodes == other.master_statement_nodes
        return isinstance(other, StartNode) and master_statement_nodes
    
    def __repr__(self):
        return f"StartNode(master_statement_nodes={self.master_statement_nodes})"
