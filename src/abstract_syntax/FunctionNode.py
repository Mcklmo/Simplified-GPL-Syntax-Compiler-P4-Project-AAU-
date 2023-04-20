from Node import Node
from TypeNode import TypeNode
from ParameterNode import ParameterNode
from typing import List
from BlockNode import BlockNode

class FunctionNode(Node):
    def __init__(self, identifier: str,type:TypeNode, params: List[ParameterNode], block: BlockNode) -> None:
        super().__init__()
        self.identifier   = identifier
        self.params = params
        self.block   = block 