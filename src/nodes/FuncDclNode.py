from .DclNode import DclNode

class FuncDclNode(DclNode):
    def __init__(self, id:str, return_type:str, line_number:int=0) -> None:
        super().__init__(id, line_number)
        self.return_type = return_type

    

    