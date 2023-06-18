source_code = """
    print("hello "+bool_to_string(true)+" "+num_to_string(5))
    """
import os
from antlr4 import *
from antlr4.tree.Trees import Trees

from nodes.Node import Node
from compile import compile

SOURCE_CODE_FILE_NAME = r"././input_stream/fizzbuzz.algo"

def main(argv=None):
    success=compile_this(source_code)
    # success=compile_from_file(SOURCE_CODE_FILE_NAME)
    if success:
        print("Done")
    else:
        print("Failed")


def compile_from_file(source_code_path: str):
    return compile(source_code_path)

def compile_this(source_code: str):
    source_code_path = r"././input_stream/test.txt"
    write_file(source_code, source_code_path)
    success=compile(source_code_path)
    delete_file(source_code_path)
    return success

def delete_file( path: str):
    os.remove(path)
def write_file(content: str, path :str):
    with open(path, "w") as f:
        f.write(content)

def print_ast(node, indent=""):
    print(indent, node.__class__.__name__)
    indent += "    "

    for attribute_name, attribute_value in vars(node).items():
        if isinstance(attribute_value, Node):
            print_ast(attribute_value, indent)
        elif isinstance(attribute_value, list):
            print(indent, attribute_name, f"[{len(attribute_value)}]")
            indent += "    "
            for item in attribute_value:
                if isinstance(item, Node):
                    print_ast(item, indent)
                else:
                    print(indent, attribute_name, item)
            indent = indent[:-4]
        else:
            print(indent, attribute_name, attribute_value)

def print_cst(parser, parse_tree_start_node):
    print("CST:")
    tree_str = Trees.toStringTree(parse_tree_start_node, None, parser)
    print(tree_str)


if __name__ == "__main__":
    main()
# TODO:
# Migrate from camel-case to snake_case
