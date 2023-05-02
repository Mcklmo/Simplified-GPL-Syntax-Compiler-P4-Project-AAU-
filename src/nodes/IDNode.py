from .ValueNode import ValueNode

class IDNode(ValueNode):
    def __init__(self, line_number, identifier: str):
        super().__init__(line_number = line_number)
        self.identifier = identifier
        
    def __eq__(self, other):
        instance = isinstance(other, IDNode)
        identifier = self.identifier == other.identifier
        return instance and identifier
    
    def __repr__(self):
        return f"IDNode(identifier={self.identifier})"