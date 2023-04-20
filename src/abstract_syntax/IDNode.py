from .ValueNode import ValueNode

class IDNode(ValueNode):
    def __init__(self,identifier):
        self.identifier = identifier