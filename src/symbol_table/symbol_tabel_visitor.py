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
                if isinstance(master_stmt.statement_node, nodes.DeclarationStatementNode):
                    pass
                if isinstance(master_stmt.statement_node, nodes.AssignmentStatementNode):
                    pass
                if isinstance(master_stmt.statement_node, nodes.FunctionCallStatementNode):
                    pass
                if isinstance(master_stmt.statement_node, nodes.WhileStatementNode):
                    pass
                if isinstance(master_stmt.statement_node, nodes.IfStatementNode):
                    pass
                if isinstance(master_stmt.statement_node, nodes.ReturnStatementNode):
                    pass


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
        if isinstance(node.subscripts, Iterable):
            for subscript_expr in node.subscripts:
                self.visitGeneralExprNode(subscript_expr)
        
        self.visitGeneralExprNode(node.expression)
        
    def visitGeneralExprNode(self, node: Any):
        if isinstance(node, nodes.BinaryExpressionNode): self.visitBinaryExpressionNode(node)
        if isinstance(node, nodes.UnaryExpressionNode): self.visitUnaryExpressionNode(node)
        if isinstance(node, nodes.ValueNode): self.visitValueNode(node)
        if isinstance(node, nodes.FunctionCallExpressionNode): self.visitFunctionCallExpressionNode(node)
    
    def visitFunctionNode(self, node: nodes.FunctionNode):
        self.symbol_tabel.insert_in_open_scope(node.identifier, node)
        self.symbol_tabel.open_scope()
        # inject params as variables
        for param in node.params:
            self.symbol_tabel.insert_in_open_scope(param.identifier, param)
        # visit block
        self.visitBlockNode(node.block)
        self.symbol_tabel.close_scope()
        