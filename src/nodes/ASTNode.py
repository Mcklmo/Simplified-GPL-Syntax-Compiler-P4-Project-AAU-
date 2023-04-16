
class ASTNode():
    def __init__(self, **kwargs) -> None:
        self.children = list()
        self.line_number = 0
        self.node_type = ""

        for key, value in kwargs.items(): setattr(self, key, value)

    
    def accept(self, visitor):
        visitor.visit(self)