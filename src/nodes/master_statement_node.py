from .Node import Node 
from .FunctionNode import FunctionNode
from .StatementNode import StatementNode

class MasterStatementNode(Node):
    """either a function decl or a statement"""
    def __init__(self, line_number, function_node: FunctionNode=None, statement_node: StatementNode=None) -> None:
        super().__init__(line_number = line_number)
        self.function_node = function_node
        self.statement_node = statement_node

        
      
    def __eq__(self, other):
        function_node = self.function_node == other.function_node 
        statement_node = self.statement_node == other.statement_node
        return isinstance(other, MasterStatementNode) and function_node and statement_node
    
    def __repr__(self):
        return f"MasterStatementNode(function_node={self.function_node}, statement_node={self.statement_node})"
