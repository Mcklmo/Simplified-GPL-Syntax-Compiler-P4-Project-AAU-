from _parser.AlgoPractiseParser import AlgoPractiseParser
from nodes.ElementListNode import ElementListNode

from .SingleDispatchVisitor import SingleDispatchVisitor
from nodes.StartNode import StartNode
from nodes.AssignmentStatementNode import AssignmentStatementNode
from nodes.BlockNode import BlockNode
from nodes.DeclarationStatementNode import DeclarationStatementNode
from nodes.ElseStatementNode import ElseStatementNode
from nodes.FunctionCallStatementNode import FunctionCallStatementNode
from nodes.FunctionNode import FunctionNode
from nodes.IfStatementNode import IfStatementNode
from nodes.ListSubscriptValueNode import ListSubscriptValueNode
from nodes.ParameterNode import ParameterNode
from nodes.WhileStatementNode import WhileStatementNode
from nodes.TypeNode import TypeNode

from nodes.FunctionCallExpressionNode import FunctionCallExpressionNode
from nodes.ReturnStatementNode import ReturnStatementNode
from nodes.UnaryExpressionNode import UnaryExpressionNode
from nodes.BinaryExpressionNode import BinaryExpressionNode
from nodes.BooleanNode import BooleanNode
from nodes.NumberNode import NumberNode
from nodes.StringNode import StringNode

from antlr4 import ParserRuleContext

from nodes.ExpressionNode import ExpressionNode
from nodes.ValueNode import ValueNode
from nodes.StatementNode import StatementNode


def get_operator(cst_node: ParserRuleContext):
    terminal_types = ["OR", "AND", "EQUAL", "NE", "LTE",
                      "GTE", "GT", "LT", "PLUS", "MINUS", "MULT", "DIV", "MOD"]
    for t in terminal_types:
        if t in dir(cst_node) and not getattr(cst_node, t)() is None:
            return getattr(cst_node, t)()
    return None


