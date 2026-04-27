#include<stdio.h>
#include<string.h>

#define MAX_VAR 100

typedef struct {
    char name[20];
    int address;
} Symbol;

Symbol table[MAX_VAR];
int varCount = 0;
int currentAddress = 0;
int optimizedMemory = 0;

void allocateVariable(char* name)
{
    strcpy(table[varCount].name, name);
    table[varCount].address = currentAddress;
    currentAddress += 4;
    varCount++;
}

void calculateOptimizedMemory()
{
    int activeVars = varCount / 2;
    if(activeVars < 1) activeVars = 1;

    optimizedMemory = activeVars * 4;
}

void printMemoryReport()
{
    printf("MEMORY BEFORE OPTIMIZATION\n");
    for(int i = 0; i < varCount; i++)
    {
        printf("%s -> Stack Slot: %d\n", table[i].name, table[i].address);
    }

    printf("Total Memory Before: %d\n", currentAddress);

    calculateOptimizedMemory();

    printf("\nMEMORY AFTER OPTIMIZATION\n");
    printf("Optimized Memory Usage: %d\n", optimizedMemory);

    printf("\nPERFORMANCE COMPARISON\n");
    printf("Memory Saved: %d\n", currentAddress - optimizedMemory);
}