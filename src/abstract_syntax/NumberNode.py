from ConstantNode import ConstantNode

class NumberNode(ConstantNode):
    def __init__(self, value: float) -> None:
        super().__init__()
        self.value = value