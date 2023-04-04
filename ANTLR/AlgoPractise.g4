grammar AlgoPractise;
// Lexer
BOOL_TYPE: 'bool';
STR_TYPE: 'string';
NUM_TYPE: 'num';
TRUE: 'true';
FALSE: 'false';
IF: 'if';
ELSE: 'else';
WHILE: 'while';
AND: 'and';
OR: 'or';
ID: LETTER (LETTER | DIGIT | '_')*;
LIST_DCL: '[]';
L_PAR: '(';
R_PAR: ')';
L_CURLY: '{';
R_CURLY: '}';
RETURN: 'return';
ASSIGN: ':=';
NUMVAL: ('-' DIGIT+ | DIGIT+);
STRINGVAL: '"' (LETTER | DIGIT | '\\"')* '"';
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
COMMA: ',';
WS: [ \t\r\n]+ -> skip;
// tells lexer to ignore these characters. Otherwise they will not be allowed in the input
fragment DIGIT: [0-9];
fragment LETTER: [a-zA-Z];
// Parser
start: (func | stmts | stmt)* EOF;
func: type func_decl | func_decl;
func_decl: ID params block;
type: BOOL_TYPE | STR_TYPE | NUM_TYPE;
type_decl: type | type LIST_DCL;
params: (L_PAR R_PAR | L_PAR param_lst R_PAR);
param_lst: param (COMMA param)*;
param: type ID;
block: L_CURLY stmts endblock;
endblock: (RETURN val R_CURLY | R_CURLY);
stmts: ( stmt stmts | stmt);
stmt: dcl | assign_stmt | cntrol | func_call;
dcl: type assign_stmt;
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