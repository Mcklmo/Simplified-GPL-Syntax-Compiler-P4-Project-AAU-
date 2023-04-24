from .ControlStatementNode import ControlStatementNode

class ElseIfStatementNode(ControlStatementNode):
    def __init__(self, if_statement: ControlStatementNode):
        self.ifstatement = if_statement