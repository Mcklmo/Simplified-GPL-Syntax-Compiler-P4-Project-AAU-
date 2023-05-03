import nodes
from symbol_table.stack import Stack
from .abs_symbol_tabel_visitor import AbstractSymbolTableVisitor
from collections.abc import Iterable
from typing import Any

"""
OBS: 

These visitors should be implemented with the objective to verify that the input prigram contains no scope violations.
While during that, it should populate out ast nodes with types, making typechecking possible afterwards.

When entering a block, a new scope should be opened in the symbol table. Make sure to always close opend scopes in the SAME visitor it was opned in.

ETC - We found an assignment node:
1: use traverse tro find corrosponding dcl
2: If no dcl exists, raise error (To be implemented)
3: Populate the assignemt node with the type of the dcl.

!!Current issue!!
The valueListSubscript node is redundant (right?)

Fixed issues:
1. Added identifier to dcl node eved though it has assignment node.

2.
It is unclear how variables are handled in the ast. According to the gramma, a value can contain a ID, however no ID node exists. 
In ast, when hitting an id, the cst node is returned as a part of our ast. - Emily


"""

#class SymbolTableVisitor():
class SymbolTableVisitor(AbstractSymbolTableVisitor):
    def __init__(self) -> None:
        self.symbol_tabel = Stack()
    
    @staticmethod
    def is_iterable(obj):
        try:
            iterator = iter(obj)
        except TypeError:
            # not iterable
            return False
        else:
            # iterable
            return True

    def startVisitor(self, node: nodes.StartNode):
        
        for master_stmt in node.master_statement_nodes:
            if not master_stmt.statement_node is None:
                if isinstance(master_stmt.statement_node, nodes.DeclarationStatementNode): self.visitDeclarationStatementNode(master_stmt.statement_node)
                if isinstance(master_stmt.statement_node, nodes.AssignmentStatementNode): self.visitAssignmentStatementNode(master_stmt.statement_node)
                if isinstance(master_stmt.statement_node, nodes.FunctionCallStatementNode): self.visitFunctionCallStatementNode(master_stmt.statement_node)
                if isinstance(master_stmt.statement_node, nodes.WhileStatementNode): self.visitWhileStatementNode(master_stmt.statement_node)
                if isinstance(master_stmt.statement_node, nodes.IfStatementNode): self.visitIfStatementNode(master_stmt.statement_node)
                if isinstance(master_stmt.statement_node, nodes.ReturnStatementNode): self.visitReturnStatementNode(master_stmt.statement_node)


            elif not master_stmt.function_node is None:
                self.visitFunctionNode(master_stmt.function_node)
            
            else:
                print("Stop coding, you are tired!")
        
    
    def visitDeclarationStatementNode(self, node: nodes.DeclarationStatementNode):
        if not self.symbol_tabel.current.try_fetch_id(node.identifier.identifier) is None:
            # Error, doubble declaration!
            # TODO: (Needs to pass linenumber to new nodes)
            pass

        self.symbol_tabel.insert_in_open_scope(node.identifier.identifier, node)
        self.visitAssignmentStatementNode(node.assignment)
    
    def visitAssignmentStatementNode(self, node: nodes.AssignmentStatementNode):
        dcl_node = self.symbol_tabel.traverse(node.identifier.identifier)
        if dcl_node is None:
            # Error, not declared!
            raise Exception()
            pass
        
        # Populate assignemnt node with dcl type for later typecheck
        node.dcl_type = dcl_node.type

        # The subscript node is redundant. It should be a list (As it does not make sence to make an empty subscript node as default value for assignemnts without subscrips.)
        # The none check i s just a workaround
        if not node.subscripts is None and self.is_iterable(node.subscripts.subscripts):
            for subscript_expr in node.subscripts.subscripts:
                self.visitGeneralExprNode(subscript_expr)
        
        self.visitGeneralExprNode(node.expression)
        
    def visitGeneralExprNode(self, node: Any):
        if isinstance(node, nodes.BinaryExpressionNode): self.visitBinaryExpressionNode(node)
        if isinstance(node, nodes.UnaryExpressionNode): self.visitUnaryExpressionNode(node)
        if isinstance(node, nodes.FunctionCallExpressionNode): self.visitFunctionCallExpressionAndStatementNode(node)

        self.visitGeneralValueNode(node)
    
    def visitGeneralValueNode(self, node: Any):
        if isinstance(node, nodes.NumberNode): pass
        if isinstance(node, nodes.StringNode): pass
        if isinstance(node, nodes.BooleanNode): pass
        if isinstance(node, nodes.IDNode): self.visitIDNode(node)
        if isinstance(node, nodes.FunctionCallExpressionNode): self.visitFunctionCallExpressionAndStatementNode(node)
        if isinstance(node, nodes.ElementListNode): 
            for expr in node.expressions:
                self.visitGeneralExprNode(expr)

        if isinstance(node, nodes.ListSubscriptValueNode): 
            self.visitIDNode(node.identifier.identifier)
            for sub_expr in node.subscripts:
                self.visitGeneralExprNode(sub_expr)

    def visitIDNode(self, node: nodes.IDNode):
        dcl_node = self.symbol_tabel.traverse(node.identifier)
        if dcl_node is None:
            i = 0
            # Err not declared!!
            pass
    
        else:
            node.dcl_type = dcl_node.type

    def visitBinaryExpressionNode(self, node: nodes.BinaryExpressionNode):
        self.visitGeneralExprNode(node.left)
        self.visitGeneralExprNode(node.right)
    
    def visitUnaryExpressionNode(self, node: nodes.UnaryExpressionNode):
        self.visitGeneralExprNode(node)
    

    def visitFunctionCallExpressionAndStatementNode(self, node: Any): #FunctionCallExpOrStmt
        dcl_node = self.symbol_tabel.traverse(node.identifier.identifier)
        if dcl_node is None:
            # Error, not declared!
            pass
        
        node.dcl_type = dcl_node._type

        if self.is_iterable(node.arguments):
            for param in node.arguments:
                self.visitGeneralExprNode(param)


    def visitFunctionNode(self, node: nodes.FunctionNode):
        """This is func dcl, just poor naming"""
        self.symbol_tabel.insert_in_open_scope(node.identifier.identifier, node)
        
        self.symbol_tabel.open_scope()
        # inject params as variables
        for param in node.params:
            self.symbol_tabel.insert_in_open_scope(param.identifier.identifier, param)
        # visit block
        self.visitBlockNode(node.block)
        self.symbol_tabel.close_scope()

    def visitBlockNode(self, node: nodes.BlockNode):
        # Inserting statements from block
        for statement_node in node.statements_nodes:
            if type(statement_node) is nodes.IfStatementNode:
                self.visitIfStatementNode(statement_node)
            elif type(statement_node) is nodes.WhileStatementNode:
                self.visitWhileStatementNode(statement_node)
            elif type(statement_node) is nodes.FunctionCallStatementNode: 
                self.visitFunctionCallExpressionAndStatementNode(statement_node)
            elif type(statement_node) is nodes.AssignmentStatementNode:
                self.visitAssignmentStatementNode(statement_node)
            elif type(statement_node) is nodes.ReturnStatementNode:
                self.visitReturnStatementNode(statement_node)
            elif type(statement_node) is nodes.DeclarationStatementNode:
                self.visitDeclarationStatementNode(statement_node)

    def visitIfStatementNode(self, node: nodes.IfStatementNode):
        self.symbol_tabel.open_scope()
        self.visitBlockNode(node.block)
        self.symbol_tabel.close_scope()
        
        if not node.else_node is None:
            self.visitElseStatementNode(node.else_node)

    def visitWhileStatementNode(self, node: nodes.WhileStatementNode):
        self.symbol_tabel.open_scope()
        self.visitBlockNode(node.block)
        self.symbol_tabel.close_scope()

    def visitElseStatementNode(self, node: nodes.ElseStatementNode):
        if not node.if_statement is None:
            self.visitIfStatementNode(node.if_statement)
        else:
            self.symbol_tabel.open_scope()
            self.visitBlockNode(node.block)
            self.symbol_tabel.close_scope()

    def visitReturnStatementNode(self, node: nodes.ReturnStatementNode):
        self.visitGeneralExprNode(node.expression)
