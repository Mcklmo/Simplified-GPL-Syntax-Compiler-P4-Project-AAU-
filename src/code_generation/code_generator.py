from TypeCheckVisitors.type_check_visitors import NUM_TYPE, STRING_TYPE, BOOL_TYPE
import nodes

class CodeGenerator():
    map_type = lambda type_str: {NUM_TYPE: "doubble", STRING_TYPE: "str", BOOL_TYPE:"bool"}[type_str]

    def __init__(self):
        self.out = "class Program() {\n"
        self.current_indent = 1

    
    def save(self, path):
        with open(path, "w+") as f:
            f.write(self.out)
        
        print("Enjoy!")

    def write_line(self, str):
        self.out += "\t"*self.current_indent+"\n"

    def geenrate_type(self, type:nodes.TypeNode):
        return self.map_type(type.type)+"[]"*type.dimensions

    def generate_function_call(self, node: nodes.FunctionCallExpressionNode): 
        return {node.identifier.identifier}+"("+",".join([self.generate_expression(expr) for expr in node.arguments])+")"

    def generate_element_list_type(self, node: nodes.ElementListNode): 
        return "{"+",".join([self.generate_expression(expr) for expr in node.expressions])+"}"

    def generate_list_subscript_val(self, node: nodes.ListSubscriptVal):
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

