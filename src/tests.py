from tests.test_ast_single_dispatch_visitor import TestASTSingleDispatchVisitor
from tests.test_type_check_visitor import TestTypeCheckVisitor
from tests.test_integration_compile import TestIntegrationCompile
tests = [
    TestASTSingleDispatchVisitor(),
    TestTypeCheckVisitor(),
    TestIntegrationCompile()
]


def run_tests(tests):
    i = 0
    for test in tests:
        test.setUp()

        print(str(type(test).__name__))

        for method_name in dir(test):
            if method_name.startswith("test_"):
                test_method = getattr(test, method_name)
                test_method()
                print(f"    {method_name}")
                i += 1

        test.tearDown()

    print(f"\n{i} tests ok")


run_tests(tests)