class ASTSingleDispatchVisitor(SingleDispatchVisitor):
    def __init__(self):
        pass

    def visit_start_node(self, cst_node: AlgoPractiseParser.StartContext):

        functions_ctxs = cst_node.func()
        function_nodes = []
        for function_ctx in functions_ctxs:
            function_nodes.append(self.visit_function_node(function_ctx))

        statement_nodes = []
        statements_ctxs = cst_node.stmt()
        for statement_ctx in statements_ctxs:
            statement_nodes.append(self.visit_statement_node(statement_ctx))

        return StartNode(function_nodes, statement_nodes)

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
            ast_node = self.visit_return_statement_node(cst_node.expr())
        else:
            # return void
            ast_node = self.visit_return_statement_node(None)

        return ast_node

    def visit_control_statement_node(self, cst_node: AlgoPractiseParser.CntrolContext):
        while_statement_ctx = cst_node.while_stmt()
        if while_statement_ctx:
            return self.visit_while_statement_node(while_statement_ctx)
        if_statement_ctx = cst_node.if_stmt()
        if if_statement_ctx:
            return self.visit_if_statement_node(if_statement_ctx)

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
        expression_ctxs = cst_node.expr()
        negation = cst_node.NEG()
        if negation:
            expr = self.visit_expression_node(expression_ctxs[0])
            operator = negation.getText()
            return UnaryExpressionNode(expr, operator)

        val = cst_node.val()
        if val:
            return self.visit_val_node(val)

        if expression_ctxs is not None and len(expression_ctxs) == 2:
            # Binary
            return BinaryExpressionNode(
                left=self.visit_expression_node(expression_ctxs[0]),
                right=self.visit_expression_node(expression_ctxs[1]),
                operator=get_operator(cst_node).getText()
            )

        if expression_ctxs is not None and len(expression_ctxs) == 1:
            # (  )
            return self.visit_expression_node(expression_ctxs[0])

    def visit_val_node(self, cst_node: AlgoPractiseParser.ValContext):
        identifier = cst_node.ID()
        if identifier:
            identifier = identifier.getText()
        list_subscript = cst_node.list_subscript(0)
        if list_subscript:
            return self.visit_list_subscript_value_node(identifier, list_subscript)
        if identifier:
            return identifier
        numval = cst_node.NUMVAL()
        if numval:
            return NumberNode(numval.getText())
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
        raise Exception(
            f"Unknown val node {cst_node.getText()} {cst_node.__class__} {cst_node.__dict__}")

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

    def visit_block_node(self, cst_node: AlgoPractiseParser.BlockContext):
        statements = []
        if cst_node.stmt():
            for statement in cst_node.stmt():
                statements.append(self.visit_statement_node(statement))
        return BlockNode(statements)

    def visit_while_statement_node(self, cst_node: AlgoPractiseParser.While_stmtContext):
        return WhileStatementNode(self.visit_expression_node(cst_node.expr()), self.visit_block_node(cst_node.block()))

    def visit_declaration_statement_node(self, cst_node: AlgoPractiseParser.DclContext):
        type_node = self.visit_type_node(cst_node.type_())
        if cst_node.ID():
            identifier = cst_node.ID().getText()
            return DeclarationStatementNode(type_node, identifier=identifier)
        # has assignment statement
        assignment_statement_node = self.visit_assignment_statement_node(
            cst_node.assign_stmt())
        return DeclarationStatementNode(type_node, assignment=assignment_statement_node)
    
    def visit_else_statement_node(self, cst_node: AlgoPractiseParser.Else_stmtContext):
        if_ctx = cst_node.if_stmt()
        if if_ctx:
            return ElseStatementNode(if_statement=self.visit_if_statement_node(if_ctx))
        return (ElseStatementNode(block=self.visit_block_node(cst_node.block())))

    def visit_if_statement_node(self, cst_node: AlgoPractiseParser.If_stmtContext):
        if cst_node.else_stmt():
            return IfStatementNode(self.visit_expression_node(cst_node.expr()), self.visit_block_node(cst_node.block()),  self.visit_else_statement_node(cst_node.else_stmt()))
        else:
            return IfStatementNode(self.visit_expression_node(cst_node.expr()), self.visit_block_node(cst_node.block()))

    def visit_function_node(self, cst_node: AlgoPractiseParser.FuncContext):
        func_dcl_ctx = cst_node.func_decl()
        identifier = func_dcl_ctx.ID().getText()
        block = self.visit_block_node(func_dcl_ctx.block())
        params_ctx = func_dcl_ctx.params()
        if params_ctx:
            param_nodes = self.visit_parameters_node(params_ctx)
        type_ctx = cst_node.type_()
        if type_ctx:
            type_node = self.visit_type_node(type_ctx)
            return FunctionNode(identifier, block, param_nodes,  type_node)
        if param_nodes:
            return FunctionNode(identifier, block, param_nodes)
        return FunctionNode(identifier, block)

    def visit_function_call_statement_node(self, cst_node: AlgoPractiseParser.Func_callContext):
        identifier = cst_node.ID().getText()
        arguments = self.visit_element_list_node(cst_node.elmnt_list())
        return FunctionCallStatementNode(identifier, arguments)

    def visit_parameter_node(self, cst_node: AlgoPractiseParser.ParamContext):
        _type = self.visit_type_node(cst_node.type_())
        identifier = cst_node.ID().getText()
        return ParameterNode(identifier, _type)

    def visit_parameters_node(self, cst_node: AlgoPractiseParser.ParamsContext):
        param_lst_ctx = cst_node.param_lst()
        if not param_lst_ctx:
            return []
        param_ctxs = param_lst_ctx.param()
        param_nodes = []
        for param_ctx in param_ctxs:
            param_nodes.append(self.visit_parameter_node(param_ctx))
        return param_nodes

    def visit_return_statement_node(self, cst_node: AlgoPractiseParser.ExprContext = None):
        """visit_return_statement_node takes an optional expression context and returns a ReturnStatementNode"""
        if cst_node:
            return ReturnStatementNode(self.visit_expression_node(cst_node))
        return ReturnStatementNode()

    def visit_type_node(self, cst_node: AlgoPractiseParser.TypeContext):
        return TypeNode(
            type="bool" if cst_node.BOOL_TYPE() else "num" if cst_node.NUM_TYPE() else "string",
            dimensions=len(cst_node.L_BRACKET()
                           ) if not cst_node.L_BRACKET() is None else 0
        )
