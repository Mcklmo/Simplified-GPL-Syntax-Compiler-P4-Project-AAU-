from .DclNode import DclNode

# I think we could just make a generic "DclNode" as we are not type dependendt (we can get .type for type)
class NumDclNode(DclNode):
    def __init__(self, id:str, line_number=0) -> None:
        super().__init__(id, line_number)


    