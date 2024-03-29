from nodes.ExpressionNode import ExpressionNode

class BinaryExpressionNode(ExpressionNode):
    def __init__(self, line_number, left: ExpressionNode, right: ExpressionNode, operator: str) -> None:
        super().__init__(line_number = line_number)
        self.left = left
        self.right = right
        self.operator = operator

    def __eq__(self, other):
        return isinstance(other, BinaryExpressionNode) and self.left == other.left and self.right == other.right and self.operator == other.operator
    
    def __repr__(self):
        return f"BinaryExpressionNode(left={self.left}, right={self.right}, operator={self.operator})"