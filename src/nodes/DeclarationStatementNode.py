from .StatementNode import StatementNode
from .TypeNode import TypeNode
from .IDNode import IDNode
from .AssignmentStatementNode import AssignmentStatementNode
from typing import Optional

class DeclarationStatementNode(StatementNode):
    """The declarations without identifiers have assignments with identifiers."""
    def __init__(self, type: TypeNode, line_number, assignment: Optional[AssignmentStatementNode] =None,identifier:IDNode=None):
        if not identifier and not assignment:
            raise Exception("DeclarationStatementNode must have either an identifier or an assignment")
        super().__init__(line_number = line_number)
        self.type = type
        self.assignment = assignment
        self.identifier = identifier
        
        # symbol table populated
        self.is_global = False

    def __eq__(self, other):
        _type = self.type == other.type
        assignment = self.assignment == other.assignment
        identifier = self.identifier == other.identifier
        return isinstance(other, DeclarationStatementNode) and _type and assignment and identifier
    
    def __repr__(self):
        return f"DeclarationStatementNode(type={self.type}, assignment={self.assignment}, identifier={self.identifier})"