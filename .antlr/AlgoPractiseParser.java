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
		COMMA=33, WS=34, COMMENT=35;
	public static final int
		RULE_start = 0, RULE_func = 1, RULE_func_decl = 2, RULE_type = 3, RULE_params = 4, 
		RULE_param_lst = 5, RULE_param = 6, RULE_block = 7, RULE_endblock = 8, 
		RULE_stmts = 9, RULE_stmt = 10, RULE_dcl = 11, RULE_assign_stmt = 12, 
		RULE_expr = 13, RULE_val = 14, RULE_cntrol = 15, RULE_if_stmt = 16, RULE_else_stmt = 17, 
		RULE_while_stmt = 18, RULE_func_call = 19, RULE_list = 20;
	private static String[] makeRuleNames() {
		return new String[] {
			"start", "func", "func_decl", "type", "params", "param_lst", "param", 
			"block", "endblock", "stmts", "stmt", "dcl", "assign_stmt", "expr", "val", 
			"cntrol", "if_stmt", "else_stmt", "while_stmt", "func_call", "list"
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
			"COMMA", "WS", "COMMENT"
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
			setState(46);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << BOOL_TYPE) | (1L << STR_TYPE) | (1L << NUM_TYPE) | (1L << IF) | (1L << WHILE) | (1L << ID))) != 0)) {
				{
				setState(44);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
				case 1:
					{
					setState(42);
					func();
					}
					break;
				case 2:
					{
					setState(43);
					stmts();
					}
					break;
				}
				}
				setState(48);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(49);
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
			setState(55);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case BOOL_TYPE:
			case STR_TYPE:
			case NUM_TYPE:
				enterOuterAlt(_localctx, 1);
				{
				setState(51);
				type(0);
				setState(52);
				func_decl();
				}
				break;
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				setState(54);
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
			setState(57);
			match(ID);
			setState(58);
			params();
			setState(59);
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
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public TerminalNode LIST_DCL() { return getToken(AlgoPractiseParser.LIST_DCL, 0); }
		public TypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_type; }
	}

	public final TypeContext type() throws RecognitionException {
		return type(0);
	}

	private TypeContext type(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		TypeContext _localctx = new TypeContext(_ctx, _parentState);
		TypeContext _prevctx = _localctx;
		int _startState = 6;
		enterRecursionRule(_localctx, 6, RULE_type, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(65);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case BOOL_TYPE:
				{
				setState(62);
				match(BOOL_TYPE);
				}
				break;
			case STR_TYPE:
				{
				setState(63);
				match(STR_TYPE);
				}
				break;
			case NUM_TYPE:
				{
				setState(64);
				match(NUM_TYPE);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(71);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,4,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new TypeContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_type);
					setState(67);
					if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
					setState(68);
					match(LIST_DCL);
					}
					} 
				}
				setState(73);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,4,_ctx);
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
		enterRule(_localctx, 8, RULE_params);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(80);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
			case 1:
				{
				setState(74);
				match(L_PAR);
				setState(75);
				match(R_PAR);
				}
				break;
			case 2:
				{
				setState(76);
				match(L_PAR);
				setState(77);
				param_lst();
				setState(78);
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
		enterRule(_localctx, 10, RULE_param_lst);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(82);
			param();
			setState(87);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(83);
				match(COMMA);
				setState(84);
				param();
				}
				}
				setState(89);
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
		enterRule(_localctx, 12, RULE_param);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(90);
			type(0);
			setState(91);
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
		enterRule(_localctx, 14, RULE_block);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(93);
			match(L_CURLY);
			setState(94);
			stmts();
			setState(95);
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
		enterRule(_localctx, 16, RULE_endblock);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(102);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case RETURN:
				{
				setState(97);
				match(RETURN);
				setState(98);
				val();
				setState(99);
				match(R_CURLY);
				}
				break;
			case R_CURLY:
				{
				setState(101);
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
		enterRule(_localctx, 18, RULE_stmts);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(108);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				{
				setState(104);
				stmt();
				setState(105);
				stmts();
				}
				break;
			case 2:
				{
				setState(107);
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
		enterRule(_localctx, 20, RULE_stmt);
		try {
			setState(114);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(110);
				dcl();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(111);
				assign_stmt();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(112);
				cntrol();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(113);
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
		enterRule(_localctx, 22, RULE_dcl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(116);
			type(0);
			setState(117);
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
		enterRule(_localctx, 24, RULE_assign_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(119);
			match(ID);
			setState(120);
			match(ASSIGN);
			setState(121);
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
		int _startState = 26;
		enterRecursionRule(_localctx, 26, RULE_expr, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(131);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NEG:
				{
				setState(124);
				match(NEG);
				setState(125);
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
				setState(126);
				val();
				}
				break;
			case L_PAR:
				{
				setState(127);
				match(L_PAR);
				setState(128);
				expr(0);
				setState(129);
				match(R_PAR);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(174);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,12,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(172);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
					case 1:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(133);
						if (!(precpred(_ctx, 16))) throw new FailedPredicateException(this, "precpred(_ctx, 16)");
						setState(134);
						match(OR);
						setState(135);
						expr(17);
						}
						break;
					case 2:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(136);
						if (!(precpred(_ctx, 15))) throw new FailedPredicateException(this, "precpred(_ctx, 15)");
						setState(137);
						match(AND);
						setState(138);
						expr(16);
						}
						break;
					case 3:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(139);
						if (!(precpred(_ctx, 14))) throw new FailedPredicateException(this, "precpred(_ctx, 14)");
						setState(140);
						match(EQUAL);
						setState(141);
						expr(15);
						}
						break;
					case 4:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(142);
						if (!(precpred(_ctx, 13))) throw new FailedPredicateException(this, "precpred(_ctx, 13)");
						setState(143);
						match(NE);
						setState(144);
						expr(14);
						}
						break;
					case 5:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(145);
						if (!(precpred(_ctx, 12))) throw new FailedPredicateException(this, "precpred(_ctx, 12)");
						setState(146);
						match(LTE);
						setState(147);
						expr(13);
						}
						break;
					case 6:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(148);
						if (!(precpred(_ctx, 11))) throw new FailedPredicateException(this, "precpred(_ctx, 11)");
						setState(149);
						match(GTE);
						setState(150);
						expr(12);
						}
						break;
					case 7:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(151);
						if (!(precpred(_ctx, 10))) throw new FailedPredicateException(this, "precpred(_ctx, 10)");
						setState(152);
						match(GT);
						setState(153);
						expr(11);
						}
						break;
					case 8:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(154);
						if (!(precpred(_ctx, 9))) throw new FailedPredicateException(this, "precpred(_ctx, 9)");
						setState(155);
						match(LT);
						setState(156);
						expr(10);
						}
						break;
					case 9:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(157);
						if (!(precpred(_ctx, 8))) throw new FailedPredicateException(this, "precpred(_ctx, 8)");
						setState(158);
						match(PLUS);
						setState(159);
						expr(9);
						}
						break;
					case 10:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(160);
						if (!(precpred(_ctx, 7))) throw new FailedPredicateException(this, "precpred(_ctx, 7)");
						setState(161);
						match(MINUS);
						setState(162);
						expr(8);
						}
						break;
					case 11:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(163);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(164);
						match(MULT);
						setState(165);
						expr(7);
						}
						break;
					case 12:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(166);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(167);
						match(DIV);
						setState(168);
						expr(6);
						}
						break;
					case 13:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(169);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(170);
						match(MOD);
						setState(171);
						expr(5);
						}
						break;
					}
					} 
				}
				setState(176);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,12,_ctx);
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
		enterRule(_localctx, 28, RULE_val);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(187);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,13,_ctx) ) {
			case 1:
				{
				setState(177);
				match(ID);
				}
				break;
			case 2:
				{
				setState(178);
				match(NUMVAL);
				}
				break;
			case 3:
				{
				setState(179);
				match(STRINGVAL);
				}
				break;
			case 4:
				{
				setState(180);
				match(TRUE);
				}
				break;
			case 5:
				{
				setState(181);
				match(FALSE);
				}
				break;
			case 6:
				{
				setState(182);
				match(L_CURLY);
				setState(183);
				list();
				setState(184);
				match(R_CURLY);
				}
				break;
			case 7:
				{
				setState(186);
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
		enterRule(_localctx, 30, RULE_cntrol);
		try {
			setState(191);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IF:
				enterOuterAlt(_localctx, 1);
				{
				setState(189);
				if_stmt();
				}
				break;
			case WHILE:
				enterOuterAlt(_localctx, 2);
				{
				setState(190);
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
		enterRule(_localctx, 32, RULE_if_stmt);
		try {
			setState(202);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,15,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(193);
				match(IF);
				setState(194);
				expr(0);
				setState(195);
				block();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(197);
				match(IF);
				setState(198);
				expr(0);
				setState(199);
				block();
				setState(200);
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
		enterRule(_localctx, 34, RULE_else_stmt);
		try {
			setState(208);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,16,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(204);
				match(ELSE);
				setState(205);
				if_stmt();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(206);
				match(ELSE);
				setState(207);
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
		enterRule(_localctx, 36, RULE_while_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(210);
			match(WHILE);
			setState(211);
			expr(0);
			setState(212);
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
		enterRule(_localctx, 38, RULE_func_call);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(214);
			match(ID);
			setState(215);
			match(L_PAR);
			setState(216);
			list();
			setState(217);
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
		enterRule(_localctx, 40, RULE_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(219);
			val();
			setState(224);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(220);
				match(COMMA);
				setState(221);
				val();
				}
				}
				setState(226);
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
		case 3:
			return type_sempred((TypeContext)_localctx, predIndex);
		case 13:
			return expr_sempred((ExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean type_sempred(TypeContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 1);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 1:
			return precpred(_ctx, 16);
		case 2:
			return precpred(_ctx, 15);
		case 3:
			return precpred(_ctx, 14);
		case 4:
			return precpred(_ctx, 13);
		case 5:
			return precpred(_ctx, 12);
		case 6:
			return precpred(_ctx, 11);
		case 7:
			return precpred(_ctx, 10);
		case 8:
			return precpred(_ctx, 9);
		case 9:
			return precpred(_ctx, 8);
		case 10:
			return precpred(_ctx, 7);
		case 11:
			return precpred(_ctx, 6);
		case 12:
			return precpred(_ctx, 5);
		case 13:
			return precpred(_ctx, 4);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3%\u00e6\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\3\2\3\2\7\2/\n\2\f\2\16\2\62"+
		"\13\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3:\n\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5"+
		"\5\5D\n\5\3\5\3\5\7\5H\n\5\f\5\16\5K\13\5\3\6\3\6\3\6\3\6\3\6\3\6\5\6"+
		"S\n\6\3\7\3\7\3\7\7\7X\n\7\f\7\16\7[\13\7\3\b\3\b\3\b\3\t\3\t\3\t\3\t"+
		"\3\n\3\n\3\n\3\n\3\n\5\ni\n\n\3\13\3\13\3\13\3\13\5\13o\n\13\3\f\3\f\3"+
		"\f\3\f\5\fu\n\f\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3"+
		"\17\3\17\3\17\3\17\5\17\u0086\n\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17"+
		"\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17"+
		"\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17"+
		"\3\17\3\17\3\17\3\17\7\17\u00af\n\17\f\17\16\17\u00b2\13\17\3\20\3\20"+
		"\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\5\20\u00be\n\20\3\21\3\21\5\21"+
		"\u00c2\n\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\5\22\u00cd\n"+
		"\22\3\23\3\23\3\23\3\23\5\23\u00d3\n\23\3\24\3\24\3\24\3\24\3\25\3\25"+
		"\3\25\3\25\3\25\3\26\3\26\3\26\7\26\u00e1\n\26\f\26\16\26\u00e4\13\26"+
		"\3\26\2\4\b\34\27\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*\2\2\2"+
		"\u00f6\2\60\3\2\2\2\49\3\2\2\2\6;\3\2\2\2\bC\3\2\2\2\nR\3\2\2\2\fT\3\2"+
		"\2\2\16\\\3\2\2\2\20_\3\2\2\2\22h\3\2\2\2\24n\3\2\2\2\26t\3\2\2\2\30v"+
		"\3\2\2\2\32y\3\2\2\2\34\u0085\3\2\2\2\36\u00bd\3\2\2\2 \u00c1\3\2\2\2"+
		"\"\u00cc\3\2\2\2$\u00d2\3\2\2\2&\u00d4\3\2\2\2(\u00d8\3\2\2\2*\u00dd\3"+
		"\2\2\2,/\5\4\3\2-/\5\24\13\2.,\3\2\2\2.-\3\2\2\2/\62\3\2\2\2\60.\3\2\2"+
		"\2\60\61\3\2\2\2\61\63\3\2\2\2\62\60\3\2\2\2\63\64\7\2\2\3\64\3\3\2\2"+
		"\2\65\66\5\b\5\2\66\67\5\6\4\2\67:\3\2\2\28:\5\6\4\29\65\3\2\2\298\3\2"+
		"\2\2:\5\3\2\2\2;<\7\r\2\2<=\5\n\6\2=>\5\20\t\2>\7\3\2\2\2?@\b\5\1\2@D"+
		"\7\3\2\2AD\7\4\2\2BD\7\5\2\2C?\3\2\2\2CA\3\2\2\2CB\3\2\2\2DI\3\2\2\2E"+
		"F\f\3\2\2FH\7\16\2\2GE\3\2\2\2HK\3\2\2\2IG\3\2\2\2IJ\3\2\2\2J\t\3\2\2"+
		"\2KI\3\2\2\2LM\7\17\2\2MS\7\20\2\2NO\7\17\2\2OP\5\f\7\2PQ\7\20\2\2QS\3"+
		"\2\2\2RL\3\2\2\2RN\3\2\2\2S\13\3\2\2\2TY\5\16\b\2UV\7#\2\2VX\5\16\b\2"+
		"WU\3\2\2\2X[\3\2\2\2YW\3\2\2\2YZ\3\2\2\2Z\r\3\2\2\2[Y\3\2\2\2\\]\5\b\5"+
		"\2]^\7\r\2\2^\17\3\2\2\2_`\7\21\2\2`a\5\24\13\2ab\5\22\n\2b\21\3\2\2\2"+
		"cd\7\23\2\2de\5\36\20\2ef\7\22\2\2fi\3\2\2\2gi\7\22\2\2hc\3\2\2\2hg\3"+
		"\2\2\2i\23\3\2\2\2jk\5\26\f\2kl\5\24\13\2lo\3\2\2\2mo\5\26\f\2nj\3\2\2"+
		"\2nm\3\2\2\2o\25\3\2\2\2pu\5\30\r\2qu\5\32\16\2ru\5 \21\2su\5(\25\2tp"+
		"\3\2\2\2tq\3\2\2\2tr\3\2\2\2ts\3\2\2\2u\27\3\2\2\2vw\5\b\5\2wx\5\32\16"+
		"\2x\31\3\2\2\2yz\7\r\2\2z{\7\24\2\2{|\5\34\17\2|\33\3\2\2\2}~\b\17\1\2"+
		"~\177\7\27\2\2\177\u0086\5\34\17\5\u0080\u0086\5\36\20\2\u0081\u0082\7"+
		"\17\2\2\u0082\u0083\5\34\17\2\u0083\u0084\7\20\2\2\u0084\u0086\3\2\2\2"+
		"\u0085}\3\2\2\2\u0085\u0080\3\2\2\2\u0085\u0081\3\2\2\2\u0086\u00b0\3"+
		"\2\2\2\u0087\u0088\f\22\2\2\u0088\u0089\7\f\2\2\u0089\u00af\5\34\17\23"+
		"\u008a\u008b\f\21\2\2\u008b\u008c\7\13\2\2\u008c\u00af\5\34\17\22\u008d"+
		"\u008e\f\20\2\2\u008e\u008f\7\30\2\2\u008f\u00af\5\34\17\21\u0090\u0091"+
		"\f\17\2\2\u0091\u0092\7\35\2\2\u0092\u00af\5\34\17\20\u0093\u0094\f\16"+
		"\2\2\u0094\u0095\7\31\2\2\u0095\u00af\5\34\17\17\u0096\u0097\f\r\2\2\u0097"+
		"\u0098\7\32\2\2\u0098\u00af\5\34\17\16\u0099\u009a\f\f\2\2\u009a\u009b"+
		"\7\34\2\2\u009b\u00af\5\34\17\r\u009c\u009d\f\13\2\2\u009d\u009e\7\33"+
		"\2\2\u009e\u00af\5\34\17\f\u009f\u00a0\f\n\2\2\u00a0\u00a1\7\36\2\2\u00a1"+
		"\u00af\5\34\17\13\u00a2\u00a3\f\t\2\2\u00a3\u00a4\7\37\2\2\u00a4\u00af"+
		"\5\34\17\n\u00a5\u00a6\f\b\2\2\u00a6\u00a7\7 \2\2\u00a7\u00af\5\34\17"+
		"\t\u00a8\u00a9\f\7\2\2\u00a9\u00aa\7!\2\2\u00aa\u00af\5\34\17\b\u00ab"+
		"\u00ac\f\6\2\2\u00ac\u00ad\7\"\2\2\u00ad\u00af\5\34\17\7\u00ae\u0087\3"+
		"\2\2\2\u00ae\u008a\3\2\2\2\u00ae\u008d\3\2\2\2\u00ae\u0090\3\2\2\2\u00ae"+
		"\u0093\3\2\2\2\u00ae\u0096\3\2\2\2\u00ae\u0099\3\2\2\2\u00ae\u009c\3\2"+
		"\2\2\u00ae\u009f\3\2\2\2\u00ae\u00a2\3\2\2\2\u00ae\u00a5\3\2\2\2\u00ae"+
		"\u00a8\3\2\2\2\u00ae\u00ab\3\2\2\2\u00af\u00b2\3\2\2\2\u00b0\u00ae\3\2"+
		"\2\2\u00b0\u00b1\3\2\2\2\u00b1\35\3\2\2\2\u00b2\u00b0\3\2\2\2\u00b3\u00be"+
		"\7\r\2\2\u00b4\u00be\7\25\2\2\u00b5\u00be\7\26\2\2\u00b6\u00be\7\6\2\2"+
		"\u00b7\u00be\7\7\2\2\u00b8\u00b9\7\21\2\2\u00b9\u00ba\5*\26\2\u00ba\u00bb"+
		"\7\22\2\2\u00bb\u00be\3\2\2\2\u00bc\u00be\5(\25\2\u00bd\u00b3\3\2\2\2"+
		"\u00bd\u00b4\3\2\2\2\u00bd\u00b5\3\2\2\2\u00bd\u00b6\3\2\2\2\u00bd\u00b7"+
		"\3\2\2\2\u00bd\u00b8\3\2\2\2\u00bd\u00bc\3\2\2\2\u00be\37\3\2\2\2\u00bf"+
		"\u00c2\5\"\22\2\u00c0\u00c2\5&\24\2\u00c1\u00bf\3\2\2\2\u00c1\u00c0\3"+
		"\2\2\2\u00c2!\3\2\2\2\u00c3\u00c4\7\b\2\2\u00c4\u00c5\5\34\17\2\u00c5"+
		"\u00c6\5\20\t\2\u00c6\u00cd\3\2\2\2\u00c7\u00c8\7\b\2\2\u00c8\u00c9\5"+
		"\34\17\2\u00c9\u00ca\5\20\t\2\u00ca\u00cb\5$\23\2\u00cb\u00cd\3\2\2\2"+
		"\u00cc\u00c3\3\2\2\2\u00cc\u00c7\3\2\2\2\u00cd#\3\2\2\2\u00ce\u00cf\7"+
		"\t\2\2\u00cf\u00d3\5\"\22\2\u00d0\u00d1\7\t\2\2\u00d1\u00d3\5\20\t\2\u00d2"+
		"\u00ce\3\2\2\2\u00d2\u00d0\3\2\2\2\u00d3%\3\2\2\2\u00d4\u00d5\7\n\2\2"+
		"\u00d5\u00d6\5\34\17\2\u00d6\u00d7\5\20\t\2\u00d7\'\3\2\2\2\u00d8\u00d9"+
		"\7\r\2\2\u00d9\u00da\7\17\2\2\u00da\u00db\5*\26\2\u00db\u00dc\7\20\2\2"+
		"\u00dc)\3\2\2\2\u00dd\u00e2\5\36\20\2\u00de\u00df\7#\2\2\u00df\u00e1\5"+
		"\36\20\2\u00e0\u00de\3\2\2\2\u00e1\u00e4\3\2\2\2\u00e2\u00e0\3\2\2\2\u00e2"+
		"\u00e3\3\2\2\2\u00e3+\3\2\2\2\u00e4\u00e2\3\2\2\2\24.\609CIRYhnt\u0085"+
		"\u00ae\u00b0\u00bd\u00c1\u00cc\u00d2\u00e2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}