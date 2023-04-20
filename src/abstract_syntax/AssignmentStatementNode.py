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

