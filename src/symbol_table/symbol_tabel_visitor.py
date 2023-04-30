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
1.
DCL node in ast has non identifier!

2.
It is unclear how variables are handled in the ast. According to the gramma, a value can contain a ID, however no ID node exists. 
In ast, when hitting an id, the cst node is returned as a part of our ast.

Fixed issues:
1. Added identifier to dcl node eved though it has assignment node.
2. 

Status quo: Implement visitGeneralValueNode when id issue in ast has been fixed

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
        if not self.symbol_tabel.current.try_fetch_id(node.identifier) is None:
            # Error, doubble declaration!
            # TODO: (Needs to pass linenumber to new nodes)
            pass

        self.symbol_tabel.insert_in_open_scope(node.identifier, node)
        self.visitAssignmentStatementNode(node.assignment)
    
    def visitAssignmentStatementNode(self, node: nodes.AssignmentStatementNode):
        dcl_node = self.symbol_tabel.traverse(node.identifier)
        if dcl_node is None:
            # Error, not declared!
            raise Exception()
            pass
        
        # Populate assignemnt node with dcl type for later typecheck
        node.dcl_type = dcl_node.type

        if self.is_iterable(node.subscripts.subscripts):
            for subscript_expr in node.subscripts.subscripts:
                self.visitGeneralExprNode(subscript_expr)
        
        self.visitGeneralExprNode(node.expression)
        
    def visitGeneralExprNode(self, node: Any):
        if isinstance(node, nodes.BinaryExpressionNode): self.visitBinaryExpressionNode(node)
        if isinstance(node, nodes.UnaryExpressionNode): self.visitUnaryExpressionNode(node)
        if isinstance(node, nodes.FunctionCallExpressionNode): self.visitFunctionCallExpressionNode(node)

        # TODO: Fix id/var node in ast
        self.visitGeneralValueNode(node)
    
    def visitGeneralValueNode(self, node: Any):
        # Includes; IdNode, ListSubscriptValueNode (....)
        pass
    
    def visitBinaryExpressionNode(self, node: nodes.BinaryExpressionNode):
        self.visitGeneralExprNode(node.left)
        self.visitGeneralExprNode(node.right)
    
    def visitUnaryExpressionNode(self, node: nodes.UnaryExpressionNode):
        self.visitGeneralExprNode(node)
    

    def visitFunctionCallExpressionNode(self, node: nodes.FunctionCallExpressionNode):
        dcl_node = self.symbol_tabel.traverse(node.identifier)
        if dcl_node is None:
            # Error, not declared!
            pass
        
        node.dcl_type = dcl_node._type

        if self.is_iterable(node.arguments):
            for param in node.arguments:
                self.visitGeneralExprNode(param)
        
        self.visitGeneralExprNode(node.expression)


    def visitFunctionNode(self, node: nodes.FunctionNode):
        """This is func dcl, just poor naming"""
        self.symbol_tabel.insert_in_open_scope(node.identifier, node)
        self.symbol_tabel.open_scope()
        # inject params as variables
        for param in node.params:
            self.symbol_tabel.insert_in_open_scope(param.identifier, param)
        # visit block
        self.visitBlockNode(node.block)
        self.symbol_tabel.close_scope()
        