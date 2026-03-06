#include<stdio.h>
extern int yyparse();
extern void printTAC();
extern void printMemoryReport();

int main()
{
    yyparse();
    printTAC();
    printMemoryReport();
    return 0;
}