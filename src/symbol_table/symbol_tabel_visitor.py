import nodes
from symbol_table.stack import Stack
from .abs_symbol_tabel_visitor import AbstractSymbolTableVisitor
from collections.abc import Iterable
from typing import Any

class SymbolTableVisitor(AbstractSymbolTableVisitor):
    def __init__(self) -> None:
        self.symbol_tabel = Stack()

    def startVisitor(self, node: nodes.StartNode):
        self.symbol_tabel.open_scope()
        
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
        
        self.symbol_tabel.close_scope()
    
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
            pass
        
        # Populate assignemnt node with dcl type for later typecheck
        node.dcl_type = dcl_node.type

        if isinstance(node.subscripts, Iterable):
            for subscript_expr in node.subscripts:
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

        if isinstance(node.arguments, Iterable):
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
        