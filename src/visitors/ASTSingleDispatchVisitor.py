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
from nodes.IDNode import IDNode

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
from nodes.master_statement_node import MasterStatementNode


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

        master_statement_cntxs = cst_node.master_statement()

        master_stmt_nodes = []
        for master_statement_ctx in master_statement_cntxs:
            master_stmt_nodes.append(self.visit_master_statement_node(master_statement_ctx))

        return StartNode(cst_node.start.line, master_stmt_nodes)
    
    def visit_master_statement_node(self, cst_ctx: AlgoPractiseParser.Master_statementContext):
        return MasterStatementNode(
            cst_ctx.start.line,
            function_node=None if cst_ctx.func() is None else self.visit_function_node(cst_ctx.func()),
            statement_node=None if cst_ctx.stmt() is None else self.visit_statement_node(cst_ctx.stmt())
        )
    


    def visit_statement_node(self, cst_node: AlgoPractiseParser.StmtContext):
        ast_node = None
        if not cst_node.dcl() is None:
            ast_node = self.visit_declaration_statement_node(cst_node.dcl())

        elif not cst_node.assign_stmt() is None:
            ast_node = self.visit_assignment_statement_node(
                cst_node.assign_stmt())

        elif not cst_node.func_call() is None:
            ast_node = self.visit_function_call_statement_node(
                cst_node.func_call())

        elif not cst_node.cntrol() is None:
            ast_node = self.visit_control_statement_node(cst_node.cntrol())
        elif not cst_node.RETURN() and not cst_node.expr() is None:
            ast_node = self.visit_return_statement_node(expression_ctx=cst_node.expr())
        else:
            # return void
            ast_node = self.visit_return_statement_node(line=cst_node.start.line)

        return ast_node

    def visit_control_statement_node(self, cst_node: AlgoPractiseParser.CntrolContext):
        while_statement_ctx = cst_node.while_stmt()
        if while_statement_ctx:
            return self.visit_while_statement_node(while_statement_ctx)
        if_statement_ctx = cst_node.if_stmt()
        if if_statement_ctx:
            return self.visit_if_statement_node(if_statement_ctx)

    def visit_assignment_statement_node(self, cst_node: AlgoPractiseParser.Assign_stmtContext):
        identifier = IDNode(cst_node.start.line, cst_node.ID().getText())
        expression = self.visit_expression_node(cst_node.expr())
        list_subscript_ctx = cst_node.list_subscript()
        list_subscript = None
        if not list_subscript_ctx is None:
            list_subscript = self.visit_list_subscript_value_node(identifier,
                                                                  list_subscript_ctx)
        return AssignmentStatementNode(cst_node.start.line, identifier, list_subscript, expression)

    def visit_expression_node(self, cst_node: AlgoPractiseParser.ExprContext):
        expression_ctxs = cst_node.expr()
        negation = cst_node.NEG()
        if not negation is None:
            expr = self.visit_expression_node(expression_ctxs[0])
            operator = negation.getText()
            return UnaryExpressionNode(cst_node.start.line, expr, operator)

        val = cst_node.val()
        if not val is None:
            return self.visit_val_node(val)

        if expression_ctxs is not None and len(expression_ctxs) == 2:
            # Binary
            return BinaryExpressionNode(
                cst_node.start.line,
                left=self.visit_expression_node(expression_ctxs[0]),
                right=self.visit_expression_node(expression_ctxs[1]),
                operator=get_operator(cst_node).getText()
            )

        if expression_ctxs is not None and len(expression_ctxs) == 1:
            # (  )
            return self.visit_expression_node(expression_ctxs[0])

    def visit_val_node(self, cst_node: AlgoPractiseParser.ValContext): 
        identifier = cst_node.ID()
        if not identifier is None:
            identifier = IDNode(cst_node.start.line, identifier.getText())
        list_subscript = cst_node.list_subscript() 
        if not list_subscript is None:
            return self.visit_list_subscript_value_node(identifier, list_subscript)
        
        if not identifier is None:
            return IDNode(cst_node.start.line, cst_node.ID().getText())
        
        numval = cst_node.NUMVAL()
        if not numval is None:
            return NumberNode(cst_node.start.line, numval.getText())
        stringval = cst_node.STRINGVAL()
        if not stringval is None:
            return StringNode(cst_node.start.line, stringval)
        true = cst_node.TRUE()
        if not true is None:
            return BooleanNode(cst_node.start.line, true)
        false = cst_node.FALSE()
        if not false is None:
            return BooleanNode(cst_node.start.line, false)
        elmnt_list = cst_node.elmnt_list()
        if not elmnt_list is None:
            return self.visit_element_list_node(elmnt_list)
        func_call = cst_node.func_call()
        if not func_call is None:
            return self.visit_function_call_expression_node(func_call)
        raise Exception(
            f"Unknown val node {cst_node.getText()} {cst_node.__class__} {cst_node.__dict__}")

    def visit_element_list_node(self, cst_node: AlgoPractiseParser.Elmnt_listContext):
        elementList = []
        for element in cst_node.expr():
            elementList.append(self.visit_expression_node(element))
        return ElementListNode(elementList, cst_node.start.line)

    def visit_function_call_expression_node(self, cst_node: AlgoPractiseParser.Func_callContext):
        identifier = IDNode(cst_node.start.line, cst_node.ID().getText())
        arguments = self.visit_element_list_node(cst_node.elmnt_list())
        return FunctionCallExpressionNode(cst_node.start.line, identifier, arguments)

    def visit_list_subscript_value_node(self, identifier, cst_node: AlgoPractiseParser.List_subscriptContext):
        subscripts = []
        for subscript in cst_node.expr():
            subscripts.append(self.visit_expression_node(subscript))
        return ListSubscriptValueNode(cst_node.start.line, identifier, subscripts)

    def visit_block_node(self, cst_node: AlgoPractiseParser.BlockContext):
        statements = []
        if not cst_node.stmt() is None:
            for statement in cst_node.stmt():
                statements.append(self.visit_statement_node(statement))
        return BlockNode(cst_node.start.line, statements)

    def visit_while_statement_node(self, cst_node: AlgoPractiseParser.While_stmtContext):
        return WhileStatementNode(cst_node.start.line, self.visit_expression_node(cst_node.expr()), self.visit_block_node(cst_node.block()))

    def visit_declaration_statement_node(self, cst_node: AlgoPractiseParser.DclContext):
        type_node = self.visit_type_node(cst_node.type_())
        if not cst_node.ID() is None:
            identifier = IDNode(cst_node.start.line, cst_node.ID().getText())
            return DeclarationStatementNode(type_node, cst_node.start.line, identifier=identifier)
        # has assignment statement
        assignment_statement_node = self.visit_assignment_statement_node(
            cst_node.assign_stmt())
        return DeclarationStatementNode(type_node, cst_node.start.line, assignment=assignment_statement_node, identifier=assignment_statement_node.identifier)
    
    def visit_else_statement_node(self, cst_node: AlgoPractiseParser.Else_stmtContext):
        if_ctx = cst_node.if_stmt()
        if not if_ctx is None:
            return ElseStatementNode(cst_node.start.line, if_statement=self.visit_if_statement_node(if_ctx))
        return (ElseStatementNode(cst_node.start.line, block=self.visit_block_node(cst_node.block())))

    def visit_if_statement_node(self, cst_node: AlgoPractiseParser.If_stmtContext):
        if cst_node.else_stmt():
            return IfStatementNode(cst_node.start.line, self.visit_expression_node(cst_node.expr()), self.visit_block_node(cst_node.block()),  self.visit_else_statement_node(cst_node.else_stmt()))
        else:
            return IfStatementNode(cst_node.start.line, self.visit_expression_node(cst_node.expr()), self.visit_block_node(cst_node.block()))

    def visit_function_node(self, cst_node: AlgoPractiseParser.FuncContext):
        func_dcl_ctx = cst_node.func_decl()
        identifier = IDNode(cst_node.start.line, func_dcl_ctx.ID().getText())
        block = self.visit_block_node(func_dcl_ctx.block())
        params_ctx = func_dcl_ctx.params()
        if not params_ctx is None:
            param_nodes = self.visit_parameters_node(params_ctx)
        type_ctx = cst_node.type_()
        if not type_ctx is None:
            type_node = self.visit_type_node(type_ctx)
            return FunctionNode(cst_node.start.line, identifier, block, param_nodes, type_node)
        if not param_nodes is None:
            return FunctionNode(cst_node.start.line, identifier, block, param_nodes, None)
        return FunctionNode(cst_node.start.line, identifier, block)

    def visit_function_call_statement_node(self, cst_node: AlgoPractiseParser.Func_callContext):
        identifier = IDNode(cst_node.start.line, cst_node.ID().getText())
        arguments = self.visit_element_list_node(cst_node.elmnt_list())
        return FunctionCallStatementNode(cst_node.start.line, identifier, arguments)

    def visit_parameter_node(self, cst_node: AlgoPractiseParser.ParamContext):
        _type = self.visit_type_node(cst_node.type_())
        identifier = IDNode(cst_node.start.line, cst_node.ID().getText())
        return ParameterNode(cst_node.start.line, identifier, _type)

    def visit_parameters_node(self, cst_node: AlgoPractiseParser.ParamsContext):
        param_lst_ctx = cst_node.param_lst()
        if not param_lst_ctx:
            return []
        param_ctxs = param_lst_ctx.param()
        param_nodes = []
        for param_ctx in param_ctxs:
            param_nodes.append(self.visit_parameter_node(param_ctx))
        return param_nodes

    def visit_return_statement_node(self, expression_ctx: AlgoPractiseParser.ExprContext = None, line=None):
        """visit_return_statement_node takes an optional expression context and returns a ReturnStatementNode"""
        if not expression_ctx is None:
            return ReturnStatementNode(expression_ctx.start.line, self.visit_expression_node(expression_ctx))
        if not line is None:
            return ReturnStatementNode(line)
        raise Exception("visit_return_statement_node requires either an expression context or a line number")

    def visit_type_node(self, cst_node: AlgoPractiseParser.TypeContext):
        return TypeNode(
            cst_node.start.line,
            type="bool" if cst_node.BOOL_TYPE() else "num" if cst_node.NUM_TYPE() else "string",
            dimensions=len(cst_node.L_BRACKET()
                           ) if not cst_node.L_BRACKET() is None else 0
        )