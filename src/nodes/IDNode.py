from .ValueNode import ValueNode

class IDNode(ValueNode):
    def __init__(self, line_number, identifier: str):
        super().__init__(line_number = line_number)
        self.identifier = identifier