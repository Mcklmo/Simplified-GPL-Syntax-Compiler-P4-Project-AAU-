from .DclNode import DclNode

class ListDclNode(DclNode):
    def __init__(self, id:str, type:str, nested_level:int=0, line_number=0) -> None:
        super().__init__(id, line_number)
        self.nested_level = nested_level
        self.type = type


    