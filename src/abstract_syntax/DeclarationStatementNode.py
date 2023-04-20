from StatementNode import StatementNode
from TypeNode import TypeNode
from AssignmentStatementNode import AssignmentStatementNode

class DeclarationStatementNode(StatementNode):
    def __init__(self, type: TypeNode, assignment: AssignmentStatementNode = None ) -> None:
        super().__init__()
        self.type = type
        self.value = assignment