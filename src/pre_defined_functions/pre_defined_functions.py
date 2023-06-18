from typing import List
from nodes.IDNode import IDNode
from nodes.ParameterNode import ParameterNode
from nodes.TypeNode import TypeNode


class PreDefinedFunction():
    def __init__(self, identifier: IDNode, params: List[ParameterNode], return_type: TypeNode):
        self.identifier = identifier
        self.params = params
        self.return_type = return_type

pre_defined_functions = [
    PreDefinedFunction(IDNode(0, "print"), [ParameterNode(
        0, IDNode(0, "value", TypeNode(0, "string", 0)), TypeNode(0, "string", 0))], TypeNode(0, "void", 0)),
    PreDefinedFunction(IDNode(0, "bool_to_string"), [ParameterNode(
        0, IDNode(0, "value", TypeNode(0, "bool", 0)), TypeNode(0, "bool", 0))], TypeNode(0, "string", 0)),
    PreDefinedFunction(IDNode(0, "num_to_string"), [ParameterNode(
        0, IDNode(0, "value", TypeNode(0, "num", 0)), TypeNode(0, "num", 0))], TypeNode(0, "string", 0)),
]

pre_defined_function_ids = [fn.identifier.identifier for fn in pre_defined_functions]

pre_defined_identifiers_map = {
            "print": "Console.WriteLine",
        }
conversions = ["bool_to_string", "num_to_string"]