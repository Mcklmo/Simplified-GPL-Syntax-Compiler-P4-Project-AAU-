from .ExpressionNode import ExpressionNode

class ValueNode(ExpressionNode):
    def __init__(self, line_number):
        super().__init__(line_number = line_number)