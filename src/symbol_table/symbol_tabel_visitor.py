import nodes
from typing import Any
from .utils import SymbolTableUtils
from pre_defined_functions.pre_defined_functions import pre_defined_functions,pre_defined_function_ids

"""
OBS: 

These visitors should be implemented with the objective to verify that the input prigram contains no scope violations.
While during that, it should populate out ast nodes with types, making typechecking possible afterwards.

When entering a block, a new scope should be opened in the symbol table. Make sure to always close opend scopes in the SAME visitor it was opned in.

ETC - We found an assignment node:
1: use traverse tro find corrosponding dcl
2: If no dcl exists, raise error (To be implemented)
3: Populate the assignemt node with the type of the dcl.


todo 5.5.23:
- tilføj expected_return_type til ReturnStatementNode
- tilføj felt til symbol table klasse der holder typen af en funktion
- når en func decl findes, settes feltet i klassen. 
- når en ny blok åbnes, sætter vi feltet til den nuværende. sådan er der altid den aktuelle retur type i det åbne scope indenfor
  en functions deklarations block.
- når der mødes et retur statement henter vi typen fra klassen g tilføjer den til return noden


"""


class SymbolTableVisitor(SymbolTableUtils):
    def __init__(self) -> None:
        super().__init__()
    
    def do_visit(self, start_node:nodes.StartNode):
        # inject pre defined functions in symbol table. These are used to decorate function call nodes with correct input and output types
        for fn in pre_defined_functions:
            function_node = nodes.FunctionNode(0,fn.identifier,nodes.BlockNode(0),fn.params,fn.return_type)
            self.visitFunctionNode(function_node, True)
            
        self.visitStartNode(start_node)

        if len(self.errors) == 0:
            return []
        return self.errors

    def visitStartNode(self, node: nodes.StartNode):
        for master_stmt in node.master_statement_nodes:
            if not master_stmt.statement_node is None:
                if isinstance(master_stmt.statement_node, nodes.DeclarationStatementNode):
                    master_stmt.statement_node.is_global = True
                    self.visitDeclarationStatementNode(
                        master_stmt.statement_node)
                if isinstance(master_stmt.statement_node, nodes.AssignmentStatementNode):
                    self.visitAssignmentStatementNode(
                        master_stmt.statement_node)
                if isinstance(master_stmt.statement_node, nodes.FunctionCallStatementNode):
                    self.visitFunctionCallExpressionAndStatementNode(
                        master_stmt.statement_node)
                if isinstance(master_stmt.statement_node, nodes.ControlStatementNode):
                    self.visit_control_statement_node(master_stmt.statement_node)
                if isinstance(master_stmt.statement_node, nodes.ReturnStatementNode):
                    self.regsiter_err("Return statement outside function!",
                                      master_stmt.statement_node.line_number)
                    self.visitReturnStatementNode(master_stmt.statement_node)

            elif not master_stmt.function_node is None:
                self.visitFunctionNode(master_stmt.function_node)

            else:
                raise Exception("Stop coding, you are tired!")
    def visit_control_statement_node(self, node:nodes.ControlStatementNode):
        if isinstance(node, nodes.WhileStatementNode):
            self.visitWhileStatementNode(node)
        if isinstance(node, nodes.IfStatementNode):
            self.visitIfStatementNode(node)

    def visitDeclarationStatementNode(self, node: nodes.DeclarationStatementNode):
        if not self.symbol_tabel.current.try_fetch_id(node.identifier.identifier) is None:
            self.regsiter_err(
                f"id {node.identifier.identifier} has been declared more than once!", node.line_number)
            return

        # If no err, insert in scope
        self.symbol_tabel.insert_in_open_scope(
            node.identifier.identifier, node)

        if not node.assignment is None:
            self.visitAssignmentStatementNode(node.assignment)

    def visitAssignmentStatementNode(self, node: nodes.AssignmentStatementNode):
        dcl_node = self.symbol_tabel.traverse(node.identifier.identifier)
        if dcl_node is None:
            # Error, not declared!
            self.regsiter_err(
                f"var {node.identifier.identifier} was never declared!", node.line_number)
            return

        # Populate assignemnt node with dcl type for later typecheck
        node.dcl_type = dcl_node.type
        # also populate IDNode with same thing
        node.identifier.dcl_type = dcl_node.type

        # The subscript node is redundant. It should be a list (As it does not make sence to make an empty subscript node as default value for assignemnts without subscrips.)
        # The none check i s just a workaround
        if not node.subscripts is None and self.is_iterable(node.subscripts.subscripts):
            for subscript_expr in node.subscripts.subscripts:
                self.visitGeneralExprNode(subscript_expr)

        self.visitGeneralExprNode(node.expression)

    def visitGeneralExprNode(self, node: Any):
        if isinstance(node, nodes.BinaryExpressionNode):
            self.visitBinaryExpressionNode(node)
        if isinstance(node, nodes.UnaryExpressionNode):
            self.visitUnaryExpressionNode(node)
        if isinstance(node, nodes.FunctionCallExpressionNode):
            self.visitFunctionCallExpressionAndStatementNode(node)

        self.visitGeneralValueNode(node)

    def visitGeneralValueNode(self, node: Any):
        if isinstance(node, nodes.NumberNode):
            node.type_node = nodes.TypeNode(node.line_number, "num", 0)
        if isinstance(node, nodes.StringNode):
            node.type_node = nodes.TypeNode(node.line_number, "string", 0)
        if isinstance(node, nodes.BooleanNode):
            node.type_node = nodes.TypeNode(node.line_number, "bool", 0)
        if isinstance(node, nodes.IDNode):
            self.visitIDNode(node)
        if isinstance(node, nodes.FunctionCallExpressionNode):
            self.visitFunctionCallExpressionAndStatementNode(node)
        if isinstance(node, nodes.ElementListNode):
            for expr in node.expressions:
                self.visitGeneralExprNode(expr)

        if isinstance(node, nodes.ListSubscriptValueNode):
            self.visitListSubscript(node)

    def visitListSubscript(self, node: nodes.ListSubscriptValueNode):
        self.visitIDNode(node.identifier)
        for sub_expr in node.subscripts:
            self.visitGeneralExprNode(sub_expr)

    def visitIDNode(self, node: nodes.IDNode):
        dcl_node = self.symbol_tabel.traverse(node.identifier)
        if dcl_node is None:
            self.regsiter_err(
                f"var {node.identifier} was never declared!", node.line_number)

        else:
            node.dcl_type = dcl_node.type
            node.dcl_dimensions = dcl_node.type.dimensions

    def visitBinaryExpressionNode(self, node: nodes.BinaryExpressionNode):
        self.visitGeneralExprNode(node.left)
        self.visitGeneralExprNode(node.right)

    def visitUnaryExpressionNode(self, node: nodes.UnaryExpressionNode):
        self.visitGeneralExprNode(node.expression)

    # FunctionCallExpOrStmt
    def visitFunctionCallExpressionAndStatementNode(self, node: Any):
        dcl_node = self.symbol_tabel.traverse(node.identifier.identifier)
        if dcl_node is None:
            self.regsiter_err(
                f"function {node.identifier.identifier} is called but never declared!", node.line_number)
            # Error, not declared!
            return

        node.dcl_node = dcl_node
        node.dcl_type = dcl_node.type

        if self.is_iterable(node.arguments):
            for param in node.arguments:
                self.visitGeneralExprNode(param)

    def visitFunctionNode(self, node: nodes.FunctionNode,is_pre_defined=False):
        """This is func dcl, just poor naming"""
        if not self.symbol_tabel.current.try_fetch_id(node.identifier.identifier) is None:
            if node.identifier.identifier in pre_defined_function_ids:
                self.regsiter_err(f"cannot define a function with the same name as a pre defined function ({node.identifier.identifier})", node.line_number)
                return 
            self.regsiter_err(
                f"id {node.identifier.identifier} has been declared more than once!", node.line_number)
            return
        self.symbol_tabel.insert_in_open_scope(
            node.identifier.identifier, node)

        self.symbol_tabel.open_scope()
        # inject params as variables
        for param in node.params:
            self.symbol_tabel.insert_in_open_scope(
                param.identifier.identifier, nodes.DeclarationStatementNode(type=param._type, line_number=param.line_number, identifier=param.identifier))

        # set expected return type
        self.symbol_tabel.current.expected_return_type = node.type

        # ignore block if pre defined
        if not is_pre_defined:
        # visit block
            returns = self.visitBlockNode(node.block)
            return_void = node.type.type == "void"
            if not return_void and not returns:
                self.regsiter_err(
                    f"Some paths in function {node.identifier.identifier} are missing return statements!", node.line_number)
            elif return_void and returns:
                self.regsiter_err(
                    f"Function {node.identifier.identifier} returns a value but is declared void!", node.line_number)
        
        self.symbol_tabel.close_scope()

    def visitBlockNode(self, node: nodes.BlockNode):
        """returns true if all paths (including all nested if else statements) have a return statement"""
        returns = False
        # Inserting statements from block
        for statement_node in node.statements_nodes:
            if type(statement_node) is nodes.IfStatementNode:
                returns = self.visitIfStatementNode(
                    statement_node)
            elif type(statement_node) is nodes.WhileStatementNode:
                self.visitWhileStatementNode(statement_node)
            elif type(statement_node) is nodes.FunctionCallStatementNode:
                self.visitFunctionCallExpressionAndStatementNode(
                    statement_node)
            elif type(statement_node) is nodes.AssignmentStatementNode:
                self.visitAssignmentStatementNode(statement_node)
            elif type(statement_node) is nodes.ReturnStatementNode:
                returns = True
                self.visitReturnStatementNode(statement_node)
            elif type(statement_node) is nodes.DeclarationStatementNode:
                self.visitDeclarationStatementNode(statement_node)

        return returns

    def visitIfStatementNode(self, node: nodes.IfStatementNode):
        """return true if the if statement has an else statement and both the if and else statements have a return statement"""
        self.visitGeneralExprNode(node.condition)
        expected_return_type = self.symbol_tabel.current.expected_return_type
        self.symbol_tabel.open_scope()
        self.symbol_tabel.current.expected_return_type = expected_return_type
        if_returning = self.visitBlockNode(node.block)
        self.symbol_tabel.close_scope()
        else_returning = False
        if not node.else_node is None:
            else_returning = self.visitElseStatementNode(node.else_node)
        return if_returning and else_returning

    def visitWhileStatementNode(self, node: nodes.WhileStatementNode):
        self.visitGeneralExprNode(node.condition)
        expected_return_type = self.symbol_tabel.current.expected_return_type

        self.symbol_tabel.open_scope()
        self.symbol_tabel.current.expected_return_type = expected_return_type

        self.visitBlockNode(node.block)
        self.symbol_tabel.close_scope()

    def visitElseStatementNode(self, node: nodes.ElseStatementNode):
        if not node.if_statement is None:
            return self.visitIfStatementNode(node.if_statement)
        expected_return_type = self.symbol_tabel.current.expected_return_type

        self.symbol_tabel.open_scope()
        self.symbol_tabel.current.expected_return_type = expected_return_type

        else_returning = self.visitBlockNode(node.block)
        self.symbol_tabel.close_scope()
        return else_returning

    def visitReturnStatementNode(self, node: nodes.ReturnStatementNode):
        node.expected_return_type = self.symbol_tabel.current.expected_return_type
        self.visitGeneralExprNode(node.expression)
