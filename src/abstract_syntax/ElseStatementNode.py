from .ControlStatementNode import ControlStatementNode
from .BlockNode import BlockNode
from typing import Optional


class ElseStatementNode(ControlStatementNode):
    def __init__(self, block: BlockNode, if_statement: Optional[ControlStatementNode]) -> None:
        super().__init__(block)
        self.if_statement = if_statement
