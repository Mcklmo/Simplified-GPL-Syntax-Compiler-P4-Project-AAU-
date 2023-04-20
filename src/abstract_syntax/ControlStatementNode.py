from .StatementNode import StatementNode
from .BlockNode import BlockNode


class ControlStatementNode(StatementNode):
    def __init__(self, condition, block: BlockNode) -> None:
        super().__init__()
        self.block = block
