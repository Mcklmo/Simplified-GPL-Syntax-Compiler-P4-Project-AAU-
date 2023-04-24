from .ControlStatementNode import ControlStatementNode
from .BlockNode import BlockNode
from typing import Optional


class ElseStatementNode(ControlStatementNode):
    def __init__(self, block: BlockNode=None, if_statement: Optional[ControlStatementNode]=None) -> None:
        if not block and not if_statement:
            raise ValueError("Either block or if_statement must be provided to create an ElseStatementNode")
        self.if_statement = if_statement
        self.block = block