from .ConstantNode import ConstantNode

class NumberNode(ConstantNode):
    def __init__(self, value: float) -> None:
        super().__init__()
        self.value = float(value)

    def __eq__(self, other):
        value = self.value == other.value
        return isinstance(other, NumberNode) and value
    
    def __repr__(self):
        return f"NumberNode(value={self.value})"