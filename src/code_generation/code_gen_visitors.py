import nodes
from .code_generator import CodeGenerator
from pre_defined_functions.pre_defined_functions import pre_defined_functions

pre_defined_function_ids = [fn.identifier.identifier for fn in pre_defined_functions]

# todo: fix dimensions of c# list generators (new list<list<...<<double>) in element list code generation. see current output and try to compile to c# for more info

class CodeGeneratorASTVisitor(CodeGenerator):
    def __init__(self):
        super().__init__()

    def do_visit(self, start_node: nodes.StartNode):
        self.visit_start_node(start_node)
        # Debug

        self.save("./out.cs")


    def visit_start_node(self, node: nodes.StartNode):
        dcl_stmts, main_stmts, func_dcls = [], [], []

        for master_stmt in node.master_statement_nodes:
            if not master_stmt.statement_node is None:
                if isinstance(master_stmt.statement_node, nodes.DeclarationStatementNode):
                    dcl_stmts.append(master_stmt.statement_node)
                else:
                    main_stmts.append(master_stmt.statement_node)

            elif not master_stmt.function_node is None:
                func_dcls.append(master_stmt.function_node)

        for node in dcl_stmts:
            self.visit_dcl(node)
        for node in func_dcls:
            # ignore pre-defined functions
            if node.identifier.identifier in pre_defined_function_ids:
                continue
            self.visit_func_dcl(node)
        self.visit_main_stmts(main_stmts)


    def visit_dcl(self, node:nodes.DeclarationStatementNode):
        base_str = f"{'static ' if node.is_global else ''}{self.generate_type(node.type)} {node.identifier.identifier}"
        if node.assignment is None: self.write_line(base_str+self.new_default_value(node)+";")
        else: self.write_line(base_str+f" = {self.generate_expression(node.assignment.expression)};")
    
    def new_default_value(self, node):
        types_mapping = {
            "num": " = 0.0",
            "string":" = \"\"",
            "bool":" = false"
        }
        return types_mapping[node.type.type]
    
    def visit_func_dcl(self, node: nodes.FunctionNode):
        self.write_line(self.generate_function_declaration(node))
        self.current_indent += 1
        self.visit_block(node.block)
        self.current_indent -= 1
        self.write_line("}")


    def visit_assignemnt(self, node: nodes.AssignmentStatementNode):
        self.write_line(self.generate_assignment(node)+";")


    def visit_function_call(self, node:nodes.FunctionCallStatementNode):
        self.write_line(self.generate_function_call(node) + ";")
        
    
    def visitIfStatementNode(self, node: nodes.IfStatementNode):
        self.write_line(self.generate_if_statement(node))
        self.current_indent += 1
        self.visit_block(node.block)
        self.current_indent -= 1
        self.write_line("}")
        if not node.else_node is None:
            if not node.else_node.if_statement is None:
                self.write_line("else " + self.generate_if_statement(node.else_node.if_statement))
                self.current_indent += 1
                self.visit_block(node.else_node.if_statement.block)
                self.current_indent -= 1
                self.write_line("}")
            else:
                self.write_line("else {")
                self.current_indent += 1
                self.visit_block(node.else_node.block)
                self.current_indent -= 1
                self.write_line("}")


    def visitWhileStatementNode(self, node: nodes.WhileStatementNode):
        self.write_line(self.generate_while_statement(node))
        self.current_indent += 1
        self.visit_block(node.block)
        self.current_indent -= 1
        self.write_line("}")
    

    def visitReturnStatementNode(self, node: nodes.ReturnStatementNode):
        self.write_line(f"{self.generate_return_stmt(node)};")


    def visit_block(self, node: nodes.BlockNode):
        # Inserting statements from block
        for statement_node in node.statements_nodes:
            if isinstance(statement_node, nodes.IfStatementNode):
                self.visitIfStatementNode(statement_node)
            elif isinstance(statement_node, nodes.WhileStatementNode):
                self.visitWhileStatementNode(statement_node)
            elif isinstance(statement_node, nodes.FunctionCallStatementNode):
                self.visit_function_call(statement_node)
                    
            elif isinstance(statement_node, nodes.AssignmentStatementNode):
                self.visit_assignemnt(statement_node)
            elif isinstance(statement_node, nodes.ReturnStatementNode):
                self.visitReturnStatementNode(statement_node)
            elif isinstance(statement_node, nodes.DeclarationStatementNode):
                self.visit_dcl(statement_node)


    def visit_main_stmts(self, stmt_nodes: nodes.FunctionNode):

        self.visit_func_dcl(
            nodes.FunctionNode(
                0,
                nodes.IDNode(
                    0,
                    identifier="Main",
                    dcl_type=None
                ),
                nodes.BlockNode(
                    0,
                    stmt_nodes
                ),
                [

                ],
                nodes.TypeNode(
                    0,
                    "void",
                    0
                )
            )

        )
