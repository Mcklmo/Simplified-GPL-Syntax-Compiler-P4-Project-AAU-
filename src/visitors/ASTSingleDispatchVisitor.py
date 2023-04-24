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

from antlr4 import ParserRuleContext

from abstract_syntax.ExpressionNode import ExpressionNode
from abstract_syntax.ValueNode import ValueNode
from abstract_syntax.StatementNode import StatementNode

def get_operator(cst_node: ParserRuleContext):
    terminal_types = ["OR", "AND", "EQUAL", "NE", "LTE", "GTE", "GT", "LT", "PLUS", "MINUS", "MULT", "DIV", "MOD"]
    for t in terminal_types:
        if t in dir(cst_node):
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
        negation = cst_node.NEG()
        expressions = cst_node.expr()
        if negation:
            expr = self.visit_expression_node(expressions[0])
            operator = negation.getText()
            return UnaryExpressionNode(expr, operator)
        

        val = cst_node.val()
        if val:
            return self.visit_val_node(val)
        
        if expressions is not None and len(expressions) == 2:
            # Binary
            return BinaryExpressionNode(
                left=expressions[0],
                right=expressions[1],
                operator=get_operator(cst_node).getText()
            )
        
        if expressions is not None and len(expressions) == 1:
            # (  )
            return self.visit_expression_node(expressions[0])
        



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

    def visit_block_node(self, cst_node: BlockNode):
        statements = []
        for statement in cst_node.stmt():
            statements.append(self.visit_statement_node(statement))
        return BlockNode(statements)

    def visit_while_statement_node(self, cst_node: AlgoPractiseParser.While_stmtContext):
        return WhileStatementNode(self.visit_expression_node(cst_node.expr()), self.visit_block_node(cst_node.block()))

    # emily
    def visit_declaration_statement_node(self, cst_node: AlgoPractiseParser.DclContext):
        print("corge")
    # rasmus

    def visit_else_statement_node(self, cst_node: ElseStatementNode):
        print("grault")
    #matthias
    def visit_function_node(self, cst_node: AlgoPractiseParser.FuncContext):
        func_dcl_ctx = cst_node.func_decl()
        identifier = func_dcl_ctx.ID().getText()
        block = self.visit_block_node(func_dcl_ctx.block())
        params = self.visit_parameters_node(func_dcl_ctx.params())
        type_ctx = cst_node.type_()
        if type_ctx:
            type_node = self.visit_type_node(type_ctx)
            return FunctionNode(identifier, params, block, type_node)

        return FunctionNode(identifier, params, block)
    #rasmus
    # moritz

    def visit_function_call_statement_node(self, cst_node: AlgoPractiseParser.Func_callContext):
        identifier = cst_node.ID().getText()
        arguments = self.visit_element_list_node(cst_node.elmnt_list())
        return FunctionCallStatementNode(identifier, arguments)
    # rasmus

    def visit_if_statement_node(self, cst_node: IfStatementNode):
        print("plugh")
        else_node = cst_node.else_stmt()
        if else_node:
            raise Exception("else node not implemented. call moritz")
        return IfStatementNode(self.visit_expression_node(cst_node.expr()), self.visit_block_node(cst_node.block()))
        #return WhileStatementNode(self.visitExpressionNode(cst_node.expr()), self.visitBlockNode(cst_node.block()))
    #matthias
    def visit_parameter_node(self, cst_node: AlgoPractiseParser.ParamContext):
        _type = self.visit_type_node(cst_node.type_())
        identifier = cst_node.ID().getText()
        return ParameterNode(identifier, _type)
    #matthias
    def visit_parameters_node(self, cst_node: AlgoPractiseParser.ParamsContext):
        param_ctxs = cst_node.param_lst().param()
        param_nodes = []
        for param_ctx in param_ctxs:
            param_nodes.append(self.visit_parameter_node(param_ctx))
        return param_nodes

    #emily
        # return WhileStatementNode(self.visitExpressionNode(cst_node.expr()), self.visitBlockNode(cst_node.block()))
    # moritz

    def visit_return_statement_node(self, cst_node: AlgoPractiseParser.ExprContext = None):
        """visit_return_statement_node takes an optional expression context and returns a ReturnStatementNode"""
        if cst_node:
            return ReturnStatementNode(self.visit_expression_node(cst_node))
        return ReturnStatementNode()
    # emily

    def visit_unary_expression_node(self, cst_node: UnaryExpressionNode):
        print("thud")
    
    #malthe
    def visit_type_node(self, cst_node: AlgoPractiseParser.TypeContext):
        return TypeNode(
            type="bool" if cst_node.BOOL_TYPE() else "num" if cst_node.NUM_TYPE() else "string",
            dimensions=len(cst_node.L_BRACKET()) if not cst_node.L_BRACKET() is None else 0
        )
