from .ASTNode import ASTNode

class ValExpr(ASTNode):
    def __init__(self, line_number:int) -> None:
        super().__init__()
        self.line_number = line_number
    

    