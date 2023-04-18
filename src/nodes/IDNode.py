from .ASTNode import ASTNode

class IDNode(ASTNode):
    def __init__(self, id:str, type:str="", line_number=0) -> None:
        super().__init__(line_number = line_number)
        self.id = id
        self.type = type
    

    