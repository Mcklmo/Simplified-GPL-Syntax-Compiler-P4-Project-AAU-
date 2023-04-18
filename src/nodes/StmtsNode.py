from .ASTNode import ASTNode

class StmtsNode(ASTNode):
    def __init__(self, line_number:int):
        super().__init__()
        self.line_number = line_number