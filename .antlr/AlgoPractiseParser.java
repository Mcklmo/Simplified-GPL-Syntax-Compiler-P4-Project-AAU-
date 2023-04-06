// Generated from d:\OneDrive\projects\GitHub\p4-group-project\AlgoPractise.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class AlgoPractiseParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		BOOL_TYPE=1, STR_TYPE=2, NUM_TYPE=3, TRUE=4, FALSE=5, IF=6, ELSE=7, WHILE=8, 
		AND=9, OR=10, ID=11, LIST_DCL=12, L_PAR=13, R_PAR=14, L_CURLY=15, R_CURLY=16, 
		RETURN=17, ASSIGN=18, NUMVAL=19, STRINGVAL=20, NEG=21, EQUAL=22, LTE=23, 
		GTE=24, LT=25, GT=26, NE=27, PLUS=28, MINUS=29, MULT=30, DIV=31, MOD=32, 
		COMMA=33, WS=34;
	public static final int
		RULE_start = 0, RULE_func = 1, RULE_func_decl = 2, RULE_type = 3, RULE_type_decl = 4, 
		RULE_params = 5, RULE_param_lst = 6, RULE_param = 7, RULE_block = 8, RULE_endblock = 9, 
		RULE_stmts = 10, RULE_stmt = 11, RULE_dcl = 12, RULE_assign_stmt = 13, 
		RULE_expr = 14, RULE_val = 15, RULE_cntrol = 16, RULE_if_stmt = 17, RULE_else_stmt = 18, 
		RULE_while_stmt = 19, RULE_func_call = 20, RULE_list = 21;
	private static String[] makeRuleNames() {
		return new String[] {
			"start", "func", "func_decl", "type", "type_decl", "params", "param_lst", 
			"param", "block", "endblock", "stmts", "stmt", "dcl", "assign_stmt", 
			"expr", "val", "cntrol", "if_stmt", "else_stmt", "while_stmt", "func_call", 
			"list"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'bool'", "'string'", "'num'", "'true'", "'false'", "'if'", "'else'", 
			"'while'", "'and'", "'or'", null, "'[]'", "'('", "')'", "'{'", "'}'", 
			"'return'", "':='", null, null, "'!'", "'=='", "'<='", "'>='", "'<'", 
			"'>'", "'!='", "'+'", "'-'", "'*'", "'/'", "'%'", "','"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "BOOL_TYPE", "STR_TYPE", "NUM_TYPE", "TRUE", "FALSE", "IF", "ELSE", 
			"WHILE", "AND", "OR", "ID", "LIST_DCL", "L_PAR", "R_PAR", "L_CURLY", 
			"R_CURLY", "RETURN", "ASSIGN", "NUMVAL", "STRINGVAL", "NEG", "EQUAL", 
			"LTE", "GTE", "LT", "GT", "NE", "PLUS", "MINUS", "MULT", "DIV", "MOD", 
			"COMMA", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "AlgoPractise.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public AlgoPractiseParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class StartContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(AlgoPractiseParser.EOF, 0); }
		public List<FuncContext> func() {
			return getRuleContexts(FuncContext.class);
		}
		public FuncContext func(int i) {
			return getRuleContext(FuncContext.class,i);
		}
		public List<StmtsContext> stmts() {
			return getRuleContexts(StmtsContext.class);
		}
		public StmtsContext stmts(int i) {
			return getRuleContext(StmtsContext.class,i);
		}
		public StartContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_start; }
	}

	public final StartContext start() throws RecognitionException {
		StartContext _localctx = new StartContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_start);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(48);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << BOOL_TYPE) | (1L << STR_TYPE) | (1L << NUM_TYPE) | (1L << IF) | (1L << WHILE) | (1L << ID))) != 0)) {
				{
				setState(46);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
				case 1:
					{
					setState(44);
					func();
					}
					break;
				case 2:
					{
					setState(45);
					stmts();
					}
					break;
				}
				}
				setState(50);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(51);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FuncContext extends ParserRuleContext {
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public Func_declContext func_decl() {
			return getRuleContext(Func_declContext.class,0);
		}
		public FuncContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_func; }
	}

	public final FuncContext func() throws RecognitionException {
		FuncContext _localctx = new FuncContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_func);
		try {
			setState(57);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case BOOL_TYPE:
			case STR_TYPE:
			case NUM_TYPE:
				enterOuterAlt(_localctx, 1);
				{
				setState(53);
				type();
				setState(54);
				func_decl();
				}
				break;
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				setState(56);
				func_decl();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Func_declContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(AlgoPractiseParser.ID, 0); }
		public ParamsContext params() {
			return getRuleContext(ParamsContext.class,0);
		}
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public Func_declContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_func_decl; }
	}

	public final Func_declContext func_decl() throws RecognitionException {
		Func_declContext _localctx = new Func_declContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_func_decl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(59);
			match(ID);
			setState(60);
			params();
			setState(61);
			block();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TypeContext extends ParserRuleContext {
		public TerminalNode BOOL_TYPE() { return getToken(AlgoPractiseParser.BOOL_TYPE, 0); }
		public TerminalNode STR_TYPE() { return getToken(AlgoPractiseParser.STR_TYPE, 0); }
		public TerminalNode NUM_TYPE() { return getToken(AlgoPractiseParser.NUM_TYPE, 0); }
		public TypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_type; }
	}

	public final TypeContext type() throws RecognitionException {
		TypeContext _localctx = new TypeContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_type);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(63);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << BOOL_TYPE) | (1L << STR_TYPE) | (1L << NUM_TYPE))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Type_declContext extends ParserRuleContext {
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public TerminalNode LIST_DCL() { return getToken(AlgoPractiseParser.LIST_DCL, 0); }
		public Type_declContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_type_decl; }
	}

	public final Type_declContext type_decl() throws RecognitionException {
		Type_declContext _localctx = new Type_declContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_type_decl);
		try {
			setState(69);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(65);
				type();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(66);
				type();
				setState(67);
				match(LIST_DCL);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ParamsContext extends ParserRuleContext {
		public TerminalNode L_PAR() { return getToken(AlgoPractiseParser.L_PAR, 0); }
		public TerminalNode R_PAR() { return getToken(AlgoPractiseParser.R_PAR, 0); }
		public Param_lstContext param_lst() {
			return getRuleContext(Param_lstContext.class,0);
		}
		public ParamsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_params; }
	}

	public final ParamsContext params() throws RecognitionException {
		ParamsContext _localctx = new ParamsContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_params);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(77);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
			case 1:
				{
				setState(71);
				match(L_PAR);
				setState(72);
				match(R_PAR);
				}
				break;
			case 2:
				{
				setState(73);
				match(L_PAR);
				setState(74);
				param_lst();
				setState(75);
				match(R_PAR);
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Param_lstContext extends ParserRuleContext {
		public List<ParamContext> param() {
			return getRuleContexts(ParamContext.class);
		}
		public ParamContext param(int i) {
			return getRuleContext(ParamContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(AlgoPractiseParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(AlgoPractiseParser.COMMA, i);
		}
		public Param_lstContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_param_lst; }
	}

	public final Param_lstContext param_lst() throws RecognitionException {
		Param_lstContext _localctx = new Param_lstContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_param_lst);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(79);
			param();
			setState(84);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(80);
				match(COMMA);
				setState(81);
				param();
				}
				}
				setState(86);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ParamContext extends ParserRuleContext {
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public TerminalNode ID() { return getToken(AlgoPractiseParser.ID, 0); }
		public ParamContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_param; }
	}

	public final ParamContext param() throws RecognitionException {
		ParamContext _localctx = new ParamContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_param);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(87);
			type();
			setState(88);
			match(ID);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BlockContext extends ParserRuleContext {
		public TerminalNode L_CURLY() { return getToken(AlgoPractiseParser.L_CURLY, 0); }
		public StmtsContext stmts() {
			return getRuleContext(StmtsContext.class,0);
		}
		public EndblockContext endblock() {
			return getRuleContext(EndblockContext.class,0);
		}
		public BlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block; }
	}

	public final BlockContext block() throws RecognitionException {
		BlockContext _localctx = new BlockContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_block);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(90);
			match(L_CURLY);
			setState(91);
			stmts();
			setState(92);
			endblock();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class EndblockContext extends ParserRuleContext {
		public TerminalNode RETURN() { return getToken(AlgoPractiseParser.RETURN, 0); }
		public ValContext val() {
			return getRuleContext(ValContext.class,0);
		}
		public TerminalNode R_CURLY() { return getToken(AlgoPractiseParser.R_CURLY, 0); }
		public EndblockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_endblock; }
	}

	public final EndblockContext endblock() throws RecognitionException {
		EndblockContext _localctx = new EndblockContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_endblock);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(99);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case RETURN:
				{
				setState(94);
				match(RETURN);
				setState(95);
				val();
				setState(96);
				match(R_CURLY);
				}
				break;
			case R_CURLY:
				{
				setState(98);
				match(R_CURLY);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StmtsContext extends ParserRuleContext {
		public StmtContext stmt() {
			return getRuleContext(StmtContext.class,0);
		}
		public StmtsContext stmts() {
			return getRuleContext(StmtsContext.class,0);
		}
		public StmtsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stmts; }
	}

	public final StmtsContext stmts() throws RecognitionException {
		StmtsContext _localctx = new StmtsContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_stmts);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(105);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
			case 1:
				{
				setState(101);
				stmt();
				setState(102);
				stmts();
				}
				break;
			case 2:
				{
				setState(104);
				stmt();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StmtContext extends ParserRuleContext {
		public DclContext dcl() {
			return getRuleContext(DclContext.class,0);
		}
		public Assign_stmtContext assign_stmt() {
			return getRuleContext(Assign_stmtContext.class,0);
		}
		public CntrolContext cntrol() {
			return getRuleContext(CntrolContext.class,0);
		}
		public Func_callContext func_call() {
			return getRuleContext(Func_callContext.class,0);
		}
		public StmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stmt; }
	}

	public final StmtContext stmt() throws RecognitionException {
		StmtContext _localctx = new StmtContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_stmt);
		try {
			setState(111);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(107);
				dcl();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(108);
				assign_stmt();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(109);
				cntrol();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(110);
				func_call();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DclContext extends ParserRuleContext {
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public Assign_stmtContext assign_stmt() {
			return getRuleContext(Assign_stmtContext.class,0);
		}
		public DclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_dcl; }
	}

	public final DclContext dcl() throws RecognitionException {
		DclContext _localctx = new DclContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_dcl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(113);
			type();
			setState(114);
			assign_stmt();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Assign_stmtContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(AlgoPractiseParser.ID, 0); }
		public TerminalNode ASSIGN() { return getToken(AlgoPractiseParser.ASSIGN, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public Assign_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assign_stmt; }
	}

	public final Assign_stmtContext assign_stmt() throws RecognitionException {
		Assign_stmtContext _localctx = new Assign_stmtContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_assign_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(116);
			match(ID);
			setState(117);
			match(ASSIGN);
			setState(118);
			expr(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExprContext extends ParserRuleContext {
		public TerminalNode NEG() { return getToken(AlgoPractiseParser.NEG, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public ValContext val() {
			return getRuleContext(ValContext.class,0);
		}
		public TerminalNode L_PAR() { return getToken(AlgoPractiseParser.L_PAR, 0); }
		public TerminalNode R_PAR() { return getToken(AlgoPractiseParser.R_PAR, 0); }
		public TerminalNode OR() { return getToken(AlgoPractiseParser.OR, 0); }
		public TerminalNode AND() { return getToken(AlgoPractiseParser.AND, 0); }
		public TerminalNode EQUAL() { return getToken(AlgoPractiseParser.EQUAL, 0); }
		public TerminalNode NE() { return getToken(AlgoPractiseParser.NE, 0); }
		public TerminalNode LTE() { return getToken(AlgoPractiseParser.LTE, 0); }
		public TerminalNode GTE() { return getToken(AlgoPractiseParser.GTE, 0); }
		public TerminalNode GT() { return getToken(AlgoPractiseParser.GT, 0); }
		public TerminalNode LT() { return getToken(AlgoPractiseParser.LT, 0); }
		public TerminalNode PLUS() { return getToken(AlgoPractiseParser.PLUS, 0); }
		public TerminalNode MINUS() { return getToken(AlgoPractiseParser.MINUS, 0); }
		public TerminalNode MULT() { return getToken(AlgoPractiseParser.MULT, 0); }
		public TerminalNode DIV() { return getToken(AlgoPractiseParser.DIV, 0); }
		public TerminalNode MOD() { return getToken(AlgoPractiseParser.MOD, 0); }
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	}

	public final ExprContext expr() throws RecognitionException {
		return expr(0);
	}

	private ExprContext expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprContext _localctx = new ExprContext(_ctx, _parentState);
		ExprContext _prevctx = _localctx;
		int _startState = 28;
		enterRecursionRule(_localctx, 28, RULE_expr, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(128);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NEG:
				{
				setState(121);
				match(NEG);
				setState(122);
				expr(3);
				}
				break;
			case TRUE:
			case FALSE:
			case ID:
			case L_CURLY:
			case NUMVAL:
			case STRINGVAL:
				{
				setState(123);
				val();
				}
				break;
			case L_PAR:
				{
				setState(124);
				match(L_PAR);
				setState(125);
				expr(0);
				setState(126);
				match(R_PAR);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(171);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,11,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(169);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,10,_ctx) ) {
					case 1:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(130);
						if (!(precpred(_ctx, 16))) throw new FailedPredicateException(this, "precpred(_ctx, 16)");
						setState(131);
						match(OR);
						setState(132);
						expr(17);
						}
						break;
					case 2:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(133);
						if (!(precpred(_ctx, 15))) throw new FailedPredicateException(this, "precpred(_ctx, 15)");
						setState(134);
						match(AND);
						setState(135);
						expr(16);
						}
						break;
					case 3:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(136);
						if (!(precpred(_ctx, 14))) throw new FailedPredicateException(this, "precpred(_ctx, 14)");
						setState(137);
						match(EQUAL);
						setState(138);
						expr(15);
						}
						break;
					case 4:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(139);
						if (!(precpred(_ctx, 13))) throw new FailedPredicateException(this, "precpred(_ctx, 13)");
						setState(140);
						match(NE);
						setState(141);
						expr(14);
						}
						break;
					case 5:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(142);
						if (!(precpred(_ctx, 12))) throw new FailedPredicateException(this, "precpred(_ctx, 12)");
						setState(143);
						match(LTE);
						setState(144);
						expr(13);
						}
						break;
					case 6:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(145);
						if (!(precpred(_ctx, 11))) throw new FailedPredicateException(this, "precpred(_ctx, 11)");
						setState(146);
						match(GTE);
						setState(147);
						expr(12);
						}
						break;
					case 7:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(148);
						if (!(precpred(_ctx, 10))) throw new FailedPredicateException(this, "precpred(_ctx, 10)");
						setState(149);
						match(GT);
						setState(150);
						expr(11);
						}
						break;
					case 8:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(151);
						if (!(precpred(_ctx, 9))) throw new FailedPredicateException(this, "precpred(_ctx, 9)");
						setState(152);
						match(LT);
						setState(153);
						expr(10);
						}
						break;
					case 9:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(154);
						if (!(precpred(_ctx, 8))) throw new FailedPredicateException(this, "precpred(_ctx, 8)");
						setState(155);
						match(PLUS);
						setState(156);
						expr(9);
						}
						break;
					case 10:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(157);
						if (!(precpred(_ctx, 7))) throw new FailedPredicateException(this, "precpred(_ctx, 7)");
						setState(158);
						match(MINUS);
						setState(159);
						expr(8);
						}
						break;
					case 11:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(160);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(161);
						match(MULT);
						setState(162);
						expr(7);
						}
						break;
					case 12:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(163);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(164);
						match(DIV);
						setState(165);
						expr(6);
						}
						break;
					case 13:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(166);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(167);
						match(MOD);
						setState(168);
						expr(5);
						}
						break;
					}
					} 
				}
				setState(173);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,11,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class ValContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(AlgoPractiseParser.ID, 0); }
		public TerminalNode NUMVAL() { return getToken(AlgoPractiseParser.NUMVAL, 0); }
		public TerminalNode STRINGVAL() { return getToken(AlgoPractiseParser.STRINGVAL, 0); }
		public TerminalNode TRUE() { return getToken(AlgoPractiseParser.TRUE, 0); }
		public TerminalNode FALSE() { return getToken(AlgoPractiseParser.FALSE, 0); }
		public TerminalNode L_CURLY() { return getToken(AlgoPractiseParser.L_CURLY, 0); }
		public ListContext list() {
			return getRuleContext(ListContext.class,0);
		}
		public TerminalNode R_CURLY() { return getToken(AlgoPractiseParser.R_CURLY, 0); }
		public Func_callContext func_call() {
			return getRuleContext(Func_callContext.class,0);
		}
		public ValContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_val; }
	}

	public final ValContext val() throws RecognitionException {
		ValContext _localctx = new ValContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_val);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(184);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,12,_ctx) ) {
			case 1:
				{
				setState(174);
				match(ID);
				}
				break;
			case 2:
				{
				setState(175);
				match(NUMVAL);
				}
				break;
			case 3:
				{
				setState(176);
				match(STRINGVAL);
				}
				break;
			case 4:
				{
				setState(177);
				match(TRUE);
				}
				break;
			case 5:
				{
				setState(178);
				match(FALSE);
				}
				break;
			case 6:
				{
				setState(179);
				match(L_CURLY);
				setState(180);
				list();
				setState(181);
				match(R_CURLY);
				}
				break;
			case 7:
				{
				setState(183);
				func_call();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class CntrolContext extends ParserRuleContext {
		public If_stmtContext if_stmt() {
			return getRuleContext(If_stmtContext.class,0);
		}
		public While_stmtContext while_stmt() {
			return getRuleContext(While_stmtContext.class,0);
		}
		public CntrolContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_cntrol; }
	}

	public final CntrolContext cntrol() throws RecognitionException {
		CntrolContext _localctx = new CntrolContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_cntrol);
		try {
			setState(188);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IF:
				enterOuterAlt(_localctx, 1);
				{
				setState(186);
				if_stmt();
				}
				break;
			case WHILE:
				enterOuterAlt(_localctx, 2);
				{
				setState(187);
				while_stmt();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class If_stmtContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(AlgoPractiseParser.IF, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public Else_stmtContext else_stmt() {
			return getRuleContext(Else_stmtContext.class,0);
		}
		public If_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_if_stmt; }
	}

	public final If_stmtContext if_stmt() throws RecognitionException {
		If_stmtContext _localctx = new If_stmtContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_if_stmt);
		try {
			setState(199);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,14,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(190);
				match(IF);
				setState(191);
				expr(0);
				setState(192);
				block();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(194);
				match(IF);
				setState(195);
				expr(0);
				setState(196);
				block();
				setState(197);
				else_stmt();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Else_stmtContext extends ParserRuleContext {
		public TerminalNode ELSE() { return getToken(AlgoPractiseParser.ELSE, 0); }
		public If_stmtContext if_stmt() {
			return getRuleContext(If_stmtContext.class,0);
		}
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public Else_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_else_stmt; }
	}

	public final Else_stmtContext else_stmt() throws RecognitionException {
		Else_stmtContext _localctx = new Else_stmtContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_else_stmt);
		try {
			setState(205);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,15,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(201);
				match(ELSE);
				setState(202);
				if_stmt();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(203);
				match(ELSE);
				setState(204);
				block();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class While_stmtContext extends ParserRuleContext {
		public TerminalNode WHILE() { return getToken(AlgoPractiseParser.WHILE, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public While_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_while_stmt; }
	}

	public final While_stmtContext while_stmt() throws RecognitionException {
		While_stmtContext _localctx = new While_stmtContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_while_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(207);
			match(WHILE);
			setState(208);
			expr(0);
			setState(209);
			block();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Func_callContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(AlgoPractiseParser.ID, 0); }
		public TerminalNode L_PAR() { return getToken(AlgoPractiseParser.L_PAR, 0); }
		public ListContext list() {
			return getRuleContext(ListContext.class,0);
		}
		public TerminalNode R_PAR() { return getToken(AlgoPractiseParser.R_PAR, 0); }
		public Func_callContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_func_call; }
	}

	public final Func_callContext func_call() throws RecognitionException {
		Func_callContext _localctx = new Func_callContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_func_call);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(211);
			match(ID);
			setState(212);
			match(L_PAR);
			setState(213);
			list();
			setState(214);
			match(R_PAR);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ListContext extends ParserRuleContext {
		public List<ValContext> val() {
			return getRuleContexts(ValContext.class);
		}
		public ValContext val(int i) {
			return getRuleContext(ValContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(AlgoPractiseParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(AlgoPractiseParser.COMMA, i);
		}
		public ListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_list; }
	}

	public final ListContext list() throws RecognitionException {
		ListContext _localctx = new ListContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(216);
			val();
			setState(221);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(217);
				match(COMMA);
				setState(218);
				val();
				}
				}
				setState(223);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 14:
			return expr_sempred((ExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 16);
		case 1:
			return precpred(_ctx, 15);
		case 2:
			return precpred(_ctx, 14);
		case 3:
			return precpred(_ctx, 13);
		case 4:
			return precpred(_ctx, 12);
		case 5:
			return precpred(_ctx, 11);
		case 6:
			return precpred(_ctx, 10);
		case 7:
			return precpred(_ctx, 9);
		case 8:
			return precpred(_ctx, 8);
		case 9:
			return precpred(_ctx, 7);
		case 10:
			return precpred(_ctx, 6);
		case 11:
			return precpred(_ctx, 5);
		case 12:
			return precpred(_ctx, 4);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3$\u00e3\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\3\2\3\2\7\2\61\n\2"+
		"\f\2\16\2\64\13\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3<\n\3\3\4\3\4\3\4\3\4\3\5"+
		"\3\5\3\6\3\6\3\6\3\6\5\6H\n\6\3\7\3\7\3\7\3\7\3\7\3\7\5\7P\n\7\3\b\3\b"+
		"\3\b\7\bU\n\b\f\b\16\bX\13\b\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13"+
		"\3\13\3\13\5\13f\n\13\3\f\3\f\3\f\3\f\5\fl\n\f\3\r\3\r\3\r\3\r\5\rr\n"+
		"\r\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3"+
		"\20\3\20\5\20\u0083\n\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20"+
		"\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20"+
		"\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20"+
		"\3\20\3\20\7\20\u00ac\n\20\f\20\16\20\u00af\13\20\3\21\3\21\3\21\3\21"+
		"\3\21\3\21\3\21\3\21\3\21\3\21\5\21\u00bb\n\21\3\22\3\22\5\22\u00bf\n"+
		"\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u00ca\n\23\3\24"+
		"\3\24\3\24\3\24\5\24\u00d0\n\24\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26"+
		"\3\26\3\27\3\27\3\27\7\27\u00de\n\27\f\27\16\27\u00e1\13\27\3\27\2\3\36"+
		"\30\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,\2\3\3\2\3\5\2\u00f0"+
		"\2\62\3\2\2\2\4;\3\2\2\2\6=\3\2\2\2\bA\3\2\2\2\nG\3\2\2\2\fO\3\2\2\2\16"+
		"Q\3\2\2\2\20Y\3\2\2\2\22\\\3\2\2\2\24e\3\2\2\2\26k\3\2\2\2\30q\3\2\2\2"+
		"\32s\3\2\2\2\34v\3\2\2\2\36\u0082\3\2\2\2 \u00ba\3\2\2\2\"\u00be\3\2\2"+
		"\2$\u00c9\3\2\2\2&\u00cf\3\2\2\2(\u00d1\3\2\2\2*\u00d5\3\2\2\2,\u00da"+
		"\3\2\2\2.\61\5\4\3\2/\61\5\26\f\2\60.\3\2\2\2\60/\3\2\2\2\61\64\3\2\2"+
		"\2\62\60\3\2\2\2\62\63\3\2\2\2\63\65\3\2\2\2\64\62\3\2\2\2\65\66\7\2\2"+
		"\3\66\3\3\2\2\2\678\5\b\5\289\5\6\4\29<\3\2\2\2:<\5\6\4\2;\67\3\2\2\2"+
		";:\3\2\2\2<\5\3\2\2\2=>\7\r\2\2>?\5\f\7\2?@\5\22\n\2@\7\3\2\2\2AB\t\2"+
		"\2\2B\t\3\2\2\2CH\5\b\5\2DE\5\b\5\2EF\7\16\2\2FH\3\2\2\2GC\3\2\2\2GD\3"+
		"\2\2\2H\13\3\2\2\2IJ\7\17\2\2JP\7\20\2\2KL\7\17\2\2LM\5\16\b\2MN\7\20"+
		"\2\2NP\3\2\2\2OI\3\2\2\2OK\3\2\2\2P\r\3\2\2\2QV\5\20\t\2RS\7#\2\2SU\5"+
		"\20\t\2TR\3\2\2\2UX\3\2\2\2VT\3\2\2\2VW\3\2\2\2W\17\3\2\2\2XV\3\2\2\2"+
		"YZ\5\b\5\2Z[\7\r\2\2[\21\3\2\2\2\\]\7\21\2\2]^\5\26\f\2^_\5\24\13\2_\23"+
		"\3\2\2\2`a\7\23\2\2ab\5 \21\2bc\7\22\2\2cf\3\2\2\2df\7\22\2\2e`\3\2\2"+
		"\2ed\3\2\2\2f\25\3\2\2\2gh\5\30\r\2hi\5\26\f\2il\3\2\2\2jl\5\30\r\2kg"+
		"\3\2\2\2kj\3\2\2\2l\27\3\2\2\2mr\5\32\16\2nr\5\34\17\2or\5\"\22\2pr\5"+
		"*\26\2qm\3\2\2\2qn\3\2\2\2qo\3\2\2\2qp\3\2\2\2r\31\3\2\2\2st\5\b\5\2t"+
		"u\5\34\17\2u\33\3\2\2\2vw\7\r\2\2wx\7\24\2\2xy\5\36\20\2y\35\3\2\2\2z"+
		"{\b\20\1\2{|\7\27\2\2|\u0083\5\36\20\5}\u0083\5 \21\2~\177\7\17\2\2\177"+
		"\u0080\5\36\20\2\u0080\u0081\7\20\2\2\u0081\u0083\3\2\2\2\u0082z\3\2\2"+
		"\2\u0082}\3\2\2\2\u0082~\3\2\2\2\u0083\u00ad\3\2\2\2\u0084\u0085\f\22"+
		"\2\2\u0085\u0086\7\f\2\2\u0086\u00ac\5\36\20\23\u0087\u0088\f\21\2\2\u0088"+
		"\u0089\7\13\2\2\u0089\u00ac\5\36\20\22\u008a\u008b\f\20\2\2\u008b\u008c"+
		"\7\30\2\2\u008c\u00ac\5\36\20\21\u008d\u008e\f\17\2\2\u008e\u008f\7\35"+
		"\2\2\u008f\u00ac\5\36\20\20\u0090\u0091\f\16\2\2\u0091\u0092\7\31\2\2"+
		"\u0092\u00ac\5\36\20\17\u0093\u0094\f\r\2\2\u0094\u0095\7\32\2\2\u0095"+
		"\u00ac\5\36\20\16\u0096\u0097\f\f\2\2\u0097\u0098\7\34\2\2\u0098\u00ac"+
		"\5\36\20\r\u0099\u009a\f\13\2\2\u009a\u009b\7\33\2\2\u009b\u00ac\5\36"+
		"\20\f\u009c\u009d\f\n\2\2\u009d\u009e\7\36\2\2\u009e\u00ac\5\36\20\13"+
		"\u009f\u00a0\f\t\2\2\u00a0\u00a1\7\37\2\2\u00a1\u00ac\5\36\20\n\u00a2"+
		"\u00a3\f\b\2\2\u00a3\u00a4\7 \2\2\u00a4\u00ac\5\36\20\t\u00a5\u00a6\f"+
		"\7\2\2\u00a6\u00a7\7!\2\2\u00a7\u00ac\5\36\20\b\u00a8\u00a9\f\6\2\2\u00a9"+
		"\u00aa\7\"\2\2\u00aa\u00ac\5\36\20\7\u00ab\u0084\3\2\2\2\u00ab\u0087\3"+
		"\2\2\2\u00ab\u008a\3\2\2\2\u00ab\u008d\3\2\2\2\u00ab\u0090\3\2\2\2\u00ab"+
		"\u0093\3\2\2\2\u00ab\u0096\3\2\2\2\u00ab\u0099\3\2\2\2\u00ab\u009c\3\2"+
		"\2\2\u00ab\u009f\3\2\2\2\u00ab\u00a2\3\2\2\2\u00ab\u00a5\3\2\2\2\u00ab"+
		"\u00a8\3\2\2\2\u00ac\u00af\3\2\2\2\u00ad\u00ab\3\2\2\2\u00ad\u00ae\3\2"+
		"\2\2\u00ae\37\3\2\2\2\u00af\u00ad\3\2\2\2\u00b0\u00bb\7\r\2\2\u00b1\u00bb"+
		"\7\25\2\2\u00b2\u00bb\7\26\2\2\u00b3\u00bb\7\6\2\2\u00b4\u00bb\7\7\2\2"+
		"\u00b5\u00b6\7\21\2\2\u00b6\u00b7\5,\27\2\u00b7\u00b8\7\22\2\2\u00b8\u00bb"+
		"\3\2\2\2\u00b9\u00bb\5*\26\2\u00ba\u00b0\3\2\2\2\u00ba\u00b1\3\2\2\2\u00ba"+
		"\u00b2\3\2\2\2\u00ba\u00b3\3\2\2\2\u00ba\u00b4\3\2\2\2\u00ba\u00b5\3\2"+
		"\2\2\u00ba\u00b9\3\2\2\2\u00bb!\3\2\2\2\u00bc\u00bf\5$\23\2\u00bd\u00bf"+
		"\5(\25\2\u00be\u00bc\3\2\2\2\u00be\u00bd\3\2\2\2\u00bf#\3\2\2\2\u00c0"+
		"\u00c1\7\b\2\2\u00c1\u00c2\5\36\20\2\u00c2\u00c3\5\22\n\2\u00c3\u00ca"+
		"\3\2\2\2\u00c4\u00c5\7\b\2\2\u00c5\u00c6\5\36\20\2\u00c6\u00c7\5\22\n"+
		"\2\u00c7\u00c8\5&\24\2\u00c8\u00ca\3\2\2\2\u00c9\u00c0\3\2\2\2\u00c9\u00c4"+
		"\3\2\2\2\u00ca%\3\2\2\2\u00cb\u00cc\7\t\2\2\u00cc\u00d0\5$\23\2\u00cd"+
		"\u00ce\7\t\2\2\u00ce\u00d0\5\22\n\2\u00cf\u00cb\3\2\2\2\u00cf\u00cd\3"+
		"\2\2\2\u00d0\'\3\2\2\2\u00d1\u00d2\7\n\2\2\u00d2\u00d3\5\36\20\2\u00d3"+
		"\u00d4\5\22\n\2\u00d4)\3\2\2\2\u00d5\u00d6\7\r\2\2\u00d6\u00d7\7\17\2"+
		"\2\u00d7\u00d8\5,\27\2\u00d8\u00d9\7\20\2\2\u00d9+\3\2\2\2\u00da\u00df"+
		"\5 \21\2\u00db\u00dc\7#\2\2\u00dc\u00de\5 \21\2\u00dd\u00db\3\2\2\2\u00de"+
		"\u00e1\3\2\2\2\u00df\u00dd\3\2\2\2\u00df\u00e0\3\2\2\2\u00e0-\3\2\2\2"+
		"\u00e1\u00df\3\2\2\2\23\60\62;GOVekq\u0082\u00ab\u00ad\u00ba\u00be\u00c9"+
		"\u00cf\u00df";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}