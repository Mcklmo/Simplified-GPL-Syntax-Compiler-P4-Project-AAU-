from .ExpressionNode import ExpressionNode

class BinaryExpressionNode(ExpressionNode):
    def __init__(self, left: ExpressionNode, right: ExpressionNode, operator: str) -> None:
        super().__init__()
        self.left = left
        self.right = right
        self.operator = operator