import nodes

STRING_TYPE = "str"
NUM_TYPE = "num"
BOOL_TYPE = "bool"

class ASTTypeChecker():
    def __init__(self):
        pass

    def visit_start_node(self, node: nodes.StartNode):
        for master_stmt in node.master_statement_nodes:
            if not master_stmt.statement_node is None:
                if isinstance(master_stmt.statement_node, nodes.AssignmentStatementNode):
                    self.visit_assignment(master_stmt.statement_node)
                if isinstance(master_stmt.statement_node, nodes.ReturnStatementNode):
                    self.visit_return(master_stmt.statement_node)
                if isinstance(master_stmt.statement_node, nodes.DeclarationStatementNode):
                    self.visit_declaration(master_stmt.statement_node)
                if isinstance(master_stmt.statement_node, nodes.UnaryExpressionNode):
                    self.visit_unary_expression(master_stmt.statement_node)
                if isinstance(master_stmt.statement_node, nodes.BinaryExpressionNode):
                    self.visit_binary_expression(master_stmt.statement_node)
                if isinstance(master_stmt.statement_node, nodes.ExpressionNode):
                    self.visit_expression(master_stmt.statement_node)
                if isinstance(master_stmt.statement_node, nodes.ListSubscriptValueNode):
                    self.visit_list_subscript(master_stmt.statement_node)

    def visit_expression(self, expr):
        """"returns the type of the expression as a string (str,num,bool)"""
        if isinstance(expr,nodes.ValueNode):
            return self.visit_value_node(expr) 
        if isinstance(expr, nodes.FunctionCallExpressionNode):
            return self.visit_function_call(expr)
        if isinstance(expr, nodes.UnaryExpressionNode):
            return self.visit_unary_expression(expr)
        if isinstance(expr, nodes.BinaryExpressionNode):
            return self.visit_binary_expression(expr)

        raise TypeError(f"Invalid expression node type: {type(expr)}")
    
    def visit_statement(self, stmt):
        if isinstance(stmt, nodes.AssignmentStatementNode):
            return self.visit_assignment(stmt)
        if isinstance(stmt, nodes.ReturnStatementNode):
            return self.visit_return(stmt)
        if isinstance(stmt, nodes.DeclarationStatementNode):
            return self.visit_declaration(stmt)
        
        raise TypeError(f"Invalid statement node type: {type(stmt)}")

    def visit_value_node(self, node):
        """handles ConstantValueNode, IDNode and ListSubscriptValueNode"""
        if isinstance(node, nodes.ConstantValueNode):
            return self.visit_constant_node(node)
        if isinstance(node, nodes.IDNode):
            return self.visit_id_node(node)
        if isinstance(node, nodes.ListSubscriptValueNode):
            return self.visit_list_subscript_value_node(node)
    
    def visit_list_subscript_value_node(self, node):
        pass
            
    def visit_id_node(self,node:nodes.IDNode): 
        return node.dcl_type.type
    
    def visit_constant_node(self, node):
        if isinstance(node, nodes.StringNode):
            return STRING_TYPE
        if isinstance(node, nodes.NumberNode):
            return NUM_TYPE
        if isinstance(node, nodes.BooleanNode):
            return BOOL_TYPE

    def visit_function_call(self, node): 
        pass

    def visit_unary_expression(self, node: nodes.UnaryExpressionNode):
        expr = self.visit_expression(node.expression)
        if (expr) != BOOL_TYPE and node.operator != "!":
            raise TypeError(f"line {node.line_number}: expected bool with '!' operator, got {type(expr)}")
        

    def visit_binary_expression(self, node: nodes.BinaryExpressionNode):
        left_expr = self.visit_expression(node.left)
        right_expr = self.visit_expression(node.right)

        if left_expr != right_expr:
            raise TypeError(f"line {node.line_number}: type mismatch, {type(left_expr)} and {type(right_expr)}")
        if left_expr != NUM_TYPE and node.operator in ["+", "-", "*", "/"]:
            raise TypeError(f"line {node.line_number}: expected num with {node.operator} operator, got {type(left_expr)}")
        if left_expr != BOOL_TYPE and node.operator in ["&&", "||"]:
            raise TypeError(f"line {node.line_number}: expected bool with {node.operator} operator, got {type(left_expr)}")
        if left_expr != STRING_TYPE and node.operator == "+":
            raise TypeError(f"line {node.line_number}: expected str with {node.operator} operator, got {type(left_expr)}")
        if left_expr != BOOL_TYPE and node.operator == "!":
            raise TypeError(f"line {node.line_number}: expected bool with {node.operator} operator, got {type(left_expr)}")
        if left_expr and right_expr != NUM_TYPE and node.operator in ["==", "!="]:
            raise TypeError(f"line {node.line_number}: type mismatch, {type(left_expr)} and {type(right_expr)}")
        if left_expr and right_expr != NUM_TYPE and node.operator in ["<", ">", "<=", ">="]:
            raise TypeError(f"line {node.line_number}: type mismatch, {type(left_expr)} and {type(right_expr)}")
            
            
    def visit_assignment(self, node: nodes.AssignmentStatementNode):
        
        id = self.visit_value_node(node.identifier)

        if not node.expression is None:
            expr = self.visit_expression(node.expression)

            if expr != id:
                raise TypeError(f"line {node.line_number}: type mismatch, {type(expr)} and {type(id)}")
        
        if not node.subscripts is None:
            for sub in node.subscripts:
                expr = self.visit_expression(sub)
                
                if expr != id:
                    raise TypeError(f"line {node.line_number}: type mismatch, {type(expr)} and {type(id)}")

        
    def visit_return(self, node: nodes.ReturnStatementNode):
        pass

    def visit_declaration(self, node: nodes.DeclarationStatementNode):
        pass

    def visit_list_subscript(self, node: nodes.ListSubscriptValueNode):
        pass