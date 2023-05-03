import nodes

class ASTTypeChecker():
    def __init__(self):
        pass

    def UnaryNodeTypeChecker(self, node: nodes.UnaryExpressionNode): # Boolean expr should be handled here
        pass

    def BinaryNodeTypeChecker(self, node: nodes.UnaryExpressionNode): # Boolean expr should be handled here
        pass

    def AssignmentNodeTypeChecker(self, node: nodes.AssignmentStatementNode):
        pass

    def ReturnNodeTypeChecker(self, node: nodes.ReturnStatementNode):
        pass

    def ExpressionNodeTypeChecker(self, node: nodes.ExpressionNode):
        pass

    def DeclareNodeTypeChecker(self, node: nodes.DeclarationStatementNode):
        pass

    def ListSubscriptNodeTypeChecker(self, node: nodes.ListSubscriptValueNode):
        pass