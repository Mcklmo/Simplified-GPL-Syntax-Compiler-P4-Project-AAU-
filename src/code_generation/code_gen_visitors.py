import nodes
from .code_generator import CodeGenerator

class CodeGeneratorASTVisitor(CodeGenerator):
    def __init__(self):
        super().__init__()

    def do_visit(self, start_node: nodes.StartNode):
        self.visit_start_node(start_node)
        self.code_generator.save("./out.cs")
    

    def visit_start_node(self, node: nodes.StartNode):
        dcl_stmts, main_stmts, func_dcls = [], [], []

        for master_stmt in node.master_statement_nodes:
            if not master_stmt.statement_node is None:
                if isinstance(master_stmt.statement_node, nodes.DeclarationStatementNode):
                    self.dcl_stmts.append(master_stmt.statement_node)
                else:
                    self.main_stmts.append(master_stmt.statement_node)

            elif not master_stmt.function_node is None:
                self.func_dcls.append(master_stmt.function_node)
        
        map(self.visit_dcl, dcl_stmts)
        map(self.visit_func_dcl, func_dcls)
        self.visit_main_stmts(main_stmts)

        # Debug

        self.save("./out.cs")

    
    def visit_expression(self, node:nodes.ExpressionNode):
        if isinstance(node, nodes.BinaryExpressionNode):
            self.visit_binary_expression(node)
        if isinstance(node, nodes.UnaryExpressionNode):
            self.visit_unary_expression(node)
        if isinstance(node, nodes.FunctionCallExpressionNode):
            self.visit_function_call(node)

        self.visit_value_node(node)
    

    def visit_dcl(self, node:nodes.DeclarationStatementNode):
        base_str = f"{self.geenrate_type(node.type)} {node.identifier.identifier}"
        if node.assignment is None: self.write_line(base_str+";")
        else: self.write_line(base_str+f" = {self.visit_expression(node.assignment.expression)};")
    

    def visit_func_dcl(self, node: nodes.FunctionNode):
        pass
    def visit_main_stmts(self, node: nodes.FunctionNode):
        pass

    