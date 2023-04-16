from .ASTNode import ASTNode

class IDNode(ASTNode):
    def __init__(self, id:str, line_number) -> None:
        super().__init__(line_number = line_number)
        self.id = id

    

    