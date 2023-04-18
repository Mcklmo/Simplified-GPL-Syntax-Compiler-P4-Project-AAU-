from .ASTNode import ASTNode

class StmtNode(ASTNode):
    def __init__(self, line_number:int):
        super().__init__()
        self.line_number = line_number