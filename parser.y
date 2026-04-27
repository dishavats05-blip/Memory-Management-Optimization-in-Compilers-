%{
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include "tac.h"
#include "memory.h"
#include "semantic.h"

extern int yylex();
void yyerror(char *s);

int tempCount = 0;
char temp[10];
%}

%union {
    char* str;
}

%token <str> ID NUMBER
%token INT ASSIGN PLUS MINUS MUL DIV SEMI LPAREN RPAREN
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
    INT ID SEMI {
        // 🔹 Declaration Phase
        allocateVariable($2);
        declareVar($2);
    }
    |
    ID ASSIGN expr SEMI {
        // 🔹 Semantic Check
        checkVariable($1);

        // 🔹 TAC Generation
        generateTAC("=", $3, "", $1);
    }
    ;

expr:
    expr PLUS expr {
        sprintf(temp, "t%d", tempCount++);
        generateTAC("+", $1, $3, temp);
        $$ = strdup(temp);
    }
    |
    expr MINUS expr {
        sprintf(temp, "t%d", tempCount++);
        generateTAC("-", $1, $3, temp);
        $$ = strdup(temp);
    }
    |
    expr MUL expr {
        sprintf(temp, "t%d", tempCount++);
        generateTAC("*", $1, $3, temp);
        $$ = strdup(temp);
    }
    |
    expr DIV expr {
        sprintf(temp, "t%d", tempCount++);
        generateTAC("/", $1, $3, temp);
        $$ = strdup(temp);
    }
    |
    LPAREN expr RPAREN {
        $$ = $2;
    }
    |
    ID {
        // 🔹 Semantic Check for usage
        checkVariable($1);
        $$ = $1;
    }
    |
    NUMBER {
        $$ = $1;
    }
    ;

%%

void yyerror(char* s)
{
    printf("Parse Error\n");
}