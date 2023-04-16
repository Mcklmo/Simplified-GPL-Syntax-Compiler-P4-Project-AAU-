from .AlgoPractiseVisitor import AlgoPractiseVisitor
from _parser.AlgoPractiseParser import AlgoPractiseParser
from nodes import StartNode, ASTNode
from typing import List
from antlr4.Token import CommonToken, Token
from antlr4 import ParserRuleContext
from nodes.DclValueNodes import NumDclNode, BoolDclNode, StringDclNode
from nodes.Assign_stmtNode import Assign_stmtNode
from nodes.IDNode import IDNode

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
    
        elif False: #TODO: Check for list (Is CFG right?)
            pass
        
        else:
            _type = ctx.type_().getText()
            if _type == "num":
                return NumDclNode(ctx.ID(), ctx.start.line)
            if _type == "bool":
                return BoolDclNode(ctx.ID(), ctx.start.line)
            if _type == "string":
                return StringDclNode(ctx.ID(), ctx.start.line)
        
    def visitAssign_stmt(self, ctx: AlgoPractiseParser.Assign_stmtContext):
        #  = parrent
        assign_node = Assign_stmtNode(ctx.start.line)

        # Parrent is dcl
        if isinstance(ctx.parentCtx, AlgoPractiseParser.DclContext): 
            return self.assign_stmtDcl(ctx, ctx.parentCtx) 
        
        elif False: pass # Is list TODO: implement
        else:
            #                            IdNode                             ExprNode
            assign_node.children.extend([IDNode(ctx.ID(), ctx.start.line), self.visit(ctx.expr())])
            return  assign_node



    def assign_stmtDcl(self, ctx:AlgoPractiseParser.Assign_stmtContext, parent: ParserRuleContext):
        assign_node = Assign_stmtNode(ctx.start.line)
        
        #                This is Assign_stmtNode
        _type = parent.getChild(0).type_().getText()

        if _type == "num":
            assign_node.children.append(NumDclNode(ctx.ID(), ctx.start.line))
        elif _type == "bool":
            assign_node.children.append(BoolDclNode(ctx.ID(), ctx.start.line))
        elif _type == "string":
            assign_node.children.append(StringDclNode(ctx.ID(), ctx.start.line))
        else: return None
            
        
        assign_node.children.append(ctx.expr())
        return assign_node