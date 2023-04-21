from .Node import Node
from .TypeNode import TypeNode
from .ParameterNode import ParameterNode
from .BlockNode import BlockNode

from typing import List

class FunctionNode(Node):
    def __init__(self, identifier: str,type:TypeNode, params: List[ParameterNode], block: BlockNode) -> None:
        super().__init__()
        self.identifier   = identifier
        self.params = params
        self.block   = block 
    
    def __eq__(self, other):
        print("hello im alive")
        return isinstance(other, FunctionNode) and self.identifier == other.identifier and self.params == other.params and self.block == other.block
    
    def __repr__(self):
        return f"FunctionNode(identifier={self.identifier}, params={self.params}, block={self.block})"