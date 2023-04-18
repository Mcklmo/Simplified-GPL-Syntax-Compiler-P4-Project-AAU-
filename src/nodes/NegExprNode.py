from .ASTNode import ASTNode

class NegExprNode(ASTNode):
    def __init__(self, line_number) -> None:
        super().__init__()
        self.line_number = line_number
    

    