from .ConstantNode import ConstantNode

class StringNode(ConstantNode):
    def __init__(self, value: str) -> None:
        super().__init__()
        self.value = value