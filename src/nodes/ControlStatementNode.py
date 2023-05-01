from .StatementNode import StatementNode
from .BlockNode import BlockNode


class ControlStatementNode(StatementNode):
    def __init__(self, line_number):
        super().__init__(line_number = line_number)