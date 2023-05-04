from .ConstantNode import ConstantValueNode

class BooleanNode(ConstantValueNode):
    def __init__(self, value: bool, line_number) -> None:
        super().__init__(line_number = line_number)
        self.value = value

    def __eq__(self, other):
        return isinstance(other, BooleanNode) and self.value == other.value
    
    def __repr__(self):
        return f"BooleanNode(value={self.value})"