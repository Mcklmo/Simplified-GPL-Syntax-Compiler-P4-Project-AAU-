import nodes
from TypeCheckVisitors.type_check_utils import TypeCheckUtils

"""
note 1: A decision has been made: In the case where the expresison could not be evaluated, we only shows the error regarding the expression valuation . 
Not the "type is not bool
"""

STRING_TYPE = "string"
NUM_TYPE = "num"
BOOL_TYPE = "bool"


class ASTTypeChecker(TypeCheckUtils):
    def __init__(self) -> None:
        super().__init__()

    def do_visit(self, start_node: nodes.StartNode):
        """returns produced errors or None"""
        self.visit_start_node(start_node)

        if len(self.errors) == 0:
            return []
        return self.errors

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
                if isinstance(master_stmt.statement_node, nodes.ControlStatementNode):
                    self.visit_control_statement(master_stmt.statement_node)
                if isinstance(master_stmt.statement_node, nodes.BlockNode):
                    self.visit_block_node(master_stmt.statement_node)
                if isinstance(master_stmt.statement_node, nodes.FunctionCallStatementNode):
                    self.visit_function_call(master_stmt.statement_node)

            if not master_stmt.function_node is None:
                self.visit_function_declaration(master_stmt.function_node)

    def visit_expression(self, expr,expected_type=None):
        """"returns a typenode."""
        if isinstance(expr, nodes.ValueNode):
            return self.visit_value_node(expr)
        if isinstance(expr, nodes.FunctionCallExpressionNode):
            return self.visit_function_call(expr)
        if isinstance(expr, nodes.UnaryExpressionNode):
            return self.visit_unary_expression(expr)
        if isinstance(expr, nodes.BinaryExpressionNode):
            return self.visit_binary_expression(expr)
        if isinstance(expr, nodes.ElementListNode):
            return self.visit_element_list_node(expr,expected_type)

    def visit_block_node(self, node: nodes.BlockNode):
        for statement in node.statements_nodes:
            if isinstance(statement, nodes.ControlStatementNode):
                self.visit_control_statement(statement)
            if isinstance(statement, nodes.StatementsNode):
                self.visit_statement(statement)
            if isinstance(statement, nodes.FunctionCallExpressionNode):
                self.visit_expression(statement)

    def visit_control_statement(self, node: nodes.ControlStatementNode):
        if isinstance(node, nodes.WhileStatementNode) or isinstance(node, nodes.IfStatementNode):
            expr_type = self.visit_expression(node.condition)
            # See note 1
            if not expr_type is None and expr_type.type != BOOL_TYPE:
                self.register_err(
                    f"Condition in if-statement on line number: {node.line_number}, expected boolean value")

            self.visit_block_node(node.block)

        if isinstance(node, nodes.ElseStatementNode):
            if not node.if_statement is None:
                self.visit_control_statement(node.if_statement)
        else:
            self.visit_block_node(node.block)

    def visit_statement(self, stmt):
        if isinstance(stmt, nodes.AssignmentStatementNode):
            return self.visit_assignment(stmt)
        if isinstance(stmt, nodes.ReturnStatementNode):
            return self.visit_return(stmt)
        if isinstance(stmt, nodes.DeclarationStatementNode):
            return self.visit_declaration(stmt)

        self.register_err(
            f"Invalid statement node type: {stmt.type}.", stmt.line_number)

    def visit_value_node(self, node):
        """handles ConstantValueNode, IDNode and ListSubscriptValueNode.
        Returns a type node!!!"""
        if isinstance(node, nodes.ConstantValueNode):
            return self.visit_constant_node(node)
        if isinstance(node, nodes.IDNode):
            return node.dcl_type
        if isinstance(node, nodes.ListSubscriptValueNode):
            return node.identifier.dcl_type

    def visit_element_list_node(self, node: nodes.ElementListNode, expected_type: nodes.TypeNode):
        """returns a type node containing the number of dimensions and the type of the elements in the list.
        Returns None and registers errors if the dimensions are inconsistent or the elements are of different types."""
        node = self.extract_type_node_from_elem_list(node, expected_type)

        return node.type
    
    def extract_type_node_from_elem_list(self, node: nodes.Node, expected_type: nodes.TypeNode):
        def has_valid_child_types(childs):
            first_child_type = childs[0].type
            return all(child.type == first_child_type and child.type.dimensions == first_child_type.dimensions for child in childs)

        # base case: primitive type
        if not isinstance(node, nodes.ElementListNode):
            node.type = nodes.TypeNode(node.line_number, self.visit_expression(node).type, 0)
            return node

        # base case: empty list
        if not node.expressions:
            node.type = nodes.TypeNode(node.line_number, expected_type.type, 1)
            return node

        childs = [self.extract_type_node_from_elem_list(child, expected_type) for child in node.expressions]

        if any(child is None for child in childs):
            return None

        if not has_valid_child_types(childs):
            self.register_err(f"List elements are not of the same type", node.line_number)
            return None

        first_child_type = childs[0].type
        node.type = nodes.TypeNode(node.line_number, first_child_type.type, first_child_type.dimensions + 1)
        return node
        
    def is_primitive(self, type_node:nodes.TypeNode):
        return type_node.type == NUM_TYPE or type_node.type == BOOL_TYPE or type_node.type == STRING_TYPE

    def visit_id_node(self, node: nodes.IDNode):
        return node.dcl_type.type

    def visit_constant_node(self, node):
        if isinstance(node, nodes.StringNode):
            return nodes.TypeNode(node.line_number, STRING_TYPE, 0)
        if isinstance(node, nodes.NumberNode):
            return nodes.TypeNode(node.line_number, NUM_TYPE, 0)
        if isinstance(node, nodes.BooleanNode):
            return nodes.TypeNode(node.line_number, BOOL_TYPE, 0)

    def visit_function_call(self, node: nodes.FunctionCallExpressionNode):
        function_return_type = node.dcl_type

        if len(node.arguments) != len(node.dcl_node.params):
            self.register_err(
                f"Function {node.identifier.identifier} received {len(node.arguments)} arguments, expected {len(node.dcl_node.params)}!", node.line_number)
            return function_return_type

        for i, parameters in enumerate(zip(node.arguments, node.dcl_node.params)):
            actual_parameter_type, formal_parameter_type = self.visit_expression(
                parameters[0],parameters[1]._type), parameters[1]._type
            # See note 1
            if not None in (actual_parameter_type, formal_parameter_type) and actual_parameter_type != formal_parameter_type:
                self.register_err(
                    f'Parameter {i+1} in function call "{node.identifier}" expected {formal_parameter_type.type}, got {actual_parameter_type.type}!', node.line_number)

        return function_return_type

    def visit_unary_expression(self, node: nodes.UnaryExpressionNode):
        expr_type_node = self.visit_expression(node.expression)
        # See note 1
        if not expr_type_node is None and expr_type_node.type != BOOL_TYPE and node.operator != "!":
            self.register_err(
                f"Expected bool with '!' operator, got {expr_type_node.type}.", node.line_number)

        return nodes.TypeNode(node.line_number, BOOL_TYPE, 0)

    def visit_binary_expression(self, node: nodes.BinaryExpressionNode):
        left_expr_type_node = self.visit_expression(node.left)
        right_expr_type_node = self.visit_expression(node.right)
        # See note 1
        if None in (left_expr_type_node, right_expr_type_node):
            return

        if left_expr_type_node == right_expr_type_node:

            if left_expr_type_node.type == NUM_TYPE:
                if node.operator in ["+", "-", "*", "/"]:
                    return nodes.TypeNode(node.line_number, NUM_TYPE, 0)
                elif node.operator in ["==", "!=", "<", ">", "<=", ">="]:
                    return nodes.TypeNode(node.line_number, BOOL_TYPE, 0)
                else:
                    self.register_err(
                        "Invalid operator for num type.", node.line_number)

            elif left_expr_type_node.type == STRING_TYPE:
                if node.operator in ["+"]:
                    return nodes.TypeNode(node.line_number, STRING_TYPE, 0)
                else:
                    self.register_err(
                        "Invalid operator for string type.", node.line_number)

            elif left_expr_type_node.type == BOOL_TYPE:
                if node.operator in ["&&", "||", "==", "!="]:
                    return nodes.TypeNode(node.line_number, BOOL_TYPE, 0)
                else:
                    self.register_err(
                        "Invalid operator for bool type.", node.line_number)

        else:
            self.register_err(
                f"Binary type mismatch, {left_expr_type_node.type} and {right_expr_type_node.type}. Expected {left_expr_type_node.type}.", node.line_number)

    def visit_assignment(self, node: nodes.AssignmentStatementNode):
       
        lhs_type_node = self.visit_value_node(node.identifier)
        
        if lhs_type_node is None: return # See note 1

        if not node.expression is None:
            rhs_type_node = self.visit_expression(node.expression,lhs_type_node)
            if rhs_type_node is None:
                return lhs_type_node # See note 1
            #                                    if there are subscripts we have to postpone the type comparison 
            if rhs_type_node != lhs_type_node and node.subscripts is None:
                self.register_err(f"Assignment type mismatch: Expected {lhs_type_node}, got {rhs_type_node}.", node.line_number)
                return 
        
        if not node.subscripts is None:
            lhs_number_of_subscripts = self.visit_list_subscript(node.subscripts)
            rhs_type_node = self.visit_expression(node.expression,lhs_type_node)
            # dimensions lhs + dimensions rhs = dcl dimensions
            if lhs_number_of_subscripts + rhs_type_node.dimensions != lhs_type_node.dimensions:
                if rhs_type_node.dimensions == 0:
                    self.register_err(f"Assignment subscript dimensions mismatch. Trying to assign a primitive value to a list subscripted with {lhs_number_of_subscripts} dimension(s), but the list was declared with {lhs_type_node.dimensions} dimensions.", node.line_number)
                else:
                    self.register_err(f"Assignment subscript dimensions mismatch. Trying to assign a list with {rhs_type_node.dimensions} dimension(s) to a list subscripted with {lhs_number_of_subscripts} dimension(s), but the list was declared with {lhs_type_node.dimensions} dimensions.", node.line_number)
                return 


        return lhs_type_node
        
    def visit_return(self, node: nodes.ReturnStatementNode):
        if not node.expected_return_type is None:
            return self.visit_expression(node.expression, node.expected_return_type)
        # default return is none

    def visit_declaration(self, node: nodes.DeclarationStatementNode):
        if not node.assignment is None:
            assign_type_node = self.visit_assignment(node.assignment)
            if assign_type_node is None:
                return  # see node 1

            dcl_type = self.visit_value_node(node.identifier)

            if dcl_type != assign_type_node:
                self.register_err(
                    f"Declaration type mismatch, {assign_type_node.type} and {dcl_type.type}. Expected {assign_type_node.type}.", node.line_number)

    def visit_function_declaration(self, node: nodes.FunctionNode):
        func_return_node = node._type

        # This might crash if default for statements_nodes is None?
        for stmt_node in node.block.statements_nodes:
            if isinstance(stmt_node, nodes.ReturnStatementNode):
                actual_return_type_node = self.visit_return(stmt_node)
                
                if func_return_node is None and not actual_return_type_node is None:
                    # Raise Error as the return type should be None
                    self.register_err(
                        f"Expected return: void, found return type: {actual_return_type_node.type}", node.line_number)

                if not func_return_node is None and func_return_node != actual_return_type_node and not actual_return_type_node is None:
                    # Raise Error as the expected return type dosent match the type of the return stmt
                    self.register_err(
                        f"Expected return: {func_return_node.type}, found return type: {actual_return_type_node.type}", node.line_number)

    def visit_list_subscript(self, node: nodes.ListSubscriptValueNode):
        """registers an error if any of the expressions in list subscript is no num type.
        Also asserts that dimensions are legal for the variable.
        
        Returns the number of subscripts as integer."""

        if node.identifier.dcl_type.dimensions < len(node.subscripts):
            self.register_err(
                f"Unable to subscript at depth {len(node.subscripts)} of identifier {node.identifier.identifier} with depth {node.identifier.dcl_dimensions}!", node.line_number)

        for expr_node in node.subscripts:
            expr_type_node = self.visit_expression(expr_node)
            if expr_type_node is None:
                break  # See note 1

            if expr_type_node.type != NUM_TYPE:
                self.register_err(
                    f"Expression {expr_type_node} not of Num Type.", node.line_number)
        return len(node.subscripts)
