from .ASTNode import ASTNode

class ParenthesesExpr(ASTNode):
    def __init__(self, line_number) -> None:
        super().__init__()
        self.line_number = line_number
    

    