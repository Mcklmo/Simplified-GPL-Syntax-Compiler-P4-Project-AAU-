from antlr4 import *
from AlgoPractiseLexer import AlgoPractiseLexer
from _parser.AlgoPractiseParser import AlgoPractiseParser
from antlr4.tree.Trees import Trees
from nodes import ASTNode
from visitors.ASTvisitor import ASTvisitor
from visitors.ASTSingleDispatchVisitor import ASTSingleDispatchVisitor
from antlr4 import FileStream, CommonTokenStream


def pretty_print_CST(node, indent_level=0):
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
    i = r"././input_stream/assignment_noerr.txt"
    input_stream = FileStream(i)
    lexer = AlgoPractiseLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = AlgoPractiseParser(stream)
    parse_tree_start_node = parser.start()

    # visitor = ASTvisitor()
    # ast_root = visitor.visit(parse_tree_start_node)
    single_dispatch_visitor = ASTSingleDispatchVisitor()
    ast_root = single_dispatch_visitor.Dispatch(parse_tree_start_node)
    ast_root.pretty_print()
    # print("CST:")
    # tree_str = Trees.toStringTree(parse_tree_start_node, None, parser)
    # print(tree_str)
    # # Print the parse tree
    # print("AST:")
    # pretty_print_AST(ast_root)
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
# TODO:
# Migrate from camel-case to snake_case
