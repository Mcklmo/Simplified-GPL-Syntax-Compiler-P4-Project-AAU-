from .ASTNode import ASTNode

class Assign_stmtNode(ASTNode):
    def __init__(self,  line_number=0) -> None:
        super().__init__(line_number=line_number)

    

    