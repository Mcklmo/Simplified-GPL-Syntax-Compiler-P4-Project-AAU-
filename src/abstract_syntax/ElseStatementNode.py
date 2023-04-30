from .Node import Node
from .BlockNode import BlockNode
from typing import Optional


class ElseStatementNode(Node):
    def __init__(self, block: BlockNode=None, if_statement: Optional[Node]=None) -> None:
        if not block and not if_statement:
            raise ValueError("Either block or if_statement must be provided to create an ElseStatementNode")
        self.if_statement = if_statement
        self.block = block

    def __eq__(self, other):
        block = self.block == other.block
        if_statement = self.if_statement == other.if_statement
        return isinstance(other, ElseStatementNode) and block and if_statement
    
    def __repr__(self):
        return f"ElseStatementNode(block={self.block}, if_statement={self.if_statement})"