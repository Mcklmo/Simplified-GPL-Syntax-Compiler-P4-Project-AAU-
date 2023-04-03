grammar AlgoPractise;
// Lexer
ID: LETTER (LETTER | DIGIT | '_')*;
BOOL_TYPE: 'bool';
STR_TYPE: 'string';
NUM_TYPE: 'num';
LIST_DCL: '[]';
L_PAR: '(';
R_PAR: ')';
L_CURLY: '{';
R_CURLY: '}';
RETURN: 'return';
ASSIGN: ':=';
NUMVAL: ('-' DIGIT+ | DIGIT+);
STRINGVAL: '"' (LETTER | DIGIT | '\\"')* '"';
TRUE: 'true';
FALSE: 'false';
IF: 'if';
ELSE: 'else';
WHILE: 'while';
AND: 'and';
OR: 'or';
NEG: '!';
EQUAL: '==';
LTE: '<=';
GTE: '>=';
LT: '<';
GT: '>';
NE: '!=';
PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';
MOD: '%';
BLANK: (' ')+ -> skip;
COMMA: ',';
NEWLINE: '\n';
fragment DIGIT: '0' ..'9';
fragment LETTER: 'a' ..'z' | 'A' ..'Z';
// Parser
start: (func | stmts | stmt)* EOF;
func: (type ID args block | ID args block);
type:
	BOOL_TYPE LIST_DCL
	| STR_TYPE LIST_DCL
	| NUM_TYPE LIST_DCL
	| BOOL_TYPE
	| STR_TYPE
	| NUM_TYPE;
args: (L_PAR R_PAR | L_PAR arg_list R_PAR);
arg_list: (type ID (COMMA arg_list)* | type ID);
block: L_CURLY NEWLINE stmts endblock;
endblock: (RETURN val R_CURLY NEWLINE | R_CURLY NEWLINE);
stmts: (
		dcl NEWLINE stmts
		| assign_stmt NEWLINE stmts
		| cntrol stmts
		| func_call stmts
		| stmt
	);
stmt: dcl | assign_stmt | cntrol | func_call;
dcl:
	BOOL_TYPE assign_stmt
	| STR_TYPE assign_stmt
	| NUM_TYPE assign_stmt;
assign_stmt: ID ASSIGN cond;
cond: // antlr4 gives highest precedence to the first alternative
	cond OR cond
	| cond AND cond
	| cond EQUAL cond
	| cond NE cond
	| cond LTE cond
	| cond GTE cond
	| cond GT cond
	| cond LT cond
	| <assoc = right>NEG cond
	| L_PAR cond R_PAR
	| expr;
expr:
	expr PLUS expr
	| expr MINUS expr
	| expr MULT expr
	| expr DIV expr
	| expr MOD expr
	| val
	| L_PAR expr R_PAR;
val: (
		ID
		| NUMVAL
		| STRINGVAL
		| TRUE
		| FALSE
		| L_CURLY list R_CURLY
		| func_call
	);
cntrol: if_stmt | while_stmt;
if_stmt: IF cond block | IF cond block else_stmt;
else_stmt: ELSE if_stmt | ELSE block;
while_stmt: WHILE cond block;
func_call: ID L_PAR list R_PAR;
list: val (COMMA val)*;