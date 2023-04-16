import sys
from antlr4 import *
from AlgoPractiseLexer import AlgoPractiseLexer
from _parser.AlgoPractiseParser import AlgoPractiseParser
from antlr4.tree.Trees import Trees
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
    visitor.visit(parse_tree)
    # listener = AlgoPractiseListener()
    # walker = ParseTreeWalker()
    # walker.walk(listener, parse_tree)

    # Print the parse tree
    tree_str = Trees.toStringTree(parse_tree, None, parser)
    print(tree_str)

    # Optionally, you can write the parse tree to an output file
    with open("output.txt", "w") as output_file:
        output_file.write(tree_str)
    
    # Generate DOT representation of parse tree
    dot, _ = generate_tree_dot(parse_tree, parser)

    # Write DOT representation to a file
    with open("output.dot", "w") as output_file:
        output_file.write("digraph G {\n")
        output_file.write(dot)
        output_file.write("}\n")

if __name__ == "__main__":
    main()
#TODO:
# Migrate from camel-case to snake_case