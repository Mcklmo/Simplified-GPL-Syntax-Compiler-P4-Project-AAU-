import nodes 

class BinaryExpressionNode(nodes.ExpressionNode):
    def __init__(self, line_number, left: nodes.ExpressionNode, right: nodes.ExpressionNode, operator: str,type_node=None) -> None:
        super().__init__(line_number = line_number,type_node=type_node)
        self.left = left
        self.right = right
        self.operator = operator

    def __eq__(self, other):
        return isinstance(other, BinaryExpressionNode) and self.left == other.left and self.right == other.right and self.operator == other.operator
    
    def __repr__(self):
        return f"BinaryExpressionNode(left={self.left}, right={self.right}, operator={self.operator})"