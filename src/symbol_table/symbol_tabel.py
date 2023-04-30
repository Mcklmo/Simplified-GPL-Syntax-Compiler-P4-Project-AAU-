import nodes
from symbol_table.stack import Stack


class SymbolTableVisitor():
    def __init__(self) -> None:
        self.symbol_tabel = Stack()

    def startVisitor(self, node: nodes):
        self.symbol_tabel.open_scope()
        