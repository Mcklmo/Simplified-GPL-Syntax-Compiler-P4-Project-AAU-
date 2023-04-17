# Generated from AlgoPractise.g4 by ANTLR 4.12.0
from antlr4 import *
from _parser.AlgoPractiseParser import AlgoPractiseParser

# This class defines a complete generic visitor for a parse tree produced by AlgoPractiseParser.

class AlgoPractiseVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by AlgoPractiseParser#start.
    def visitStart(self, ctx:AlgoPractiseParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoPractiseParser#func.
    def visitFunc(self, ctx:AlgoPractiseParser.FuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoPractiseParser#func_decl.
    def visitFunc_decl(self, ctx:AlgoPractiseParser.Func_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoPractiseParser#type.
    def visitType(self, ctx:AlgoPractiseParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoPractiseParser#params.
    def visitParams(self, ctx:AlgoPractiseParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoPractiseParser#param_lst.
    def visitParam_lst(self, ctx:AlgoPractiseParser.Param_lstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoPractiseParser#param.
    def visitParam(self, ctx:AlgoPractiseParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoPractiseParser#block.
    def visitBlock(self, ctx:AlgoPractiseParser.BlockContext):
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


    # Visit a parse tree produced by AlgoPractiseParser#expr.
    def visitExpr(self, ctx:AlgoPractiseParser.ExprContext):
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


    # Visit a parse tree produced by AlgoPractiseParser#elmnt_list.
    def visitElmnt_list(self, ctx:AlgoPractiseParser.Elmnt_listContext):
        return self.visitChildren(ctx)



del AlgoPractiseParser