from _parser.AlgoPractiseParser import AlgoPractiseParser
from abstract_syntax.ElementListNode import ElementListNode

from .SingleDispatchVisitor import SingleDispatchVisitor
from abstract_syntax.StartNode import StartNode
from abstract_syntax.AssignmentStatementNode import AssignmentStatementNode
from abstract_syntax.BlockNode import BlockNode
from abstract_syntax.DeclarationStatementNode import DeclarationStatementNode
from abstract_syntax.ElseStatementNode import ElseStatementNode
from abstract_syntax.FunctionCallStatementNode import FunctionCallStatementNode
from abstract_syntax.FunctionNode import FunctionNode
from abstract_syntax.IfStatementNode import IfStatementNode
from abstract_syntax.ListSubscriptValueNode import ListSubscriptValueNode
from abstract_syntax.ParameterNode import ParameterNode
from abstract_syntax.WhileStatementNode import WhileStatementNode
from abstract_syntax.TypeNode import TypeNode

from abstract_syntax.FunctionCallExpressionNode import FunctionCallExpressionNode
from abstract_syntax.ReturnStatementNode import ReturnStatementNode
from abstract_syntax.UnaryExpressionNode import UnaryExpressionNode
from abstract_syntax.BinaryExpressionNode import BinaryExpressionNode
from abstract_syntax.BooleanNode import BooleanNode
from abstract_syntax.NumberNode import NumberNode
from abstract_syntax.StringNode import StringNode

from abstract_syntax.ExpressionNode import ExpressionNode
from abstract_syntax.ValueNode import ValueNode
from abstract_syntax.StatementNode import StatementNode
from abstract_syntax.IDNode import IDNode


class ASTSingleDispatchVisitor(SingleDispatchVisitor):
    def __init__(self):
        pass

    def visitStartNode(self, cst_node: AlgoPractiseParser.StartContext):

        functions = cst_node.func()
        for function in functions:
            self.visitFunctionNode(function)

        statements = cst_node.stmts()
        self.visitStatementsNode(statements)

        # cfg allows single stmt
        statement = cst_node.stmt()
        if statement:
            statements.append(self.visitStatementNode(statement))

        return StartNode(functions, statements)

    def visitStatementsNode(self, cst_node: AlgoPractiseParser.StmtsContext):
        statements = []
        for stmts in cst_node:
            for statement in stmts.stmt():
                statements.append(self.visitStatementNode(statement))
        return statements

    def visitStatementNode(self, cst_node: AlgoPractiseParser.StmtContext):
        ast_node = None
        # print(type(cst_node),vars(cst_node))
        # exit()
        if cst_node.dcl():
            ast_node = self.visitDeclarationStatementNode(cst_node.dcl())

        elif cst_node.assign_stmt():
            ast_node = self.visitAssignmentStatementNode(
                cst_node.assign_stmt())

        elif cst_node.func_call():
            ast_node = self.visitFunctionCallStatementNode(
                cst_node.func_call())

        elif cst_node.cntrol():
            ast_node = self.visitControlStatementNode(cst_node.cntrol())
        elif cst_node.RETURN() and cst_node.expr():
            ast_node = self.visitReturnStatementNode(cst_node.expr())
        else:
            # return void
            ast_node = self.visitReturnStatementNode(None)

        return ast_node

    def visitControlStatementNode(self, cst_node: AlgoPractiseParser.CntrolContext):
        pass

    def visitAssignmentStatementNode(self, cst_node: AlgoPractiseParser.Assign_stmtContext):
        identifier = cst_node.ID()
        expression = self.visitExpressionNode(cst_node.expr())
        list_subscript_ctx = cst_node.list_subscript()
        list_subscript = None 
        if list_subscript_ctx:
            list_subscript = self.visitListSubscriptValueNode(identifier,
                                                              list_subscript_ctx)
        return AssignmentStatementNode(identifier, list_subscript, expression)

    def visitExpressionNode(self, cst_node: AlgoPractiseParser.ExprContext):
        negation = cst_node.NEG()
        if negation:
            expr = self.visitExpressionNode(cst_node.expr(0))
            operator = negation.getText()
            return UnaryExpressionNode(expr, operator)
        val = cst_node.val()
        if val:
            return self.visitValNode(val)

    def visitValNode(self, cst_node: AlgoPractiseParser.ValContext):
        identifier = cst_node.ID()
        list_subscript = cst_node.list_subscript(0)
        if list_subscript:
            return self.visitListSubscriptValueNode(identifier, list_subscript)
        if identifier:
            return IDNode(identifier)
        numval = cst_node.NUMVAL()
        if numval:
            return NumberNode(numval)
        stringval = cst_node.STRINGVAL()
        if stringval:
            return StringNode(stringval)
        true = cst_node.TRUE()
        if true:
            return BooleanNode(true)
        false = cst_node.FALSE()
        if false:
            return BooleanNode(false)
        elmnt_list = cst_node.elmnt_list()
        if elmnt_list:
            return self.visitElementListNode(elmnt_list)
        func_call = cst_node.func_call()
        if func_call:
            return self.visitFunctionCallExpressionNode(func_call)

    def visitElementListNode(self, cst_node: AlgoPractiseParser.Elmnt_listContext):
        elementList = []
        for element in cst_node.expr():
            elementList.append(self.visitExpressionNode(element))
        return ElementListNode(elementList)

    def visitFunctionCallExpressionNode(self, cst_node: AlgoPractiseParser.Func_callContext):
        identifier = cst_node.ID()
        arguments = self.visitElementListNode(cst_node.elmnt_list())

        return FunctionCallExpressionNode(identifier, arguments)

    def visitListSubscriptValueNode(self, identifier: str, cst_node: AlgoPractiseParser.List_subscriptContext):
        subscripts = []
        for subscript in cst_node.expr():
            subscripts.append(self.visitExpressionNode(subscript))
        return ListSubscriptValueNode(identifier, subscripts)

    def visitBlockNode(self, cst_node: BlockNode):
        print("qux")

    def visitBooleanNode(self, cst_node: BooleanNode):
        print("quux")

    def visitDeclarationStatementNode(self, cst_node: DeclarationStatementNode):
        print("corge")

    def visitElseStatementNode(self, cst_node: ElseStatementNode):
        print("grault")

    def visitFunctionCallStatementNode(self, cst_node: FunctionCallStatementNode):
        print("waldo")

    def visitFunctionNode(self, cst_node: FunctionNode):
        print("fred")

    def visitIfStatementNode(self, cst_node: IfStatementNode):
        print("plugh")

    def visitNumberNode(self, cst_node: NumberNode):
        print("thud")

    def visitParameterNode(self, cst_node: ParameterNode):
        print("thud")

    def visitReturnStatementNode(self, cst_node: ReturnStatementNode):
        print("thud")

    def visitUnaryExpressionNode(self, cst_node: UnaryExpressionNode):
        print("thud")

    def visitWhileStatementNode(self, cst_node: WhileStatementNode):
        print("thud")

    def visitTypeNode(self, cst_node: TypeNode):
        print("thud")

    def visitStringNode(self, cst_node: StringNode):
        print("thud")

    def visitBinaryExpressionNode(self, cst_node: BinaryExpressionNode):
        print("thud")
