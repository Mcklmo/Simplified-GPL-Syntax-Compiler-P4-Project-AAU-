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


class ASTSingleDispatchVisitor(SingleDispatchVisitor):
    def __init__(self):
        pass

    def visit_start_node(self, cst_node: AlgoPractiseParser.StartContext):

        functions = cst_node.func()
        for function in functions:
            self.visit_function_node(function)

        statements = cst_node.stmts()
        self.visit_statements_node(statements)

        # cfg allows single stmt
        statement = cst_node.stmt()
        if statement:
            statements.append(self.visit_statement_node(statement))

        return StartNode(functions, statements)

    def visit_statements_node(self, cst_node: AlgoPractiseParser.StmtsContext):
        statements = []
        for stmts in cst_node:
            for statement in stmts.stmt():
                statements.append(self.visit_statement_node(statement))
        return statements

    def visit_statement_node(self, cst_node: AlgoPractiseParser.StmtContext):
        ast_node = None
        if cst_node.dcl():
            ast_node = self.visit_declaration_statement_node(cst_node.dcl())

        elif cst_node.assign_stmt():
            ast_node = self.visit_assignment_statement_node(
                cst_node.assign_stmt())

        elif cst_node.func_call():
            ast_node = self.visit_function_call_statement_node(
                cst_node.func_call())

        elif cst_node.cntrol():
            ast_node = self.visit_control_statement_node(cst_node.cntrol())
        elif cst_node.RETURN() and cst_node.expr():
            ast_node = self.visitReturnStatementNode(cst_node.expr())
        else:
            # return void
            ast_node = self.visitReturnStatementNode(None)

        return ast_node

    def visit_control_statement_node(self, cst_node: AlgoPractiseParser.CntrolContext):
        pass

    def visit_assignment_statement_node(self, cst_node: AlgoPractiseParser.Assign_stmtContext):
        identifier = cst_node.ID().getText()
        expression = self.visit_expression_node(cst_node.expr())
        list_subscript_ctx = cst_node.list_subscript()
        list_subscript = None 
        if list_subscript_ctx:
            list_subscript = self.visit_list_subscript_value_node(identifier,
                                                              list_subscript_ctx)
        return AssignmentStatementNode(identifier, list_subscript, expression)

    def visit_expression_node(self, cst_node: AlgoPractiseParser.ExprContext):
        negation = cst_node.NEG()
        if negation:
            expr = self.visit_expression_node(cst_node.expr(0))
            operator = negation.getText()
            return UnaryExpressionNode(expr, operator)
        val = cst_node.val()
        if val:
            return self.visit_val_node(val)

    def visit_val_node(self, cst_node: AlgoPractiseParser.ValContext):
        identifier = cst_node.ID()
        if identifier:
            identifier=identifier.getText()
        list_subscript = cst_node.list_subscript(0)
        if list_subscript:
            return self.visit_list_subscript_value_node(identifier, list_subscript)
        if identifier:
            return identifier
        numval = cst_node.NUMVAL().getText()
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
            return self.visit_element_list_node(elmnt_list)
        func_call = cst_node.func_call()
        if func_call:
            return self.visit_function_call_expression_node(func_call)
        raise Exception(f"Unknown val node {cst_node.getText()} {cst_node.__class__} {cst_node.__dict__}")

    def visit_element_list_node(self, cst_node: AlgoPractiseParser.Elmnt_listContext):
        elementList = []
        for element in cst_node.expr():
            elementList.append(self.visit_expression_node(element))
        return ElementListNode(elementList)

    def visit_function_call_expression_node(self, cst_node: AlgoPractiseParser.Func_callContext):
        identifier = cst_node.ID().getText()
        arguments = self.visit_element_list_node(cst_node.elmnt_list())

        return FunctionCallExpressionNode(identifier, arguments)

    def visit_list_subscript_value_node(self, identifier, cst_node: AlgoPractiseParser.List_subscriptContext):
        subscripts = []
        for subscript in cst_node.expr():
            subscripts.append(self.visit_expression_node(subscript))
        return ListSubscriptValueNode(identifier, subscripts)

    def visit_block_node(self, cst_node: BlockNode):
        print("qux")

    def visitBooleanNode(self, cst_node: BooleanNode):
        print("quux")

    def visit_declaration_statement_node(self, cst_node: DeclarationStatementNode):
        print("corge")

    def visit_else_statement_node(self, cst_node: ElseStatementNode):
        print("grault")

    def visit_function_call_statement_node(self, cst_node: FunctionCallStatementNode):
        print("waldo")

    def visit_function_node(self, cst_node: FunctionNode):
        print("fred")

    def visit_if_statement_node(self, cst_node: IfStatementNode):
        print("plugh")

    def visitNumberNode(self, cst_node: NumberNode):
        print("thud")

    def visit_parameter_node(self, cst_node: ParameterNode):
        print("thud")

    def visitReturnStatementNode(self, cst_node: ReturnStatementNode):
        print("thud")

    def visitUnaryExpressionNode(self, cst_node: UnaryExpressionNode):
        print("thud")

    def visit_while_statement_node(self, cst_node: WhileStatementNode):
        print("thud")

    def visit_type_node(self, cst_node: TypeNode):
        print("thud")

    def visitStringNode(self, cst_node: StringNode):
        print("thud")

    def visitBinaryExpressionNode(self, cst_node: BinaryExpressionNode):
        print("thud")
