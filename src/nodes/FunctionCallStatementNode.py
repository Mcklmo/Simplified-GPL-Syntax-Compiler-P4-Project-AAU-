from .StatementNode import StatementNode
from .IDNode import IDNode
from .ExpressionNode import ExpressionNode
from typing import List, Optional

class FunctionCallStatementNode(StatementNode):
    def __init__(self, line_number, identifier: IDNode, arguments: Optional[List[ExpressionNode]]=[]) -> None:
        super().__init__(line_number = line_number)
        self.identifier = identifier
        self.arguments = arguments

        # From symboltabel
        self.dcl_type = None