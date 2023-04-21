from .ConstantNode import ConstantNode

class NumberNode(ConstantNode):
    def __init__(self, value: float) -> None:
        super().__init__()
        self.value = float(value)

    def __eq__(self, other):
        return isinstance(other, NumberNode) and self.value == other.value
    
    def __repr__(self):
        return f"NumberNode(value={self.value})"