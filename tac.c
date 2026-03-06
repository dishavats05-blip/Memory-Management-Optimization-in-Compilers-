#include<stdio.h>
#include<string.h>
#define MAX_TAC 100
typedef struct 
{
    char op[10];  
    char arg1[20];
    char arg2[20];
    char result[20];
}TAC;
TAC tacTable[MAX_TAC];
int tacIndex=0;
void generateTAC(char* op, char* arg1, char* arg2, char* result)
{
    strcpy(tacTable[tacIndex].op,op);
    strcpy(tacTable[tacIndex].arg1,arg1);
    strcpy(tacTable[tacIndex].arg2,arg2);
    strcpy(tacTable[tacIndex].result,result);
    tacIndex++;
}
void printTAC()
{
    printf("THREE ADDRESS CODE\n");
    for(int i=0; i < tacIndex; i++)
    {
        if(strcmp(tacTable[i].op, "=")== 0)
        {
            printf("%s = %s\n", tacTable[i].result, tacTable[i].arg1);
        }
        else
        {
            printf("%s = %s %s %s\n", tacTable[i].result,tacTable[i].arg1, tacTable[i].op, tacTable[i].arg2);
        }
    }
}
int getTACCount()
{
    return tacIndex;
}