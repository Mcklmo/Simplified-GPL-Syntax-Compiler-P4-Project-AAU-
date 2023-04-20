from ConstantNode import ConstantNode

class BooleanNode(ConstantNode):
    def __init__(self, value: bool) -> None:
        super().__init__()
        self.value = value