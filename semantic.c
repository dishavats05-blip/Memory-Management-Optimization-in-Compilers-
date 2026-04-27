#include<stdio.h>
#include<string.h>

#define MAX 100

char declared[MAX][20];
int declCount = 0;

void declareVar(char* name)
{
    strcpy(declared[declCount++], name);
}

int isDeclared(char* name)
{
    for(int i=0;i<declCount;i++)
    {
        if(strcmp(declared[i], name)==0)
            return 1;
    }
    return 0;
}

void checkVariable(char* name)
{
    if(!isDeclared(name))
    {
        printf("Semantic Error: Variable '%s' not declared\n", name);
    }
}