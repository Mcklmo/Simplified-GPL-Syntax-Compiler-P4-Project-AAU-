from typing import Iterable, List

class Node:
    """Base class for all nodes in the abstract syntax tree."""

    def __init__(self, **kwargs):
        self.line_number = 0
        for key, value in kwargs.items(): setattr(self, key, value)

    def accept(self, visitor):
        visitor.visit(self)

