from .Node import Node

class TypeNode(Node):
    def __init__(self, line_number, type: str, dimensions :int) -> None:
        super().__init__(line_number = line_number)
        self.type = type
        self.dimensions = dimensions

    def __eq__(self, other):
        if not isinstance(other, TypeNode): return False

        _type = self.type == other.type
        dimensions = self.dimensions == other.dimensions
        return _type and dimensions
    
    def __repr__(self):
        return f"TypeNode(type={self.type}, dimensions={self.dimensions})"
    
    def __str__(self):
        return self.__repr__()