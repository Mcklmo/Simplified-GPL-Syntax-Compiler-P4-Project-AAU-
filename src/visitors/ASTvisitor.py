from .AlgoPractiseVisitor import AlgoPractiseVisitor
from _parser.AlgoPractiseParser import AlgoPractiseParser
from nodes import StartNode, ASTNode
from typing import List
from antlr4.Token import CommonToken, Token
from antlr4 import ParserRuleContext
from nodes.BoolDcnNode import  BoolDclNode
from nodes.NumDcnNode import  NumDclNode
from nodes.StringDcnNode import  StringDclNode
from nodes.Assign_stmtNode import Assign_stmtNode
from nodes.IDNode import IDNode
from nodes.FuncDclNode import FuncDclNode
from nodes.Param_lstNode import Param_lstNode
from nodes.ListDcnNode import ListDclNode
from nodes.BinExprNode import BinExprNode
from nodes.NegExprNode import NegExprNode
from nodes.ParenthesesExpr import ParenthesesExpr
from nodes.ValNode import ValNode
from nodes.While_stmtNode import While_stmtNode
from nodes.BlockNode import BlockNode


class ASTvisitor(AlgoPractiseVisitor):

    def visitStart(self, ctx: AlgoPractiseParser.StartContext):
        return self.childVisitor(StartNode.StartNode(), ctx.children)
    
    def childVisitor(self, node:ASTNode.ASTNode, children:List[ParserRuleContext]):
        # Itterate through all childrn of node
        for child in children:
            # Check if child is terminal node
            
            if child.getChildCount() == 0: 
                continue
        
            node.children.append(self.visit(child))
        
        return node

    def visitDcl(self, ctx: AlgoPractiseParser.DclContext):
        assign_context = ctx.assign_stmt()

        if not assign_context is None:
            return self.visit(assign_context)
        
        else:
            _type = ctx.type_().getText()
            if "[" in _type and "]" in _type:
                return self.listDcl(ctx)
 
            if _type == "num":
                return NumDclNode(ctx.ID(), ctx.start.line)
            if _type == "bool":
                return BoolDclNode(ctx.ID(), ctx.start.line)
            if _type == "string":
                return StringDclNode(ctx.ID(), ctx.start.line)
    
    def listDcl(self, parent: AlgoPractiseParser.DclContext):
        return ListDclNode(parent.ID(), parent.type_().getText().replace("[", "").replace("]", ""), parent.type_().getText().count("[]"), parent.start.line)
            
    def visitAssign_stmt(self, ctx: AlgoPractiseParser.Assign_stmtContext):
        #  = parrent
        assign_node = Assign_stmtNode(ctx.start.line)

        # Parrent is dcl
        if isinstance(ctx.parentCtx, AlgoPractiseParser.DclContext): 
            return self.assign_stmtDcl(ctx, ctx.parentCtx) 
        
        else:
            #                            IdNode                             ExprNode
            assign_node.children.extend([IDNode(ctx.ID(), ctx.start.line), self.visit(ctx.expr())])
            return  assign_node



    def assign_stmtDcl(self, ctx:AlgoPractiseParser.Assign_stmtContext, parent: ParserRuleContext):
        assign_node = Assign_stmtNode(ctx.start.line)
        
        #                This is Assign_stmtNode
        _type = parent.type_().getText()
        if "[" in _type and "]" in _type:
            assign_node.children.append(self.listDcl(parent))
        
        elif _type == "num":
            assign_node.children.append(NumDclNode(ctx.ID(), ctx.start.line))
        elif _type == "bool":
            assign_node.children.append(BoolDclNode(ctx.ID(), ctx.start.line))
        elif _type == "string":
            assign_node.children.append(StringDclNode(ctx.ID(), ctx.start.line))
        else: return None
            
        #                                       ExprNode
        assign_node.children.append(self.visit(ctx.expr()))
        return assign_node

    def visitFunc_decl(self, ctx: AlgoPractiseParser.Func_declContext):
        return_type = "void"
        #                   Return type defined
        if ctx.parentCtx.getChildCount() == 2:
            return_type = ctx.parentCtx.getChild(0).getText()

        funcNode = FuncDclNode(ctx.ID(), return_type, ctx.start.line)
        #                                                       ParamNode
        if not ctx.params() is None: funcNode.children.append(self.visit(ctx.params()))
        #                   BlockNode
        funcNode.children.append(self.visit(ctx.block()))

        return funcNode

    def visitParam(self, ctx: AlgoPractiseParser.ParamContext):
        return IDNode(ctx.ID(), ctx.type_().getText(),  ctx.start.line)
    
    def visitParam_lst(self, ctx: AlgoPractiseParser.Param_lstContext):
        paramNode = Param_lstNode(ctx.start.line)
        for child in ctx.getChildren():
            if child.getText() == ",": continue

            if child.getChild(0).getText() in ("num", "bool", "string"):
                paramNode.children.append(self.visit(child))
            else:
                #err
                pass
    
        return paramNode
    
    def visitExpr(self, ctx: AlgoPractiseParser.ExprContext):
        sub_exprs = ctx.expr()

        expr = None
        if len(sub_exprs) == 2:
            # BinaryExpr
            expr = BinExprNode(ctx.getChild(1).getText(), ctx.start.line)
            expr.children.extend([self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2))])
            
        elif len(sub_exprs) == 1:
            # either neg or parantheses
            if ctx.getChild(0).getText() == "!":
                expr = NegExprNode(ctx.start.line)
                expr.children.append(self.visit(ctx.getChild(1)))

            elif ctx.getChild(0).getText() == "(":
                expr = ParenthesesExpr(ctx.start.line)
                expr.children.append(self.visit(ctx.getChild(1)))
            else:
                pass
                #err
        else:
            expr = ValNode(ctx.start.line)
            expr.children.append(self.visit(ctx.getChild(0)))
        return expr
    
    def visitVal(self, ctx: AlgoPractiseParser.ValContext):
        pass

    def visitWhile_stmt(self, ctx: AlgoPractiseParser.While_stmtContext):
        while_node = While_stmtNode(ctx.start.line)
        i = ctx.block()
        while_node.children.extend([self.visit(ctx.expr()), self.visit(ctx.block())])
        return while_node
    
    def visitBlock(self, ctx: AlgoPractiseParser.BlockContext):
        block_node = BlockNode(ctx.start.line)
        stmts = ctx.stmts()
        if not stmts is None:       
            block_node.children.extend([self.visit(stmt) for stmt in stmts.stmt()])
        return block_node

    def visitVal(self, ctx: AlgoPractiseParser.ValContext):
        id_node = ctx.ID()
        elem_list = ctx.elmnt_list()

        if not id_node is None:
            # ID or subscript
            pass

        elif not elem_list is None:
            # raw List val
            pass
   
    def visitBlock(self, ctx: AlgoPractiseParser.BlockContext):
        block_node = BlockNode(ctx.start.line)
        stmts = ctx.stmts()
        if not stmts is None:       
            block_node.children.extend([self.visit(stmt) for stmt in stmts.stmt()])
        return block_node
