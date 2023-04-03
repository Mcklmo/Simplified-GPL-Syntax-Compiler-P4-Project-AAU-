# Generated from AlgoPractise.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .AlgoPractiseParser import AlgoPractiseParser
else:
    from AlgoPractiseParser import AlgoPractiseParser

# This class defines a complete generic visitor for a parse tree produced by AlgoPractiseParser.

class AlgoPractiseVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by AlgoPractiseParser#start.
    def visitStart(self, ctx:AlgoPractiseParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoPractiseParser#func.
    def visitFunc(self, ctx:AlgoPractiseParser.FuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoPractiseParser#type.
    def visitType(self, ctx:AlgoPractiseParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoPractiseParser#args.
    def visitArgs(self, ctx:AlgoPractiseParser.ArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoPractiseParser#arg_list.
    def visitArg_list(self, ctx:AlgoPractiseParser.Arg_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoPractiseParser#block.
    def visitBlock(self, ctx:AlgoPractiseParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoPractiseParser#endblock.
    def visitEndblock(self, ctx:AlgoPractiseParser.EndblockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoPractiseParser#stmts.
    def visitStmts(self, ctx:AlgoPractiseParser.StmtsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoPractiseParser#stmt.
    def visitStmt(self, ctx:AlgoPractiseParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoPractiseParser#dcl.
    def visitDcl(self, ctx:AlgoPractiseParser.DclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoPractiseParser#assign_stmt.
    def visitAssign_stmt(self, ctx:AlgoPractiseParser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoPractiseParser#cond.
    def visitCond(self, ctx:AlgoPractiseParser.CondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoPractiseParser#orCond.
    def visitOrCond(self, ctx:AlgoPractiseParser.OrCondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoPractiseParser#andCond.
    def visitAndCond(self, ctx:AlgoPractiseParser.AndCondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoPractiseParser#cond2.
    def visitCond2(self, ctx:AlgoPractiseParser.Cond2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoPractiseParser#cond3.
    def visitCond3(self, ctx:AlgoPractiseParser.Cond3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoPractiseParser#cond4.
    def visitCond4(self, ctx:AlgoPractiseParser.Cond4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoPractiseParser#atom.
    def visitAtom(self, ctx:AlgoPractiseParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoPractiseParser#expr.
    def visitExpr(self, ctx:AlgoPractiseParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoPractiseParser#expr1.
    def visitExpr1(self, ctx:AlgoPractiseParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoPractiseParser#expr2.
    def visitExpr2(self, ctx:AlgoPractiseParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoPractiseParser#val.
    def visitVal(self, ctx:AlgoPractiseParser.ValContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoPractiseParser#cntrol.
    def visitCntrol(self, ctx:AlgoPractiseParser.CntrolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoPractiseParser#if_stmt.
    def visitIf_stmt(self, ctx:AlgoPractiseParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoPractiseParser#else_stmt.
    def visitElse_stmt(self, ctx:AlgoPractiseParser.Else_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoPractiseParser#while_stmt.
    def visitWhile_stmt(self, ctx:AlgoPractiseParser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoPractiseParser#func_call.
    def visitFunc_call(self, ctx:AlgoPractiseParser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoPractiseParser#list.
    def visitList(self, ctx:AlgoPractiseParser.ListContext):
        return self.visitChildren(ctx)



del AlgoPractiseParser