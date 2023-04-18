from .ASTNode import ASTNode

class Func_callNode(ASTNode):
    
    def __init__(self,line_number:int,id:str):
        super().__init__()
        self.id = id 
        self.line_number = line_number