from ControlStatementNode import ControlStatementNode
from IfStatementNode import IfStatementNode
from BlockNode import BlockNode
from typing import Optional


class ElseStatement(ControlStatementNode):
    def __init__(self, block: BlockNode, if_statement: Optional[IfStatementNode]) -> None:
        super().__init__(block)
        self.if_statement = if_statement
