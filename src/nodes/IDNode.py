from .ValueNode import ValueNode
from .TypeNode import TypeNode

class IDNode(ValueNode):
    def __init__(self, line_number, identifier: str, dcl_type:TypeNode = None):
        super().__init__(line_number = line_number)
        self.identifier = identifier

        # Symbol table populated
        self.dcl_type  = dcl_type
        self.dcl_dimensions = None
        
    def __eq__(self, other):
        instance = isinstance(other, IDNode)
        identifier = self.identifier == other.identifier
        return instance and identifier
    
    def __repr__(self):
        return f"IDNode(identifier={self.identifier})"