from typing import List

class Node:
    """Base class for all nodes in the abstract syntax tree."""

    def __init__(self):
        pass

    def accept(self, visitor):
        visitor.visit(self)

    def pretty_print(self, indent: str = ""):
        print(indent, type(self).__name__)
        indent += "    "
        for attribute_name, attribute_value in vars(self).items():
            if isinstance(attribute_value, Node):
                self.pretty_print(attribute_value, indent)
            elif isinstance(attribute_value, list):
                for item in attribute_value:
                    if isinstance(attribute_value, Node):
                        self.pretty_print(item, indent)
                    else:
                        print(indent, attribute_name, item)
            else:
                print(indent, attribute_name, attribute_value)
