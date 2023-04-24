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
  
        statements = []
        statements_ctx = cst_node.stmt()
        for statement in statements_ctx:
            statements.append(self.visit_statement_node(statement))

        return StartNode(functions, statements)

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
        statements = []
        for statement in cst_node.stmt():
            statements.append(self.visit_statement_node(statement))
        return BlockNode(statements)
        
    def visit_while_statement_node(self, cst_node: AlgoPractiseParser.While_stmtContext):
        return WhileStatementNode(self.visit_expression_node(cst_node.expr()), self.visit_block_node(cst_node.block()))

    # emily
    def visit_declaration_statement_node(self, cst_node: AlgoPractiseParser.DclContext):
        type_node = self.visit_type_node(cst_node.type_())
        if cst_node.ID():
            identifier = cst_node.ID().getText()
            return DeclarationStatementNode(type_node, identifier=identifier)
        # has assignment statement
        assignment_statement_node = self.visit_assignment_statement_node(cst_node.assign_stmt())
        return DeclarationStatementNode(type_node, assignment=assignment_statement_node)
    
    #rasmus
    def visit_else_statement_node(self, cst_node: ElseStatementNode):
        print("grault")
    #moritz
    def visit_function_call_statement_node(self, cst_node: FunctionCallStatementNode):
        print("waldo")
    #matthias
    def visit_function_node(self, cst_node: FunctionNode):
        print("fred")
    #rasmus
    def visit_if_statement_node(self, cst_node: IfStatementNode):
        print("plugh")
        else_node = cst_node.else_stmt()
        if else_node:
            raise Exception("else node not implemented. call moritz")
        return IfStatementNode(self.visit_expression_node(cst_node.expr()), self.visit_block_node(cst_node.block()))
        #return WhileStatementNode(self.visitExpressionNode(cst_node.expr()), self.visitBlockNode(cst_node.block()))
    #matthias
    def visit_parameter_node(self, cst_node: ParameterNode):
        print("thud")
    #moritz
    def visit_return_statement_node(self, cst_node: ReturnStatementNode):
        print("chain")
    #emily
    def visit_unary_expression_node(self, cst_node: AlgoPractiseParser.ValContext):
        print("thud")
    #malthe
    def visit_type_node(self, cst_node: TypeNode):
        print("thud")
    #malthe
    def visit_binary_expression_node(self, cst_node: BinaryExpressionNode):
        print("thud")
