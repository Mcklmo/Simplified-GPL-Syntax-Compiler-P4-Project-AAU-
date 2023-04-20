from .ASTNode import ASTNode

class ValNode(ASTNode):
    def __init__(self, line_number:int,type_:str,value) -> None:
        super().__init__()
        self.line_number = line_number
        self.type = type_
        self.value = value

    

    