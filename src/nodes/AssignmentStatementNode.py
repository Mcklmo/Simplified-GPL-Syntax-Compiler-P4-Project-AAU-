from .StatementNode import StatementNode
from .ExpressionNode import ExpressionNode

from typing import List, Optional

class AssignmentStatementNode(StatementNode):
    
    """
    either subscripts or expression will be be set according to the grammar
		"""
    def __init__(self, line_number, identifier: str, subscripts: Optional[List[ExpressionNode]]=None, expression: Optional[ExpressionNode]=None) -> None:
        super().__init__(line_number=line_number)
        self.identifier = identifier
        self.subscripts = subscripts
        self.expression = expression

  
    # Add __eq__ method
    def __eq__(self, other):
        expression = self.expression == other.expression
        identifier = self.identifier == other.identifier
        subscripts = self.subscripts == other.subscripts
        return isinstance(other, AssignmentStatementNode) and expression and identifier and subscripts
    
    # Add __repr__ method
    def __repr__(self):
        return f"AssignmentStatementNode(identifier={self.identifier}, subscripts={self.subscripts}, expression={self.expression})"