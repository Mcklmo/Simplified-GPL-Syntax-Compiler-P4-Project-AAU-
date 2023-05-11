from tests.test_ast_single_dispatch_visitor import TestASTSingleDispatchVisitor
from tests.test_type_check_visitor import TestTypeCheckVisitor
visitors = [
    TestASTSingleDispatchVisitor(),
    TestTypeCheckVisitor()
]


def run_tests(visitors):
    i = 0
    for visitor in visitors:
        visitor.setUp()

        print(str(type(visitor).__name__))

        for method_name in dir(visitor):
            if method_name.startswith("test_"):
                test_method = getattr(visitor, method_name)
                test_method()
                print(f"    {method_name}")
                i += 1

        visitor.tearDown()

    print(f"\n{i} tests ok")


run_tests(visitors)
