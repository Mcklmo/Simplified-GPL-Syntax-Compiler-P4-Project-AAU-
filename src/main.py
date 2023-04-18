from antlr4 import *
from AlgoPractiseLexer import AlgoPractiseLexer
from _parser.AlgoPractiseParser import AlgoPractiseParser
from antlr4.tree.Trees import Trees
from nodes import ASTNode
from visitors import ASTvisitor
from antlr4 import FileStream, CommonTokenStream

# Custom function to generate DOT representation of parse tree
def generate_tree_dot(tree, parser, parent=None, counter=[0]):
    node_id = counter[0]
    counter[0] += 1
    dot = f'n{node_id} [label="{tree.getText()}"];\n'

    if parent is not None:
        dot += f'n{parent} -> n{node_id};\n'

    if tree.getChildCount() > 0:
        for child in tree.children:
            child_dot, child_id = generate_tree_dot(child, parser, node_id, counter)
            dot += child_dot
 
    return dot, node_id

def pretty_print_AST(node: ASTNode, indent_level: int = 0):
    if node is None:
        return

    # Prepare the attributes string to be printed
    attributes = ", ".join([f"{key}: {value}" for key, value in node.__dict__.items() if key != "children" and key != "line_number"])

    # Print the current node's attributes with indentation
    print("  " * indent_level + f"(line: {node.line_number}) {type(node).__name__} [{attributes}]")

    # Recursively pretty-print children nodes
    for child_node in node.children:
        pretty_print_AST(child_node, indent_level + 1)

def pretty_print_CST(node, indent_level = 0):
    t = Trees 
    text = t.getNodeText(node)
    if text is None:
        text = node.__class__.__name__
    if text is None or "[" in text and "]" in text:
        pass 
    else:
        print("  " * indent_level + f"{text}")
    for i in range(node.getChildCount()):
        pretty_print_CST(node.getChild(i), indent_level + 1)

def main(argv=None):
    # if len(argv) < 2:
    #     print("Usage: python main.py <input_file>")
    #     return
    i = r"./test.txt"
    input_stream = FileStream(i)
    lexer = AlgoPractiseLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = AlgoPractiseParser(stream)
    parse_tree = parser.start()

    visitor = ASTvisitor.ASTvisitor()
    root = visitor.visit(parse_tree)
    print("CST:")
    pretty_print_CST(parse_tree)
    print("AST:")
    pretty_print_AST(root)
    # listener = AlgoPractiseListener()
    # walker = ParseTreeWalker()
    # walker.walk(listener, parse_tree)

    # Print the parse tree
    # tree_str = Trees.toStringTree(parse_tree, None, parser)
    # print(tree_str)

    # Optionally, you can write the parse tree to an output file
    # with open("output.txt", "w") as output_file:
    #     output_file.write(tree_str)
    
    # Generate DOT representation of parse tree
    # dot, _ = generate_tree_dot(parse_tree, parser)

    # Write DOT representation to a file
    # with open("output.dot", "w") as output_file:
    #     output_file.write("digraph G {\n")
    #     output_file.write(dot)
    #     output_file.write("}\n")

if __name__ == "__main__":
    main()
#TODO:
# Migrate from camel-case to snake_case