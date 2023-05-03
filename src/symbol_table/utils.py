from symbol_table.stack import Stack



class Error():
    def __init__(self, msg, line_number) -> None:
        self.msg = msg
        self.line_number = line_number

    def __str__(self) -> str:
        return f"Line {self.line_number}  -  {self.msg}"


class SymbolTableUtils:
    def __init__(self) -> None:
        self.symbol_tabel = Stack()
        self.errors = []

    @staticmethod
    def is_iterable(obj):
        try:
            iterator = iter(obj)
        except TypeError:
            # not iterable
            return False
        else:
            # iterable
            return True

    def regsiter_err(self, msg, line_number):
        self.errors.append(Error(
            msg, 
            line_number
        ))