%{
#include "parser.tab.h"
#include <string.h>
%}

%%

"int"       return INT;
[0-9]+      { yylval.str = strdup(yytext); return NUMBER; }
[a-zA-Z]+   { yylval.str = strdup(yytext); return ID; }

"="         return ASSIGN;
"+"         return PLUS;
"-"         return MINUS;
"*"         return MUL;
"/"         return DIV;

"("         return LPAREN;
")"         return RPAREN;

";"         return SEMI;

[ \t\n]     ;
.           ;

%%

int yywrap()
{
    return 1;
}