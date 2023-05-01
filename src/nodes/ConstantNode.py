from .ValueNode import ValueNode

class ConstantNode(ValueNode):
    def __init__(self, line_number):
        super().__init__(line_number = line_number)