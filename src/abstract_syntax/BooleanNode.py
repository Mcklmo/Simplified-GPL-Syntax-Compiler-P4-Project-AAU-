from .ConstantNode import ConstantNode

class BooleanNode(ConstantNode):
    def __init__(self, value: bool) -> None:
        super().__init__()
        self.value = value

    def __eq__(self, other):
        return isinstance(other, BooleanNode) and self.value == other.value
    
    def __repr__(self):
        return f"BooleanNode(value={self.value})"