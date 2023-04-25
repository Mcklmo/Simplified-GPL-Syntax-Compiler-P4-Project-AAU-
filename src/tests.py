from tests.test_ast_single_dispatch_visitor import TestASTSingleDispatchVisitor

test_ast_single_dispatch_visitor = TestASTSingleDispatchVisitor()

test_ast_single_dispatch_visitor.setUp()
i=0
for method_name in dir(test_ast_single_dispatch_visitor):
    if method_name.startswith("test_"):
        method = getattr(test_ast_single_dispatch_visitor, method_name)
        method()
        print(f"Test {method_name} passed")
        i+=1
print(f"{i} tests passed")
