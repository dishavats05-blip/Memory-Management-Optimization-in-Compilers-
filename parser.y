%{
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include "tac.h"
#include "memory.h"

extern int yylex();
void yyerror(char *s);

int tempCount=0;
char temp[10];
%}

%union
{
    char* str;
}

%token <str> ID NUMBER
%token INT ASSIGN PLUS MUL SEMI
%type <str> expr

%%
program:
    stmt_list
    ;

stmt_list:
    stmt_list stmt
    | stmt
    ;

stmt:
    INT ID SEMI{
        allocateVariable($2);
    }
    |
    ID ASSIGN expr SEMI
    {
        generateTAC("=", $3, "", $1);
    }
    ;

expr:
    expr PLUS expr
    {
        sprintf(temp, "t%d", tempCount++);
        generateTAC("+", $1, $3, temp);
        $$ = strdup(temp);
    }
    |
    expr MUL expr{
        sprintf(temp, "t%d", tempCount++);
        generateTAC("*", $1, $3, temp);
        $$ = strdup(temp);
    }
    |
    ID {$$ = $1;}
    |
    NUMBER{$$= $1;}
    ;
%%
void yyerror(char* s)
{
    printf("Parse Error\n");
}