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
RETURN: 'return';
ID: (LETTER | '_') (LETTER | DIGIT | '_')*;
L_BRACKET: '[';
R_BRACKET: ']';
L_PAR: '(';
R_PAR: ')';
L_CURLY: '{';
R_CURLY: '}';
ASSIGN: ':=';
NUMVAL: '-'? DIGIT+ ('.' DIGIT+)?;
STRINGVAL: '"' (~('\r' | '\n' | '"' | '\\') | ('\\"' | '\\n' | '\\r' | '\\\\'))* '"';
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
NEWLINE: [\n];
WS: [ \t\r]+ -> skip;
COMMENT: '/*' .*? '*/' -> skip; // multi-line comment
// tells lexer to ignore these characters. Otherwise they will not be allowed in the input
fragment DIGIT: [0-9];
fragment LETTER: [a-zA-Z];

// Parser

master_statement: func | stmt;
start: NEWLINE* (master_statement NEWLINE+)* master_statement? EOF;
func: type func_decl | func_decl;
func_decl: ID params block;
type:
	BOOL_TYPE (L_BRACKET R_BRACKET)*
	| STR_TYPE (L_BRACKET R_BRACKET)*
	| NUM_TYPE (L_BRACKET R_BRACKET)*;
params: (L_PAR R_PAR | L_PAR param_lst R_PAR);
param_lst: param (COMMA param)*;
param: type ID;
block:
	L_CURLY NEWLINE* (stmt NEWLINE+)* R_CURLY
	| L_CURLY NEWLINE* R_CURLY;
stmt:
	dcl
	| assign_stmt
	| cntrol
	| func_call
	| RETURN expr
	| RETURN;
dcl: type assign_stmt | type ID;
assign_stmt: (ID | ID list_subscript) ASSIGN expr;
list_subscript: (L_BRACKET expr R_BRACKET)+;
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
		| ID list_subscript 
		| func_call
	);
cntrol: if_stmt | while_stmt;
if_stmt: IF expr block | IF expr block NEWLINE+ else_stmt;
else_stmt: ELSE if_stmt | ELSE block;
while_stmt: WHILE expr block;
func_call: ID L_PAR elmnt_list R_PAR;
elmnt_list: expr (COMMA expr)* |;