from .StatementNode import StatementNode
from .TypeNode import TypeNode
from .AssignmentStatementNode import AssignmentStatementNode
from typing import Optional

class DeclarationStatementNode(StatementNode):
    def __init__(self, type: TypeNode, assignment: Optional[AssignmentStatementNode]  ):
        super().__init__()
        self.type = type
        self.assignment = assignment