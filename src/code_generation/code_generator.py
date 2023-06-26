from TypeCheckVisitors.type_check_visitors import NUM_TYPE, STRING_TYPE, BOOL_TYPE
import nodes
from pre_defined_functions.pre_defined_functions import dotnet_to_string_conversions, pre_defined_fns_map,pre_defined_dotnet,called_on_the_instance


class CodeGenerator():
    def map_type(_, type_str): return {
        NUM_TYPE: "double", STRING_TYPE: "String", BOOL_TYPE: "bool", "void": "void"}[type_str]

    def __init__(self):
        self.out = "using System.Collections.Generic;\nusing System;\n\nclass Program {\n"+pre_defined_dotnet
      
        self.current_indent = 1

    def save(self, path):
        with open(path, "w+") as f:
            f.write(self.out+"\n}")

    def write_line(self, _str, end="\n", indent=None):
        if indent is None:
            self.out += "\t"*self.current_indent+_str+end
        else:
            self.out += "\t"*indent+_str+end

    def generate_type(self, type: nodes.TypeNode):
        if type.dimensions != 0:
            return f"List<{self.generate_type(nodes.TypeNode(type.line_number, type=type.type, dimensions=type.dimensions-1))}>"
        return self.map_type(type.type)

    def generate_function_call(self, node: nodes.FunctionCallExpressionNode):
        _ = [self.generate_expression(expr) for expr in node.arguments]
        _id = node.identifier.identifier

        if _id in dotnet_to_string_conversions:
            return self.generate_expression(node.arguments[0])+".ToString()"
        if _id in called_on_the_instance:
            _return= self.generate_expression(node.arguments[0])+"."+called_on_the_instance[_id] 
            _return += "("+",".join([self.generate_expression(expr) for expr in node.arguments[1:]])+")" if len(node.arguments)>1 else ""
            return _return
        return pre_defined_fns_map.get(_id, _id)+"("+",".join([self.generate_expression(expr) for expr in node.arguments])+")"

    def generate_element_list_type(self, node: nodes.ElementListNode):
        return f"new {'List<' * node.type.dimensions}{self.map_type(node.type.type)}{'>' * node.type.dimensions}"+"(){"+",".join([self.generate_expression(expr) for expr in node.expressions])+"}"

    def generate_assignment(self, node: nodes.AssignmentStatementNode):

        base = self.generate_list_subscript_val(
            node.subscripts) if node.subscripts is not None else node.identifier.identifier
        return f"{base} = {self.generate_expression(node.expression)}"

    def generate_list_subscript_val(self, node: nodes.ListSubscriptValueNode):
        return f"{node.identifier.identifier}"+"".join([f"[Convert.ToInt32({self.generate_expression(subscript)})]" for subscript in node.subscripts])

    def generate_expression(self, node):
        if isinstance(node, nodes.BinaryExpressionNode):
            return self.generate_binary_expression(node)
        if isinstance(node, nodes.UnaryExpressionNode):
            return self.generate_unary_expression(node)
        if isinstance(node, nodes.FunctionCallExpressionNode):
            return self.generate_function_call(node)

        return self.generate_value_node(node)

    def generate_binary_expression(self, node):
        operator_map = {
            "and": "&&",
            "or": "||",
        }
        result = f"{self.generate_expression(node.left)}{operator_map.get(node.operator,node.operator)}{self.generate_expression(node.right)}"
        return result

    def generate_unary_expression(self, node):
        return f"{node.operator}{self.generate_expression(node.expression)}"

    def generate_function_declaration(self, node: nodes.FunctionNode):
        return f"static public {self.generate_type(node.type)} {node.identifier.identifier}(" + ",".join([f"{self.generate_type(param._type)} {param.identifier.identifier}" for param in node.params]) + "){"

    def generate_value_node(self, node):
        if isinstance(node, nodes.NumberNode):
            return str(node.value)
        if isinstance(node, nodes.StringNode):
            return node.value
        if isinstance(node, nodes.BooleanNode):
            return node.value
        if isinstance(node, nodes.IDNode):
            return node.identifier
        if isinstance(node, nodes.FunctionCallExpressionNode):
            return self.generate_function_call(node)
        if isinstance(node, nodes.ElementListNode):
            return self.generate_element_list_type(node)
        if isinstance(node, nodes.ListSubscriptValueNode):
            return self.generate_list_subscript_val(node)

    def generate_if_statement(self, node: nodes.IfStatementNode):
        return f"if ({self.generate_expression(node.condition)})" + "{"

    def generate_while_statement(self, node: nodes.WhileStatementNode):
        return f"while ({self.generate_expression(node.condition)})" + "{"

    def generate_return_stmt(self, node: nodes.ReturnStatementNode):
        return f"return {self.generate_expression(node.expression)}"
