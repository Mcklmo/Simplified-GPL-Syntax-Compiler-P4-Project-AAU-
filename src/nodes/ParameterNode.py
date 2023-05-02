from .Node import Node
from .IDNode import IDNode
from .TypeNode import TypeNode

class ParameterNode(Node):
    def __init__(self, line_number, identifier: IDNode, _type: TypeNode) -> None:
        super().__init__(line_number = line_number)
        self.identifier = identifier
        self._type = _type