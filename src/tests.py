from tests.test_ast_single_dispatch_visitor import TestASTSingleDispatchVisitor

test_ast_single_dispatch_visitor = TestASTSingleDispatchVisitor()

test_ast_single_dispatch_visitor.setUp()
i=0
print("Running tests...\n")
for method_name in dir(test_ast_single_dispatch_visitor) :
    if method_name.startswith("test_"):
        test_method = getattr(test_ast_single_dispatch_visitor, method_name)
        test_method()
        print(f"{method_name}")
        i+=1
print(f"\n{i} tests ok")
