from typing import Iterable, List

class Node:
    """Base class for all nodes in the abstract syntax tree."""

    def __init__(self):
        pass

    def accept(self, visitor):
        visitor.visit(self)

