class SymbolTable:
    def __init__(self, vars,functions,childs):
        self.vars = vars
        self.functions = functions
        self.childs = childs

class Var:
    def __init__(self, name, type, value=None):
        self.name = name
        self.type = type
        # value is used to type check the variable in the type checking compiler phase
        # it is defaulted to none because Vars are used in function parameters
        self.value = value

class Function:
    def __init__(self, name, type, params, block):
        self.name = name
        self.type = type
        self.params = params
        self.block = block