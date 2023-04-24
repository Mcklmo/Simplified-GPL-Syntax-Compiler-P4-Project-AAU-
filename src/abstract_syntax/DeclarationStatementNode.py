from .StatementNode import StatementNode
from .TypeNode import TypeNode
from .AssignmentStatementNode import AssignmentStatementNode
from typing import Optional

class DeclarationStatementNode(StatementNode):
    def __init__(self, type: TypeNode, assignment: Optional[AssignmentStatementNode] =None,identifier:str=None):
        if not identifier and not assignment:
            raise Exception("DeclarationStatementNode must have either an identifier or an assignment")
        super().__init__()
        self.type = type
        self.assignment = assignment
        self.identifier = identifier