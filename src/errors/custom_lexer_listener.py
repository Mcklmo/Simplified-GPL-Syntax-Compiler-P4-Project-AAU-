from antlr4.error.ErrorListener import ErrorListener

class CustomErrorListener(ErrorListener):

    def __init__(self):
        self.error_count = 0
        super(CustomErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.error_count += 1

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        pass 

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        pass

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        self.error_count += 1
