from TypeCheckVisitors.type_check_visitors import NUM_TYPE, STRING_TYPE, BOOL_TYPE
import nodes

class CodeGenerator():
    map_type = lambda _, type_str: {NUM_TYPE: "double", STRING_TYPE: "str", BOOL_TYPE:"bool"}[type_str]

    def __init__(self):
        self.out = "class Program() {\n"
        self.current_indent = 1

    
    def save(self, path):
        with open(path, "w+") as f:
            f.write(self.out)
        
        print("Enjoy!")

    def write_line(self, _str):
        self.out += "\t"*self.current_indent+_str+"\n"

    def geenrate_type(self, type:nodes.TypeNode):
        if type.dimensions != 0:
            return f"List<{self.geenrate_type(nodes.TypeNode(type.line_number, type=type.type, dimensions=type.dimensions-1))}>"
        return self.map_type(type.type)

    def generate_function_call(self, node: nodes.FunctionCallExpressionNode): 
        return node.identifier.identifier+"("+",".join([self.generate_expression(expr) for expr in node.arguments])+")"

    def generate_element_list_type(self, node: nodes.ElementListNode): 
        return f"new List<{self.map_type(node.type.type)}>"+"{"+",".join([self.generate_expression(expr) for expr in node.expressions])+"}()"

    def generate_list_subscript_val(self, node: nodes.ListSubscriptValueNode):
        return f"{node.identifier}"+"".join([f"[{self.generate_expression(expr)}]" for expr in node.subscripts])
    
    def generate_expression(self, node):
        if isinstance(node, nodes.BinaryExpressionNode): return self.generate_binary_expression(node)
        if isinstance(node, nodes.UnaryExpressionNode): return self.generate_unary_expression(node)
        if isinstance(node, nodes.FunctionCallExpressionNode): return self.generate_function_call(node)

        return self.generate_value_node(node)

    def generate_binary_expression(self, node):
        return f"{self.generate_expression(node.left)}{node.operator}{self.generate_expression(node.right)}"

    def generate_unary_expression(self, node):
        return f"{node.operator}{self.generate_expression(node.expression)}"
    
    def generate_value_node(self, node):
        if isinstance(node, nodes.NumberNode): return str(node.value)
        if isinstance(node, nodes.StringNode): return node.value
        if isinstance(node, nodes.BooleanNode): return node.value
        if isinstance(node, nodes.IDNode): return node.identifier
        if isinstance(node, nodes.FunctionCallExpressionNode): return self.generate_function_call(node)
        if isinstance(node, nodes.ElementListNode): return self.generate_element_list_type(node)
        if isinstance(node, nodes.ListSubscriptVal): return self.generate_list_subscript_val(node)

