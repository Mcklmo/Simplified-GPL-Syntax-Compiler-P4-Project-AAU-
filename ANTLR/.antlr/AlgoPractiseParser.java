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
		RULE_start = 0, RULE_func = 1, RULE_type = 2, RULE_args = 3, RULE_arg_list = 4, 
		RULE_block = 5, RULE_endblock = 6, RULE_stmts = 7, RULE_stmt = 8, RULE_dcl = 9, 
		RULE_assign_stmt = 10, RULE_cond = 11, RULE_expr = 12, RULE_val = 13, 
		RULE_cntrol = 14, RULE_if_stmt = 15, RULE_else_stmt = 16, RULE_while_stmt = 17, 
		RULE_func_call = 18, RULE_list = 19;
	private static String[] makeRuleNames() {
		return new String[] {
			"start", "func", "type", "args", "arg_list", "block", "endblock", "stmts", 
			"stmt", "dcl", "assign_stmt", "cond", "expr", "val", "cntrol", "if_stmt", 
			"else_stmt", "while_stmt", "func_call", "list"
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
			setState(45);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << BOOL_TYPE) | (1L << STR_TYPE) | (1L << NUM_TYPE) | (1L << IF) | (1L << WHILE) | (1L << ID))) != 0)) {
				{
				setState(43);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
				case 1:
					{
					setState(40);
					func();
					}
					break;
				case 2:
					{
					setState(41);
					stmts();
					}
					break;
				case 3:
					{
					setState(42);
					stmt();
					}
					break;
				}
				}
				setState(47);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(48);
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
		public TerminalNode ID() { return getToken(AlgoPractiseParser.ID, 0); }
		public ArgsContext args() {
			return getRuleContext(ArgsContext.class,0);
		}
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
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
			enterOuterAlt(_localctx, 1);
			{
			setState(59);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case BOOL_TYPE:
			case STR_TYPE:
			case NUM_TYPE:
				{
				setState(50);
				type();
				setState(51);
				match(ID);
				setState(52);
				args();
				setState(53);
				block();
				}
				break;
			case ID:
				{
				setState(55);
				match(ID);
				setState(56);
				args();
				setState(57);
				block();
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

	public static class TypeContext extends ParserRuleContext {
		public TerminalNode BOOL_TYPE() { return getToken(AlgoPractiseParser.BOOL_TYPE, 0); }
		public TerminalNode LIST_DCL() { return getToken(AlgoPractiseParser.LIST_DCL, 0); }
		public TerminalNode STR_TYPE() { return getToken(AlgoPractiseParser.STR_TYPE, 0); }
		public TerminalNode NUM_TYPE() { return getToken(AlgoPractiseParser.NUM_TYPE, 0); }
		public TypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_type; }
	}

	public final TypeContext type() throws RecognitionException {
		TypeContext _localctx = new TypeContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_type);
		try {
			setState(70);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(61);
				match(BOOL_TYPE);
				setState(62);
				match(LIST_DCL);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(63);
				match(STR_TYPE);
				setState(64);
				match(LIST_DCL);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(65);
				match(NUM_TYPE);
				setState(66);
				match(LIST_DCL);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(67);
				match(BOOL_TYPE);
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(68);
				match(STR_TYPE);
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(69);
				match(NUM_TYPE);
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

	public static class ArgsContext extends ParserRuleContext {
		public TerminalNode L_PAR() { return getToken(AlgoPractiseParser.L_PAR, 0); }
		public TerminalNode R_PAR() { return getToken(AlgoPractiseParser.R_PAR, 0); }
		public Arg_listContext arg_list() {
			return getRuleContext(Arg_listContext.class,0);
		}
		public ArgsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_args; }
	}

	public final ArgsContext args() throws RecognitionException {
		ArgsContext _localctx = new ArgsContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_args);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(78);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
			case 1:
				{
				setState(72);
				match(L_PAR);
				setState(73);
				match(R_PAR);
				}
				break;
			case 2:
				{
				setState(74);
				match(L_PAR);
				setState(75);
				arg_list();
				setState(76);
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

	public static class Arg_listContext extends ParserRuleContext {
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public TerminalNode ID() { return getToken(AlgoPractiseParser.ID, 0); }
		public List<TerminalNode> COMMA() { return getTokens(AlgoPractiseParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(AlgoPractiseParser.COMMA, i);
		}
		public List<Arg_listContext> arg_list() {
			return getRuleContexts(Arg_listContext.class);
		}
		public Arg_listContext arg_list(int i) {
			return getRuleContext(Arg_listContext.class,i);
		}
		public Arg_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arg_list; }
	}

	public final Arg_listContext arg_list() throws RecognitionException {
		Arg_listContext _localctx = new Arg_listContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_arg_list);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(92);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				{
				setState(80);
				type();
				setState(81);
				match(ID);
				setState(86);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
				while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1 ) {
						{
						{
						setState(82);
						match(COMMA);
						setState(83);
						arg_list();
						}
						} 
					}
					setState(88);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
				}
				}
				break;
			case 2:
				{
				setState(89);
				type();
				setState(90);
				match(ID);
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
		enterRule(_localctx, 10, RULE_block);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(94);
			match(L_CURLY);
			setState(95);
			stmts();
			setState(96);
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
		enterRule(_localctx, 12, RULE_endblock);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(103);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case RETURN:
				{
				setState(98);
				match(RETURN);
				setState(99);
				val();
				setState(100);
				match(R_CURLY);
				}
				break;
			case R_CURLY:
				{
				setState(102);
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
		public DclContext dcl() {
			return getRuleContext(DclContext.class,0);
		}
		public StmtsContext stmts() {
			return getRuleContext(StmtsContext.class,0);
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
		public StmtContext stmt() {
			return getRuleContext(StmtContext.class,0);
		}
		public StmtsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stmts; }
	}

	public final StmtsContext stmts() throws RecognitionException {
		StmtsContext _localctx = new StmtsContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_stmts);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(118);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				{
				setState(105);
				dcl();
				setState(106);
				stmts();
				}
				break;
			case 2:
				{
				setState(108);
				assign_stmt();
				setState(109);
				stmts();
				}
				break;
			case 3:
				{
				setState(111);
				cntrol();
				setState(112);
				stmts();
				}
				break;
			case 4:
				{
				setState(114);
				func_call();
				setState(115);
				stmts();
				}
				break;
			case 5:
				{
				setState(117);
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
		enterRule(_localctx, 16, RULE_stmt);
		try {
			setState(124);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(120);
				dcl();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(121);
				assign_stmt();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(122);
				cntrol();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(123);
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
		public TerminalNode BOOL_TYPE() { return getToken(AlgoPractiseParser.BOOL_TYPE, 0); }
		public Assign_stmtContext assign_stmt() {
			return getRuleContext(Assign_stmtContext.class,0);
		}
		public TerminalNode STR_TYPE() { return getToken(AlgoPractiseParser.STR_TYPE, 0); }
		public TerminalNode NUM_TYPE() { return getToken(AlgoPractiseParser.NUM_TYPE, 0); }
		public DclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_dcl; }
	}

	public final DclContext dcl() throws RecognitionException {
		DclContext _localctx = new DclContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_dcl);
		try {
			setState(132);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case BOOL_TYPE:
				enterOuterAlt(_localctx, 1);
				{
				setState(126);
				match(BOOL_TYPE);
				setState(127);
				assign_stmt();
				}
				break;
			case STR_TYPE:
				enterOuterAlt(_localctx, 2);
				{
				setState(128);
				match(STR_TYPE);
				setState(129);
				assign_stmt();
				}
				break;
			case NUM_TYPE:
				enterOuterAlt(_localctx, 3);
				{
				setState(130);
				match(NUM_TYPE);
				setState(131);
				assign_stmt();
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
		enterRule(_localctx, 20, RULE_assign_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(134);
			match(ID);
			setState(135);
			match(ASSIGN);
			setState(136);
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
		int _startState = 22;
		enterRecursionRule(_localctx, 22, RULE_cond, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(146);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
			case 1:
				{
				setState(139);
				match(NEG);
				setState(140);
				cond(3);
				}
				break;
			case 2:
				{
				setState(141);
				match(L_PAR);
				setState(142);
				cond(0);
				setState(143);
				match(R_PAR);
				}
				break;
			case 3:
				{
				setState(145);
				expr(0);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(174);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,13,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(172);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,12,_ctx) ) {
					case 1:
						{
						_localctx = new CondContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_cond);
						setState(148);
						if (!(precpred(_ctx, 11))) throw new FailedPredicateException(this, "precpred(_ctx, 11)");
						setState(149);
						match(OR);
						setState(150);
						cond(12);
						}
						break;
					case 2:
						{
						_localctx = new CondContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_cond);
						setState(151);
						if (!(precpred(_ctx, 10))) throw new FailedPredicateException(this, "precpred(_ctx, 10)");
						setState(152);
						match(AND);
						setState(153);
						cond(11);
						}
						break;
					case 3:
						{
						_localctx = new CondContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_cond);
						setState(154);
						if (!(precpred(_ctx, 9))) throw new FailedPredicateException(this, "precpred(_ctx, 9)");
						setState(155);
						match(EQUAL);
						setState(156);
						cond(10);
						}
						break;
					case 4:
						{
						_localctx = new CondContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_cond);
						setState(157);
						if (!(precpred(_ctx, 8))) throw new FailedPredicateException(this, "precpred(_ctx, 8)");
						setState(158);
						match(NE);
						setState(159);
						cond(9);
						}
						break;
					case 5:
						{
						_localctx = new CondContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_cond);
						setState(160);
						if (!(precpred(_ctx, 7))) throw new FailedPredicateException(this, "precpred(_ctx, 7)");
						setState(161);
						match(LTE);
						setState(162);
						cond(8);
						}
						break;
					case 6:
						{
						_localctx = new CondContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_cond);
						setState(163);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(164);
						match(GTE);
						setState(165);
						cond(7);
						}
						break;
					case 7:
						{
						_localctx = new CondContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_cond);
						setState(166);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(167);
						match(GT);
						setState(168);
						cond(6);
						}
						break;
					case 8:
						{
						_localctx = new CondContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_cond);
						setState(169);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(170);
						match(LT);
						setState(171);
						cond(5);
						}
						break;
					}
					} 
				}
				setState(176);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,13,_ctx);
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
		int _startState = 24;
		enterRecursionRule(_localctx, 24, RULE_expr, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(183);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case TRUE:
			case FALSE:
			case ID:
			case L_CURLY:
			case NUMVAL:
			case STRINGVAL:
				{
				setState(178);
				val();
				}
				break;
			case L_PAR:
				{
				setState(179);
				match(L_PAR);
				setState(180);
				expr(0);
				setState(181);
				match(R_PAR);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(202);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,16,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(200);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,15,_ctx) ) {
					case 1:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(185);
						if (!(precpred(_ctx, 7))) throw new FailedPredicateException(this, "precpred(_ctx, 7)");
						setState(186);
						match(PLUS);
						setState(187);
						expr(8);
						}
						break;
					case 2:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(188);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(189);
						match(MINUS);
						setState(190);
						expr(7);
						}
						break;
					case 3:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(191);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(192);
						match(MULT);
						setState(193);
						expr(6);
						}
						break;
					case 4:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(194);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(195);
						match(DIV);
						setState(196);
						expr(5);
						}
						break;
					case 5:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(197);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(198);
						match(MOD);
						setState(199);
						expr(4);
						}
						break;
					}
					} 
				}
				setState(204);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,16,_ctx);
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
		enterRule(_localctx, 26, RULE_val);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(215);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,17,_ctx) ) {
			case 1:
				{
				setState(205);
				match(ID);
				}
				break;
			case 2:
				{
				setState(206);
				match(NUMVAL);
				}
				break;
			case 3:
				{
				setState(207);
				match(STRINGVAL);
				}
				break;
			case 4:
				{
				setState(208);
				match(TRUE);
				}
				break;
			case 5:
				{
				setState(209);
				match(FALSE);
				}
				break;
			case 6:
				{
				setState(210);
				match(L_CURLY);
				setState(211);
				list();
				setState(212);
				match(R_CURLY);
				}
				break;
			case 7:
				{
				setState(214);
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
		enterRule(_localctx, 28, RULE_cntrol);
		try {
			setState(219);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IF:
				enterOuterAlt(_localctx, 1);
				{
				setState(217);
				if_stmt();
				}
				break;
			case WHILE:
				enterOuterAlt(_localctx, 2);
				{
				setState(218);
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
		enterRule(_localctx, 30, RULE_if_stmt);
		try {
			setState(230);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,19,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(221);
				match(IF);
				setState(222);
				cond(0);
				setState(223);
				block();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(225);
				match(IF);
				setState(226);
				cond(0);
				setState(227);
				block();
				setState(228);
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
		enterRule(_localctx, 32, RULE_else_stmt);
		try {
			setState(236);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,20,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(232);
				match(ELSE);
				setState(233);
				if_stmt();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(234);
				match(ELSE);
				setState(235);
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
		enterRule(_localctx, 34, RULE_while_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(238);
			match(WHILE);
			setState(239);
			cond(0);
			setState(240);
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
		enterRule(_localctx, 36, RULE_func_call);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(242);
			match(ID);
			setState(243);
			match(L_PAR);
			setState(244);
			list();
			setState(245);
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
		enterRule(_localctx, 38, RULE_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(247);
			val();
			setState(252);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(248);
				match(COMMA);
				setState(249);
				val();
				}
				}
				setState(254);
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
		case 11:
			return cond_sempred((CondContext)_localctx, predIndex);
		case 12:
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3$\u0102\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\3\2\3\2\3\2\7\2.\n\2\f\2\16\2\61\13\2\3"+
		"\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3>\n\3\3\4\3\4\3\4\3\4\3"+
		"\4\3\4\3\4\3\4\3\4\5\4I\n\4\3\5\3\5\3\5\3\5\3\5\3\5\5\5Q\n\5\3\6\3\6\3"+
		"\6\3\6\7\6W\n\6\f\6\16\6Z\13\6\3\6\3\6\3\6\5\6_\n\6\3\7\3\7\3\7\3\7\3"+
		"\b\3\b\3\b\3\b\3\b\5\bj\n\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3"+
		"\t\3\t\3\t\5\ty\n\t\3\n\3\n\3\n\3\n\5\n\177\n\n\3\13\3\13\3\13\3\13\3"+
		"\13\3\13\5\13\u0087\n\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3"+
		"\r\5\r\u0095\n\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3"+
		"\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\7\r\u00af\n\r\f\r\16\r\u00b2"+
		"\13\r\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u00ba\n\16\3\16\3\16\3\16\3\16"+
		"\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\7\16\u00cb\n\16"+
		"\f\16\16\16\u00ce\13\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3"+
		"\17\5\17\u00da\n\17\3\20\3\20\5\20\u00de\n\20\3\21\3\21\3\21\3\21\3\21"+
		"\3\21\3\21\3\21\3\21\5\21\u00e9\n\21\3\22\3\22\3\22\3\22\5\22\u00ef\n"+
		"\22\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\7\25\u00fd"+
		"\n\25\f\25\16\25\u0100\13\25\3\25\2\4\30\32\26\2\4\6\b\n\f\16\20\22\24"+
		"\26\30\32\34\36 \"$&(\2\2\2\u011d\2/\3\2\2\2\4=\3\2\2\2\6H\3\2\2\2\bP"+
		"\3\2\2\2\n^\3\2\2\2\f`\3\2\2\2\16i\3\2\2\2\20x\3\2\2\2\22~\3\2\2\2\24"+
		"\u0086\3\2\2\2\26\u0088\3\2\2\2\30\u0094\3\2\2\2\32\u00b9\3\2\2\2\34\u00d9"+
		"\3\2\2\2\36\u00dd\3\2\2\2 \u00e8\3\2\2\2\"\u00ee\3\2\2\2$\u00f0\3\2\2"+
		"\2&\u00f4\3\2\2\2(\u00f9\3\2\2\2*.\5\4\3\2+.\5\20\t\2,.\5\22\n\2-*\3\2"+
		"\2\2-+\3\2\2\2-,\3\2\2\2.\61\3\2\2\2/-\3\2\2\2/\60\3\2\2\2\60\62\3\2\2"+
		"\2\61/\3\2\2\2\62\63\7\2\2\3\63\3\3\2\2\2\64\65\5\6\4\2\65\66\7\r\2\2"+
		"\66\67\5\b\5\2\678\5\f\7\28>\3\2\2\29:\7\r\2\2:;\5\b\5\2;<\5\f\7\2<>\3"+
		"\2\2\2=\64\3\2\2\2=9\3\2\2\2>\5\3\2\2\2?@\7\3\2\2@I\7\16\2\2AB\7\4\2\2"+
		"BI\7\16\2\2CD\7\5\2\2DI\7\16\2\2EI\7\3\2\2FI\7\4\2\2GI\7\5\2\2H?\3\2\2"+
		"\2HA\3\2\2\2HC\3\2\2\2HE\3\2\2\2HF\3\2\2\2HG\3\2\2\2I\7\3\2\2\2JK\7\17"+
		"\2\2KQ\7\20\2\2LM\7\17\2\2MN\5\n\6\2NO\7\20\2\2OQ\3\2\2\2PJ\3\2\2\2PL"+
		"\3\2\2\2Q\t\3\2\2\2RS\5\6\4\2SX\7\r\2\2TU\7#\2\2UW\5\n\6\2VT\3\2\2\2W"+
		"Z\3\2\2\2XV\3\2\2\2XY\3\2\2\2Y_\3\2\2\2ZX\3\2\2\2[\\\5\6\4\2\\]\7\r\2"+
		"\2]_\3\2\2\2^R\3\2\2\2^[\3\2\2\2_\13\3\2\2\2`a\7\21\2\2ab\5\20\t\2bc\5"+
		"\16\b\2c\r\3\2\2\2de\7\23\2\2ef\5\34\17\2fg\7\22\2\2gj\3\2\2\2hj\7\22"+
		"\2\2id\3\2\2\2ih\3\2\2\2j\17\3\2\2\2kl\5\24\13\2lm\5\20\t\2my\3\2\2\2"+
		"no\5\26\f\2op\5\20\t\2py\3\2\2\2qr\5\36\20\2rs\5\20\t\2sy\3\2\2\2tu\5"+
		"&\24\2uv\5\20\t\2vy\3\2\2\2wy\5\22\n\2xk\3\2\2\2xn\3\2\2\2xq\3\2\2\2x"+
		"t\3\2\2\2xw\3\2\2\2y\21\3\2\2\2z\177\5\24\13\2{\177\5\26\f\2|\177\5\36"+
		"\20\2}\177\5&\24\2~z\3\2\2\2~{\3\2\2\2~|\3\2\2\2~}\3\2\2\2\177\23\3\2"+
		"\2\2\u0080\u0081\7\3\2\2\u0081\u0087\5\26\f\2\u0082\u0083\7\4\2\2\u0083"+
		"\u0087\5\26\f\2\u0084\u0085\7\5\2\2\u0085\u0087\5\26\f\2\u0086\u0080\3"+
		"\2\2\2\u0086\u0082\3\2\2\2\u0086\u0084\3\2\2\2\u0087\25\3\2\2\2\u0088"+
		"\u0089\7\r\2\2\u0089\u008a\7\24\2\2\u008a\u008b\5\30\r\2\u008b\27\3\2"+
		"\2\2\u008c\u008d\b\r\1\2\u008d\u008e\7\27\2\2\u008e\u0095\5\30\r\5\u008f"+
		"\u0090\7\17\2\2\u0090\u0091\5\30\r\2\u0091\u0092\7\20\2\2\u0092\u0095"+
		"\3\2\2\2\u0093\u0095\5\32\16\2\u0094\u008c\3\2\2\2\u0094\u008f\3\2\2\2"+
		"\u0094\u0093\3\2\2\2\u0095\u00b0\3\2\2\2\u0096\u0097\f\r\2\2\u0097\u0098"+
		"\7\f\2\2\u0098\u00af\5\30\r\16\u0099\u009a\f\f\2\2\u009a\u009b\7\13\2"+
		"\2\u009b\u00af\5\30\r\r\u009c\u009d\f\13\2\2\u009d\u009e\7\30\2\2\u009e"+
		"\u00af\5\30\r\f\u009f\u00a0\f\n\2\2\u00a0\u00a1\7\35\2\2\u00a1\u00af\5"+
		"\30\r\13\u00a2\u00a3\f\t\2\2\u00a3\u00a4\7\31\2\2\u00a4\u00af\5\30\r\n"+
		"\u00a5\u00a6\f\b\2\2\u00a6\u00a7\7\32\2\2\u00a7\u00af\5\30\r\t\u00a8\u00a9"+
		"\f\7\2\2\u00a9\u00aa\7\34\2\2\u00aa\u00af\5\30\r\b\u00ab\u00ac\f\6\2\2"+
		"\u00ac\u00ad\7\33\2\2\u00ad\u00af\5\30\r\7\u00ae\u0096\3\2\2\2\u00ae\u0099"+
		"\3\2\2\2\u00ae\u009c\3\2\2\2\u00ae\u009f\3\2\2\2\u00ae\u00a2\3\2\2\2\u00ae"+
		"\u00a5\3\2\2\2\u00ae\u00a8\3\2\2\2\u00ae\u00ab\3\2\2\2\u00af\u00b2\3\2"+
		"\2\2\u00b0\u00ae\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1\31\3\2\2\2\u00b2\u00b0"+
		"\3\2\2\2\u00b3\u00b4\b\16\1\2\u00b4\u00ba\5\34\17\2\u00b5\u00b6\7\17\2"+
		"\2\u00b6\u00b7\5\32\16\2\u00b7\u00b8\7\20\2\2\u00b8\u00ba\3\2\2\2\u00b9"+
		"\u00b3\3\2\2\2\u00b9\u00b5\3\2\2\2\u00ba\u00cc\3\2\2\2\u00bb\u00bc\f\t"+
		"\2\2\u00bc\u00bd\7\36\2\2\u00bd\u00cb\5\32\16\n\u00be\u00bf\f\b\2\2\u00bf"+
		"\u00c0\7\37\2\2\u00c0\u00cb\5\32\16\t\u00c1\u00c2\f\7\2\2\u00c2\u00c3"+
		"\7 \2\2\u00c3\u00cb\5\32\16\b\u00c4\u00c5\f\6\2\2\u00c5\u00c6\7!\2\2\u00c6"+
		"\u00cb\5\32\16\7\u00c7\u00c8\f\5\2\2\u00c8\u00c9\7\"\2\2\u00c9\u00cb\5"+
		"\32\16\6\u00ca\u00bb\3\2\2\2\u00ca\u00be\3\2\2\2\u00ca\u00c1\3\2\2\2\u00ca"+
		"\u00c4\3\2\2\2\u00ca\u00c7\3\2\2\2\u00cb\u00ce\3\2\2\2\u00cc\u00ca\3\2"+
		"\2\2\u00cc\u00cd\3\2\2\2\u00cd\33\3\2\2\2\u00ce\u00cc\3\2\2\2\u00cf\u00da"+
		"\7\r\2\2\u00d0\u00da\7\25\2\2\u00d1\u00da\7\26\2\2\u00d2\u00da\7\6\2\2"+
		"\u00d3\u00da\7\7\2\2\u00d4\u00d5\7\21\2\2\u00d5\u00d6\5(\25\2\u00d6\u00d7"+
		"\7\22\2\2\u00d7\u00da\3\2\2\2\u00d8\u00da\5&\24\2\u00d9\u00cf\3\2\2\2"+
		"\u00d9\u00d0\3\2\2\2\u00d9\u00d1\3\2\2\2\u00d9\u00d2\3\2\2\2\u00d9\u00d3"+
		"\3\2\2\2\u00d9\u00d4\3\2\2\2\u00d9\u00d8\3\2\2\2\u00da\35\3\2\2\2\u00db"+
		"\u00de\5 \21\2\u00dc\u00de\5$\23\2\u00dd\u00db\3\2\2\2\u00dd\u00dc\3\2"+
		"\2\2\u00de\37\3\2\2\2\u00df\u00e0\7\b\2\2\u00e0\u00e1\5\30\r\2\u00e1\u00e2"+
		"\5\f\7\2\u00e2\u00e9\3\2\2\2\u00e3\u00e4\7\b\2\2\u00e4\u00e5\5\30\r\2"+
		"\u00e5\u00e6\5\f\7\2\u00e6\u00e7\5\"\22\2\u00e7\u00e9\3\2\2\2\u00e8\u00df"+
		"\3\2\2\2\u00e8\u00e3\3\2\2\2\u00e9!\3\2\2\2\u00ea\u00eb\7\t\2\2\u00eb"+
		"\u00ef\5 \21\2\u00ec\u00ed\7\t\2\2\u00ed\u00ef\5\f\7\2\u00ee\u00ea\3\2"+
		"\2\2\u00ee\u00ec\3\2\2\2\u00ef#\3\2\2\2\u00f0\u00f1\7\n\2\2\u00f1\u00f2"+
		"\5\30\r\2\u00f2\u00f3\5\f\7\2\u00f3%\3\2\2\2\u00f4\u00f5\7\r\2\2\u00f5"+
		"\u00f6\7\17\2\2\u00f6\u00f7\5(\25\2\u00f7\u00f8\7\20\2\2\u00f8\'\3\2\2"+
		"\2\u00f9\u00fe\5\34\17\2\u00fa\u00fb\7#\2\2\u00fb\u00fd\5\34\17\2\u00fc"+
		"\u00fa\3\2\2\2\u00fd\u0100\3\2\2\2\u00fe\u00fc\3\2\2\2\u00fe\u00ff\3\2"+
		"\2\2\u00ff)\3\2\2\2\u0100\u00fe\3\2\2\2\30-/=HPX^ix~\u0086\u0094\u00ae"+
		"\u00b0\u00b9\u00ca\u00cc\u00d9\u00dd\u00e8\u00ee\u00fe";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}