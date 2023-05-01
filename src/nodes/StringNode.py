from .ConstantNode import ConstantNode

class StringNode(ConstantNode):
    def __init__(self, line_number, value: str) -> None:
        super().__init__(line_number = line_number)
        self.value = value

    def __eq__(self, other):
        return isinstance(other, StringNode) and self.value == other.value
    
    def __repr__(self):
        return f"StringNode(value={self.value})"