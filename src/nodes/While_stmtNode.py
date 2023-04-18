from .ASTNode import ASTNode

class While_stmtNode(ASTNode):
    def __init__(self, line_number:int) -> None:
        super().__init__(line_number=line_number)