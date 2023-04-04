// Generated from d:\OneDrive\projects\GitHub\p4-group-project\ANTLR\AlgoPractise.g4 by ANTLR 4.9.2
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
		RULE_cond = 14, RULE_expr = 15, RULE_val = 16, RULE_cntrol = 17, RULE_if_stmt = 18, 
		RULE_else_stmt = 19, RULE_while_stmt = 20, RULE_func_call = 21, RULE_list = 22;
	private static String[] makeRuleNames() {
		return new String[] {
			"start", "func", "func_decl", "type", "type_decl", "params", "param_lst", 
			"param", "block", "endblock", "stmts", "stmt", "dcl", "assign_stmt", 
			"cond", "expr", "val", "cntrol", "if_stmt", "else_stmt", "while_stmt", 
			"func_call", "list"
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
		public List<StmtContext> stmt() {
			return getRuleContexts(StmtContext.class);
		}
		public StmtContext stmt(int i) {
			return getRuleContext(StmtContext.class,i);
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
			setState(51);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << BOOL_TYPE) | (1L << STR_TYPE) | (1L << NUM_TYPE) | (1L << IF) | (1L << WHILE) | (1L << ID))) != 0)) {
				{
				setState(49);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
				case 1:
					{
					setState(46);
					func();
					}
					break;
				case 2:
					{
					setState(47);
					stmts();
					}
					break;
				case 3:
					{
					setState(48);
					stmt();
					}
					break;
				}
				}
				setState(53);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(54);
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
			setState(60);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case BOOL_TYPE:
			case STR_TYPE:
			case NUM_TYPE:
				enterOuterAlt(_localctx, 1);
				{
				setState(56);
				type();
				setState(57);
				func_decl();
				}
				break;
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				setState(59);
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
			setState(62);
			match(ID);
			setState(63);
			params();
			setState(64);
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
			setState(66);
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
			setState(72);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(68);
				type();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(69);
				type();
				setState(70);
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
			setState(80);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
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
		enterRule(_localctx, 12, RULE_param_lst);
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
		enterRule(_localctx, 14, RULE_param);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(90);
			type();
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
		enterRule(_localctx, 16, RULE_block);
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
		enterRule(_localctx, 18, RULE_endblock);
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
		enterRule(_localctx, 20, RULE_stmts);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(108);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
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
		enterRule(_localctx, 22, RULE_stmt);
		try {
			setState(114);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
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
		enterRule(_localctx, 24, RULE_dcl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(116);
			type();
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
		public CondContext cond() {
			return getRuleContext(CondContext.class,0);
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
			setState(119);
			match(ID);
			setState(120);
			match(ASSIGN);
			setState(121);
			cond(0);
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

	public static class CondContext extends ParserRuleContext {
		public TerminalNode NEG() { return getToken(AlgoPractiseParser.NEG, 0); }
		public List<CondContext> cond() {
			return getRuleContexts(CondContext.class);
		}
		public CondContext cond(int i) {
			return getRuleContext(CondContext.class,i);
		}
		public TerminalNode L_PAR() { return getToken(AlgoPractiseParser.L_PAR, 0); }
		public TerminalNode R_PAR() { return getToken(AlgoPractiseParser.R_PAR, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode OR() { return getToken(AlgoPractiseParser.OR, 0); }
		public TerminalNode AND() { return getToken(AlgoPractiseParser.AND, 0); }
		public TerminalNode EQUAL() { return getToken(AlgoPractiseParser.EQUAL, 0); }
		public TerminalNode NE() { return getToken(AlgoPractiseParser.NE, 0); }
		public TerminalNode LTE() { return getToken(AlgoPractiseParser.LTE, 0); }
		public TerminalNode GTE() { return getToken(AlgoPractiseParser.GTE, 0); }
		public TerminalNode GT() { return getToken(AlgoPractiseParser.GT, 0); }
		public TerminalNode LT() { return getToken(AlgoPractiseParser.LT, 0); }
		public CondContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_cond; }
	}

	public final CondContext cond() throws RecognitionException {
		return cond(0);
	}

	private CondContext cond(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		CondContext _localctx = new CondContext(_ctx, _parentState);
		CondContext _prevctx = _localctx;
		int _startState = 28;
		enterRecursionRule(_localctx, 28, RULE_cond, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(131);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
			case 1:
				{
				setState(124);
				match(NEG);
				setState(125);
				cond(3);
				}
				break;
			case 2:
				{
				setState(126);
				match(L_PAR);
				setState(127);
				cond(0);
				setState(128);
				match(R_PAR);
				}
				break;
			case 3:
				{
				setState(130);
				expr(0);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(159);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,11,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(157);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,10,_ctx) ) {
					case 1:
						{
						_localctx = new CondContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_cond);
						setState(133);
						if (!(precpred(_ctx, 11))) throw new FailedPredicateException(this, "precpred(_ctx, 11)");
						setState(134);
						match(OR);
						setState(135);
						cond(12);
						}
						break;
					case 2:
						{
						_localctx = new CondContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_cond);
						setState(136);
						if (!(precpred(_ctx, 10))) throw new FailedPredicateException(this, "precpred(_ctx, 10)");
						setState(137);
						match(AND);
						setState(138);
						cond(11);
						}
						break;
					case 3:
						{
						_localctx = new CondContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_cond);
						setState(139);
						if (!(precpred(_ctx, 9))) throw new FailedPredicateException(this, "precpred(_ctx, 9)");
						setState(140);
						match(EQUAL);
						setState(141);
						cond(10);
						}
						break;
					case 4:
						{
						_localctx = new CondContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_cond);
						setState(142);
						if (!(precpred(_ctx, 8))) throw new FailedPredicateException(this, "precpred(_ctx, 8)");
						setState(143);
						match(NE);
						setState(144);
						cond(9);
						}
						break;
					case 5:
						{
						_localctx = new CondContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_cond);
						setState(145);
						if (!(precpred(_ctx, 7))) throw new FailedPredicateException(this, "precpred(_ctx, 7)");
						setState(146);
						match(LTE);
						setState(147);
						cond(8);
						}
						break;
					case 6:
						{
						_localctx = new CondContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_cond);
						setState(148);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(149);
						match(GTE);
						setState(150);
						cond(7);
						}
						break;
					case 7:
						{
						_localctx = new CondContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_cond);
						setState(151);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(152);
						match(GT);
						setState(153);
						cond(6);
						}
						break;
					case 8:
						{
						_localctx = new CondContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_cond);
						setState(154);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(155);
						match(LT);
						setState(156);
						cond(5);
						}
						break;
					}
					} 
				}
				setState(161);
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

	public static class ExprContext extends ParserRuleContext {
		public ValContext val() {
			return getRuleContext(ValContext.class,0);
		}
		public TerminalNode L_PAR() { return getToken(AlgoPractiseParser.L_PAR, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode R_PAR() { return getToken(AlgoPractiseParser.R_PAR, 0); }
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
		int _startState = 30;
		enterRecursionRule(_localctx, 30, RULE_expr, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(168);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case TRUE:
			case FALSE:
			case ID:
			case L_CURLY:
			case NUMVAL:
			case STRINGVAL:
				{
				setState(163);
				val();
				}
				break;
			case L_PAR:
				{
				setState(164);
				match(L_PAR);
				setState(165);
				expr(0);
				setState(166);
				match(R_PAR);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(187);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,14,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(185);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,13,_ctx) ) {
					case 1:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(170);
						if (!(precpred(_ctx, 7))) throw new FailedPredicateException(this, "precpred(_ctx, 7)");
						setState(171);
						match(PLUS);
						setState(172);
						expr(8);
						}
						break;
					case 2:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(173);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(174);
						match(MINUS);
						setState(175);
						expr(7);
						}
						break;
					case 3:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(176);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(177);
						match(MULT);
						setState(178);
						expr(6);
						}
						break;
					case 4:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(179);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(180);
						match(DIV);
						setState(181);
						expr(5);
						}
						break;
					case 5:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(182);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(183);
						match(MOD);
						setState(184);
						expr(4);
						}
						break;
					}
					} 
				}
				setState(189);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,14,_ctx);
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
		enterRule(_localctx, 32, RULE_val);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(200);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,15,_ctx) ) {
			case 1:
				{
				setState(190);
				match(ID);
				}
				break;
			case 2:
				{
				setState(191);
				match(NUMVAL);
				}
				break;
			case 3:
				{
				setState(192);
				match(STRINGVAL);
				}
				break;
			case 4:
				{
				setState(193);
				match(TRUE);
				}
				break;
			case 5:
				{
				setState(194);
				match(FALSE);
				}
				break;
			case 6:
				{
				setState(195);
				match(L_CURLY);
				setState(196);
				list();
				setState(197);
				match(R_CURLY);
				}
				break;
			case 7:
				{
				setState(199);
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
		enterRule(_localctx, 34, RULE_cntrol);
		try {
			setState(204);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IF:
				enterOuterAlt(_localctx, 1);
				{
				setState(202);
				if_stmt();
				}
				break;
			case WHILE:
				enterOuterAlt(_localctx, 2);
				{
				setState(203);
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
		public CondContext cond() {
			return getRuleContext(CondContext.class,0);
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
		enterRule(_localctx, 36, RULE_if_stmt);
		try {
			setState(215);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,17,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(206);
				match(IF);
				setState(207);
				cond(0);
				setState(208);
				block();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(210);
				match(IF);
				setState(211);
				cond(0);
				setState(212);
				block();
				setState(213);
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
		enterRule(_localctx, 38, RULE_else_stmt);
		try {
			setState(221);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,18,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(217);
				match(ELSE);
				setState(218);
				if_stmt();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(219);
				match(ELSE);
				setState(220);
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
		public CondContext cond() {
			return getRuleContext(CondContext.class,0);
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
		enterRule(_localctx, 40, RULE_while_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(223);
			match(WHILE);
			setState(224);
			cond(0);
			setState(225);
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
		enterRule(_localctx, 42, RULE_func_call);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(227);
			match(ID);
			setState(228);
			match(L_PAR);
			setState(229);
			list();
			setState(230);
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
		enterRule(_localctx, 44, RULE_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(232);
			val();
			setState(237);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(233);
				match(COMMA);
				setState(234);
				val();
				}
				}
				setState(239);
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
			return cond_sempred((CondContext)_localctx, predIndex);
		case 15:
			return expr_sempred((ExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean cond_sempred(CondContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 11);
		case 1:
			return precpred(_ctx, 10);
		case 2:
			return precpred(_ctx, 9);
		case 3:
			return precpred(_ctx, 8);
		case 4:
			return precpred(_ctx, 7);
		case 5:
			return precpred(_ctx, 6);
		case 6:
			return precpred(_ctx, 5);
		case 7:
			return precpred(_ctx, 4);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 8:
			return precpred(_ctx, 7);
		case 9:
			return precpred(_ctx, 6);
		case 10:
			return precpred(_ctx, 5);
		case 11:
			return precpred(_ctx, 4);
		case 12:
			return precpred(_ctx, 3);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3$\u00f3\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\3\2\3\2\3"+
		"\2\7\2\64\n\2\f\2\16\2\67\13\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3?\n\3\3\4\3"+
		"\4\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3\6\5\6K\n\6\3\7\3\7\3\7\3\7\3\7\3\7\5"+
		"\7S\n\7\3\b\3\b\3\b\7\bX\n\b\f\b\16\b[\13\b\3\t\3\t\3\t\3\n\3\n\3\n\3"+
		"\n\3\13\3\13\3\13\3\13\3\13\5\13i\n\13\3\f\3\f\3\f\3\f\5\fo\n\f\3\r\3"+
		"\r\3\r\3\r\5\ru\n\r\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\20\3\20\3\20"+
		"\3\20\3\20\3\20\3\20\3\20\5\20\u0086\n\20\3\20\3\20\3\20\3\20\3\20\3\20"+
		"\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20"+
		"\3\20\3\20\3\20\3\20\7\20\u00a0\n\20\f\20\16\20\u00a3\13\20\3\21\3\21"+
		"\3\21\3\21\3\21\3\21\5\21\u00ab\n\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21"+
		"\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\7\21\u00bc\n\21\f\21\16\21\u00bf"+
		"\13\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\5\22\u00cb\n"+
		"\22\3\23\3\23\5\23\u00cf\n\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24"+
		"\3\24\5\24\u00da\n\24\3\25\3\25\3\25\3\25\5\25\u00e0\n\25\3\26\3\26\3"+
		"\26\3\26\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\7\30\u00ee\n\30\f\30"+
		"\16\30\u00f1\13\30\3\30\2\4\36 \31\2\4\6\b\n\f\16\20\22\24\26\30\32\34"+
		"\36 \"$&(*,.\2\3\3\2\3\5\2\u0101\2\65\3\2\2\2\4>\3\2\2\2\6@\3\2\2\2\b"+
		"D\3\2\2\2\nJ\3\2\2\2\fR\3\2\2\2\16T\3\2\2\2\20\\\3\2\2\2\22_\3\2\2\2\24"+
		"h\3\2\2\2\26n\3\2\2\2\30t\3\2\2\2\32v\3\2\2\2\34y\3\2\2\2\36\u0085\3\2"+
		"\2\2 \u00aa\3\2\2\2\"\u00ca\3\2\2\2$\u00ce\3\2\2\2&\u00d9\3\2\2\2(\u00df"+
		"\3\2\2\2*\u00e1\3\2\2\2,\u00e5\3\2\2\2.\u00ea\3\2\2\2\60\64\5\4\3\2\61"+
		"\64\5\26\f\2\62\64\5\30\r\2\63\60\3\2\2\2\63\61\3\2\2\2\63\62\3\2\2\2"+
		"\64\67\3\2\2\2\65\63\3\2\2\2\65\66\3\2\2\2\668\3\2\2\2\67\65\3\2\2\28"+
		"9\7\2\2\39\3\3\2\2\2:;\5\b\5\2;<\5\6\4\2<?\3\2\2\2=?\5\6\4\2>:\3\2\2\2"+
		">=\3\2\2\2?\5\3\2\2\2@A\7\r\2\2AB\5\f\7\2BC\5\22\n\2C\7\3\2\2\2DE\t\2"+
		"\2\2E\t\3\2\2\2FK\5\b\5\2GH\5\b\5\2HI\7\16\2\2IK\3\2\2\2JF\3\2\2\2JG\3"+
		"\2\2\2K\13\3\2\2\2LM\7\17\2\2MS\7\20\2\2NO\7\17\2\2OP\5\16\b\2PQ\7\20"+
		"\2\2QS\3\2\2\2RL\3\2\2\2RN\3\2\2\2S\r\3\2\2\2TY\5\20\t\2UV\7#\2\2VX\5"+
		"\20\t\2WU\3\2\2\2X[\3\2\2\2YW\3\2\2\2YZ\3\2\2\2Z\17\3\2\2\2[Y\3\2\2\2"+
		"\\]\5\b\5\2]^\7\r\2\2^\21\3\2\2\2_`\7\21\2\2`a\5\26\f\2ab\5\24\13\2b\23"+
		"\3\2\2\2cd\7\23\2\2de\5\"\22\2ef\7\22\2\2fi\3\2\2\2gi\7\22\2\2hc\3\2\2"+
		"\2hg\3\2\2\2i\25\3\2\2\2jk\5\30\r\2kl\5\26\f\2lo\3\2\2\2mo\5\30\r\2nj"+
		"\3\2\2\2nm\3\2\2\2o\27\3\2\2\2pu\5\32\16\2qu\5\34\17\2ru\5$\23\2su\5,"+
		"\27\2tp\3\2\2\2tq\3\2\2\2tr\3\2\2\2ts\3\2\2\2u\31\3\2\2\2vw\5\b\5\2wx"+
		"\5\34\17\2x\33\3\2\2\2yz\7\r\2\2z{\7\24\2\2{|\5\36\20\2|\35\3\2\2\2}~"+
		"\b\20\1\2~\177\7\27\2\2\177\u0086\5\36\20\5\u0080\u0081\7\17\2\2\u0081"+
		"\u0082\5\36\20\2\u0082\u0083\7\20\2\2\u0083\u0086\3\2\2\2\u0084\u0086"+
		"\5 \21\2\u0085}\3\2\2\2\u0085\u0080\3\2\2\2\u0085\u0084\3\2\2\2\u0086"+
		"\u00a1\3\2\2\2\u0087\u0088\f\r\2\2\u0088\u0089\7\f\2\2\u0089\u00a0\5\36"+
		"\20\16\u008a\u008b\f\f\2\2\u008b\u008c\7\13\2\2\u008c\u00a0\5\36\20\r"+
		"\u008d\u008e\f\13\2\2\u008e\u008f\7\30\2\2\u008f\u00a0\5\36\20\f\u0090"+
		"\u0091\f\n\2\2\u0091\u0092\7\35\2\2\u0092\u00a0\5\36\20\13\u0093\u0094"+
		"\f\t\2\2\u0094\u0095\7\31\2\2\u0095\u00a0\5\36\20\n\u0096\u0097\f\b\2"+
		"\2\u0097\u0098\7\32\2\2\u0098\u00a0\5\36\20\t\u0099\u009a\f\7\2\2\u009a"+
		"\u009b\7\34\2\2\u009b\u00a0\5\36\20\b\u009c\u009d\f\6\2\2\u009d\u009e"+
		"\7\33\2\2\u009e\u00a0\5\36\20\7\u009f\u0087\3\2\2\2\u009f\u008a\3\2\2"+
		"\2\u009f\u008d\3\2\2\2\u009f\u0090\3\2\2\2\u009f\u0093\3\2\2\2\u009f\u0096"+
		"\3\2\2\2\u009f\u0099\3\2\2\2\u009f\u009c\3\2\2\2\u00a0\u00a3\3\2\2\2\u00a1"+
		"\u009f\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\37\3\2\2\2\u00a3\u00a1\3\2\2"+
		"\2\u00a4\u00a5\b\21\1\2\u00a5\u00ab\5\"\22\2\u00a6\u00a7\7\17\2\2\u00a7"+
		"\u00a8\5 \21\2\u00a8\u00a9\7\20\2\2\u00a9\u00ab\3\2\2\2\u00aa\u00a4\3"+
		"\2\2\2\u00aa\u00a6\3\2\2\2\u00ab\u00bd\3\2\2\2\u00ac\u00ad\f\t\2\2\u00ad"+
		"\u00ae\7\36\2\2\u00ae\u00bc\5 \21\n\u00af\u00b0\f\b\2\2\u00b0\u00b1\7"+
		"\37\2\2\u00b1\u00bc\5 \21\t\u00b2\u00b3\f\7\2\2\u00b3\u00b4\7 \2\2\u00b4"+
		"\u00bc\5 \21\b\u00b5\u00b6\f\6\2\2\u00b6\u00b7\7!\2\2\u00b7\u00bc\5 \21"+
		"\7\u00b8\u00b9\f\5\2\2\u00b9\u00ba\7\"\2\2\u00ba\u00bc\5 \21\6\u00bb\u00ac"+
		"\3\2\2\2\u00bb\u00af\3\2\2\2\u00bb\u00b2\3\2\2\2\u00bb\u00b5\3\2\2\2\u00bb"+
		"\u00b8\3\2\2\2\u00bc\u00bf\3\2\2\2\u00bd\u00bb\3\2\2\2\u00bd\u00be\3\2"+
		"\2\2\u00be!\3\2\2\2\u00bf\u00bd\3\2\2\2\u00c0\u00cb\7\r\2\2\u00c1\u00cb"+
		"\7\25\2\2\u00c2\u00cb\7\26\2\2\u00c3\u00cb\7\6\2\2\u00c4\u00cb\7\7\2\2"+
		"\u00c5\u00c6\7\21\2\2\u00c6\u00c7\5.\30\2\u00c7\u00c8\7\22\2\2\u00c8\u00cb"+
		"\3\2\2\2\u00c9\u00cb\5,\27\2\u00ca\u00c0\3\2\2\2\u00ca\u00c1\3\2\2\2\u00ca"+
		"\u00c2\3\2\2\2\u00ca\u00c3\3\2\2\2\u00ca\u00c4\3\2\2\2\u00ca\u00c5\3\2"+
		"\2\2\u00ca\u00c9\3\2\2\2\u00cb#\3\2\2\2\u00cc\u00cf\5&\24\2\u00cd\u00cf"+
		"\5*\26\2\u00ce\u00cc\3\2\2\2\u00ce\u00cd\3\2\2\2\u00cf%\3\2\2\2\u00d0"+
		"\u00d1\7\b\2\2\u00d1\u00d2\5\36\20\2\u00d2\u00d3\5\22\n\2\u00d3\u00da"+
		"\3\2\2\2\u00d4\u00d5\7\b\2\2\u00d5\u00d6\5\36\20\2\u00d6\u00d7\5\22\n"+
		"\2\u00d7\u00d8\5(\25\2\u00d8\u00da\3\2\2\2\u00d9\u00d0\3\2\2\2\u00d9\u00d4"+
		"\3\2\2\2\u00da\'\3\2\2\2\u00db\u00dc\7\t\2\2\u00dc\u00e0\5&\24\2\u00dd"+
		"\u00de\7\t\2\2\u00de\u00e0\5\22\n\2\u00df\u00db\3\2\2\2\u00df\u00dd\3"+
		"\2\2\2\u00e0)\3\2\2\2\u00e1\u00e2\7\n\2\2\u00e2\u00e3\5\36\20\2\u00e3"+
		"\u00e4\5\22\n\2\u00e4+\3\2\2\2\u00e5\u00e6\7\r\2\2\u00e6\u00e7\7\17\2"+
		"\2\u00e7\u00e8\5.\30\2\u00e8\u00e9\7\20\2\2\u00e9-\3\2\2\2\u00ea\u00ef"+
		"\5\"\22\2\u00eb\u00ec\7#\2\2\u00ec\u00ee\5\"\22\2\u00ed\u00eb\3\2\2\2"+
		"\u00ee\u00f1\3\2\2\2\u00ef\u00ed\3\2\2\2\u00ef\u00f0\3\2\2\2\u00f0/\3"+
		"\2\2\2\u00f1\u00ef\3\2\2\2\26\63\65>JRYhnt\u0085\u009f\u00a1\u00aa\u00bb"+
		"\u00bd\u00ca\u00ce\u00d9\u00df\u00ef";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}