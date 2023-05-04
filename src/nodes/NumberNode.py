from .ConstantNode import ConstantValueNode

class NumberNode(ConstantValueNode):
    def __init__(self, line_number, value: float) -> None:
        super().__init__(line_number = line_number)
        self.value = float(value)

    def __eq__(self, other):
        value = self.value == other.value
        return isinstance(other, NumberNode) and value
    
    def __repr__(self):
        return f"NumberNode(value={self.value})"