from .StatementNode import StatementNode
from .ExpressionNode import ExpressionNode

from typing import List, Optional

class AssignmentStatementNode(StatementNode):
    
    """
    either subscripts or expression will be be set according to the grammar
		"""
    def __init__(self, identifier: str, subscripts: Optional[List[ExpressionNode]], expression: Optional[ExpressionNode]) -> None:
        super().__init__()
        self.identifier = identifier
        self.subscripts = subscripts
        self.expression = expression

  
    # Add __eq__ method
    def __eq__(self, other):
        return isinstance(other, AssignmentStatementNode) and self.expression == other.expression and self.identifier == other.identifier and self.subscripts == other.subscripts
    
    # Add __repr__ method
    def __repr__(self):
        return f"AssignmentStatementNode(identifier={self.identifier}, subscripts={self.subscripts}, expression={self.expression})"