from .ASTNode import ASTNode

class BinExpr(ASTNode):
    def __init__(self, operator:str, line_number) -> None:
        super().__init__()
        self.operator = operator
        self.line_number = line_number
    

    