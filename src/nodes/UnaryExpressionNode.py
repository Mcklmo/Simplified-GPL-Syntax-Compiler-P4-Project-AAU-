import nodes
class UnaryExpressionNode(nodes.ExpressionNode):
    def __init__(self, line_number, expression: nodes.ExpressionNode, operator: str,type_node=None) -> None:
        super().__init__(line_number = line_number,type_node=type_node)
        self.expression = expression
        self.operator = operator

    def __eq__(self, other):
        return isinstance(other, UnaryExpressionNode) and self.expression == other.expression and self.operator == other.operator
    
    def __repr__(self):
        return f"UnaryExpressionNode(expression={self.expression}, operator={self.operator})"