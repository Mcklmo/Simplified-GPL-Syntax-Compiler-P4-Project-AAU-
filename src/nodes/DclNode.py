from .ASTNode import ASTNode

class DclNode(ASTNode):
    def __init__(self, id:str, line_number) -> None:
        super().__init__()
        self.id = id
        self.line_number = line_number
    

    