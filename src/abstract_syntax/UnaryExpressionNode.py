from .ExpressionNode import ExpressionNode

class UnaryExpressionNode(ExpressionNode):
    def __init__(self, expression: ExpressionNode, operator: str) -> None:
        super().__init__()
        self.expression = expression
        self.operator = operator

    def __eq__(self, other):
        return isinstance(other, UnaryExpressionNode) and self.expression == other.expression and self.operator == other.operator
    
    def __repr__(self):
        return f"UnaryExpressionNode(expression={self.expression}, operator={self.operator})"