from .ExpressionNode import ExpressionNode

class UnaryExpressionNode(ExpressionNode):
    def __init__(self, expression: ExpressionNode, operator: str) -> None:
        super().__init__()
        self.expression = expression
        self.operator = operator