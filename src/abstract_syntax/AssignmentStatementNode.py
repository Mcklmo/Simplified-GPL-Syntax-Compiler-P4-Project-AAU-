from StatementNode import StatementNode
from typing import List, Optional
from ExpressionNode import ExpressionNode

class AssignmentStatementNode(StatementNode):
    
    """
    either subscripts or expression have to be set
		"""
    def __init__(self, identifier: str, subscripts: Optional[List[ExpressionNode]], expression: Optional[ExpressionNode]) -> None:
        super().__init__()
        if not subscripts and not expression:
            raise Exception("either subscripts or expression have to be set to create an assignment statement node")
        self.identifier = identifier
        self.subscripts = subscripts
        self.expression = expression

