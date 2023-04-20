from .Node import Node

class TypeNode(Node):
    def __init__(self, type: str, dimensions :int) -> None:
        super().__init__()
        self.type = type
        self.dimensions = dimensions