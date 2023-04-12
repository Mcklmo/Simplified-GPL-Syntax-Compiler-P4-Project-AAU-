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
ID: (LETTER | '_') (LETTER | DIGIT | '_')*;
LIST_DCL: '[]';
L_PAR: '(';
R_PAR: ')';
L_CURLY: '{';
R_CURLY: '}';
RETURN: 'return';
ASSIGN: ':=';
NUMVAL: '-'? DIGIT+;
STRINGVAL:
	'"' (ESC | ~["\n\r])*? '"'; // ~["\n\r] is equal to . without the escaped characters
ESC: '\\"' | '\\\\' | '\\n' | '\\r';
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
COMMENT: '/*' .*? '*/' -> skip; // multi-line comment
// tells lexer to ignore these characters. Otherwise they will not be allowed in the input
fragment DIGIT: [0-9];
fragment LETTER: [a-zA-Z];
// Parser
start: (func | stmts)* EOF;
func: type func_decl | func_decl;
func_decl: ID params block;
type: BOOL_TYPE | STR_TYPE | NUM_TYPE | type LIST_DCL;
params: (L_PAR R_PAR | L_PAR param_lst R_PAR);
param_lst: param (COMMA param)*;
param: type ID;
block: L_CURLY stmts endblock;
endblock: (RETURN val R_CURLY | R_CURLY);
stmts: ( stmt stmts | stmt);
stmt: dcl | assign_stmt | cntrol | func_call;
dcl: type assign_stmt | type ID;
assign_stmt: ID ASSIGN expr;
expr: // antlr4 gives lowest precedence to the first alternative
	expr OR expr
	| expr AND expr
	| expr EQUAL expr
	| expr NE expr
	| expr LTE expr
	| expr GTE expr
	| expr GT expr
	| expr LT expr
	| expr PLUS expr
	| expr MINUS expr
	| expr MULT expr
	| expr DIV expr
	| expr MOD expr
	| <assoc = right>NEG expr
	| val
	| L_PAR expr R_PAR;
val: (
		ID
		| NUMVAL
		| STRINGVAL
		| TRUE
		| FALSE
		| L_CURLY elmnt_list R_CURLY
		| ID ('[' val ']')+ // list subscript
		| func_call
	);
cntrol: if_stmt | while_stmt;
if_stmt: IF expr block | IF expr block else_stmt;
else_stmt: ELSE if_stmt | ELSE block;
while_stmt: WHILE expr block;
func_call: ID L_PAR elmnt_list R_PAR;
elmnt_list: expr (COMMA expr)* | ;