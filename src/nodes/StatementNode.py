from .Node import Node

class StatementNode(Node):
    def __init__(self, line_number) -> None:
        super().__init__(line_number = line_number)