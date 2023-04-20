from .Node import Node
from .TypeNode import TypeNode

class ParameterNode(Node):
    def __init__(self, identifier: str, type: TypeNode) -> None:
        super().__init__()
        self.identifier = identifier
        self.type = type