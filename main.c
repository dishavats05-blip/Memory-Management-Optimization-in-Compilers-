#include<stdio.h>

extern int yyparse();
extern void printTAC();
extern void printMemoryReport();


extern void generateTargetCode();
extern void registerAllocation();

int main()
{
    printf("===== COMPILER OUTPUT =====\n\n");
    yyparse();

    printf("\n============================\n");
    printf("THREE ADDRESS CODE (TAC)\n");
    printf("============================\n");
    printTAC();

    printf("\n============================\n");
    printf("MEMORY OPTIMIZATION\n");
    printf("============================\n");
    printMemoryReport();

    printf("\n============================\n");
    printf("TARGET CODE GENERATION\n");
    printf("============================\n");
    generateTargetCode();

    printf("\n============================\n");
    printf("REGISTER ALLOCATION\n");
    printf("============================\n");
    registerAllocation();

    printf("\n============================\n");
    printf("Optimization Applied: Variable Lifetime Analysis\n");
    printf("============================\n");

    return 0;
}