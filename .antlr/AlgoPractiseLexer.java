// Generated from d:\OneDrive\projects\GitHub\p4-group-project\AlgoPractise.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class AlgoPractiseLexer extends Lexer {
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
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"BOOL_TYPE", "STR_TYPE", "NUM_TYPE", "TRUE", "FALSE", "IF", "ELSE", "WHILE", 
			"AND", "OR", "ID", "LIST_DCL", "L_PAR", "R_PAR", "L_CURLY", "R_CURLY", 
			"RETURN", "ASSIGN", "NUMVAL", "STRINGVAL", "NEG", "EQUAL", "LTE", "GTE", 
			"LT", "GT", "NE", "PLUS", "MINUS", "MULT", "DIV", "MOD", "COMMA", "WS", 
			"COMMENT", "DIGIT", "LETTER"
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


	public AlgoPractiseLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "AlgoPractise.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2%\u00eb\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3"+
		"\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6"+
		"\3\6\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3"+
		"\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3\f\7\f\u0082\n\f\f\f\16\f\u0085\13"+
		"\f\3\r\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\22"+
		"\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\24\3\24\6\24\u009e\n\24\r\24\16"+
		"\24\u009f\3\24\6\24\u00a3\n\24\r\24\16\24\u00a4\5\24\u00a7\n\24\3\25\3"+
		"\25\3\25\3\25\3\25\7\25\u00ae\n\25\f\25\16\25\u00b1\13\25\3\25\3\25\3"+
		"\26\3\26\3\27\3\27\3\27\3\30\3\30\3\30\3\31\3\31\3\31\3\32\3\32\3\33\3"+
		"\33\3\34\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3"+
		"#\6#\u00d4\n#\r#\16#\u00d5\3#\3#\3$\3$\3$\3$\7$\u00de\n$\f$\16$\u00e1"+
		"\13$\3$\3$\3$\3$\3$\3%\3%\3&\3&\3\u00df\2\'\3\3\5\4\7\5\t\6\13\7\r\b\17"+
		"\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+"+
		"\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I\2K\2\3\2\5\5"+
		"\2\13\f\17\17\"\"\3\2\62;\4\2C\\c|\2\u00f3\2\3\3\2\2\2\2\5\3\2\2\2\2\7"+
		"\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2"+
		"\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2"+
		"\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2"+
		"\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2"+
		"\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2"+
		"\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\3M\3\2\2\2\5R\3\2\2\2\7Y"+
		"\3\2\2\2\t]\3\2\2\2\13b\3\2\2\2\rh\3\2\2\2\17k\3\2\2\2\21p\3\2\2\2\23"+
		"v\3\2\2\2\25z\3\2\2\2\27}\3\2\2\2\31\u0086\3\2\2\2\33\u0089\3\2\2\2\35"+
		"\u008b\3\2\2\2\37\u008d\3\2\2\2!\u008f\3\2\2\2#\u0091\3\2\2\2%\u0098\3"+
		"\2\2\2\'\u00a6\3\2\2\2)\u00a8\3\2\2\2+\u00b4\3\2\2\2-\u00b6\3\2\2\2/\u00b9"+
		"\3\2\2\2\61\u00bc\3\2\2\2\63\u00bf\3\2\2\2\65\u00c1\3\2\2\2\67\u00c3\3"+
		"\2\2\29\u00c6\3\2\2\2;\u00c8\3\2\2\2=\u00ca\3\2\2\2?\u00cc\3\2\2\2A\u00ce"+
		"\3\2\2\2C\u00d0\3\2\2\2E\u00d3\3\2\2\2G\u00d9\3\2\2\2I\u00e7\3\2\2\2K"+
		"\u00e9\3\2\2\2MN\7d\2\2NO\7q\2\2OP\7q\2\2PQ\7n\2\2Q\4\3\2\2\2RS\7u\2\2"+
		"ST\7v\2\2TU\7t\2\2UV\7k\2\2VW\7p\2\2WX\7i\2\2X\6\3\2\2\2YZ\7p\2\2Z[\7"+
		"w\2\2[\\\7o\2\2\\\b\3\2\2\2]^\7v\2\2^_\7t\2\2_`\7w\2\2`a\7g\2\2a\n\3\2"+
		"\2\2bc\7h\2\2cd\7c\2\2de\7n\2\2ef\7u\2\2fg\7g\2\2g\f\3\2\2\2hi\7k\2\2"+
		"ij\7h\2\2j\16\3\2\2\2kl\7g\2\2lm\7n\2\2mn\7u\2\2no\7g\2\2o\20\3\2\2\2"+
		"pq\7y\2\2qr\7j\2\2rs\7k\2\2st\7n\2\2tu\7g\2\2u\22\3\2\2\2vw\7c\2\2wx\7"+
		"p\2\2xy\7f\2\2y\24\3\2\2\2z{\7q\2\2{|\7t\2\2|\26\3\2\2\2}\u0083\5K&\2"+
		"~\u0082\5K&\2\177\u0082\5I%\2\u0080\u0082\7a\2\2\u0081~\3\2\2\2\u0081"+
		"\177\3\2\2\2\u0081\u0080\3\2\2\2\u0082\u0085\3\2\2\2\u0083\u0081\3\2\2"+
		"\2\u0083\u0084\3\2\2\2\u0084\30\3\2\2\2\u0085\u0083\3\2\2\2\u0086\u0087"+
		"\7]\2\2\u0087\u0088\7_\2\2\u0088\32\3\2\2\2\u0089\u008a\7*\2\2\u008a\34"+
		"\3\2\2\2\u008b\u008c\7+\2\2\u008c\36\3\2\2\2\u008d\u008e\7}\2\2\u008e"+
		" \3\2\2\2\u008f\u0090\7\177\2\2\u0090\"\3\2\2\2\u0091\u0092\7t\2\2\u0092"+
		"\u0093\7g\2\2\u0093\u0094\7v\2\2\u0094\u0095\7w\2\2\u0095\u0096\7t\2\2"+
		"\u0096\u0097\7p\2\2\u0097$\3\2\2\2\u0098\u0099\7<\2\2\u0099\u009a\7?\2"+
		"\2\u009a&\3\2\2\2\u009b\u009d\7/\2\2\u009c\u009e\5I%\2\u009d\u009c\3\2"+
		"\2\2\u009e\u009f\3\2\2\2\u009f\u009d\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0"+
		"\u00a7\3\2\2\2\u00a1\u00a3\5I%\2\u00a2\u00a1\3\2\2\2\u00a3\u00a4\3\2\2"+
		"\2\u00a4\u00a2\3\2\2\2\u00a4\u00a5\3\2\2\2\u00a5\u00a7\3\2\2\2\u00a6\u009b"+
		"\3\2\2\2\u00a6\u00a2\3\2\2\2\u00a7(\3\2\2\2\u00a8\u00af\7$\2\2\u00a9\u00ae"+
		"\5K&\2\u00aa\u00ae\5I%\2\u00ab\u00ac\7^\2\2\u00ac\u00ae\7$\2\2\u00ad\u00a9"+
		"\3\2\2\2\u00ad\u00aa\3\2\2\2\u00ad\u00ab\3\2\2\2\u00ae\u00b1\3\2\2\2\u00af"+
		"\u00ad\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0\u00b2\3\2\2\2\u00b1\u00af\3\2"+
		"\2\2\u00b2\u00b3\7$\2\2\u00b3*\3\2\2\2\u00b4\u00b5\7#\2\2\u00b5,\3\2\2"+
		"\2\u00b6\u00b7\7?\2\2\u00b7\u00b8\7?\2\2\u00b8.\3\2\2\2\u00b9\u00ba\7"+
		">\2\2\u00ba\u00bb\7?\2\2\u00bb\60\3\2\2\2\u00bc\u00bd\7@\2\2\u00bd\u00be"+
		"\7?\2\2\u00be\62\3\2\2\2\u00bf\u00c0\7>\2\2\u00c0\64\3\2\2\2\u00c1\u00c2"+
		"\7@\2\2\u00c2\66\3\2\2\2\u00c3\u00c4\7#\2\2\u00c4\u00c5\7?\2\2\u00c58"+
		"\3\2\2\2\u00c6\u00c7\7-\2\2\u00c7:\3\2\2\2\u00c8\u00c9\7/\2\2\u00c9<\3"+
		"\2\2\2\u00ca\u00cb\7,\2\2\u00cb>\3\2\2\2\u00cc\u00cd\7\61\2\2\u00cd@\3"+
		"\2\2\2\u00ce\u00cf\7\'\2\2\u00cfB\3\2\2\2\u00d0\u00d1\7.\2\2\u00d1D\3"+
		"\2\2\2\u00d2\u00d4\t\2\2\2\u00d3\u00d2\3\2\2\2\u00d4\u00d5\3\2\2\2\u00d5"+
		"\u00d3\3\2\2\2\u00d5\u00d6\3\2\2\2\u00d6\u00d7\3\2\2\2\u00d7\u00d8\b#"+
		"\2\2\u00d8F\3\2\2\2\u00d9\u00da\7\61\2\2\u00da\u00db\7,\2\2\u00db\u00df"+
		"\3\2\2\2\u00dc\u00de\13\2\2\2\u00dd\u00dc\3\2\2\2\u00de\u00e1\3\2\2\2"+
		"\u00df\u00e0\3\2\2\2\u00df\u00dd\3\2\2\2\u00e0\u00e2\3\2\2\2\u00e1\u00df"+
		"\3\2\2\2\u00e2\u00e3\7,\2\2\u00e3\u00e4\7\61\2\2\u00e4\u00e5\3\2\2\2\u00e5"+
		"\u00e6\b$\2\2\u00e6H\3\2\2\2\u00e7\u00e8\t\3\2\2\u00e8J\3\2\2\2\u00e9"+
		"\u00ea\t\4\2\2\u00eaL\3\2\2\2\f\2\u0081\u0083\u009f\u00a4\u00a6\u00ad"+
		"\u00af\u00d5\u00df\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}