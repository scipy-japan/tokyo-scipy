#include <stdio.h>
#include "struct_test.h"


void initStruct(myStruct *mst){
    mst->a = 0; mst->b = 0;
    mst->x = 0.0; mst->y = 0.0;
}

void showStruct(myStruct *mst){
    printf("a = %d, b = %d\n", mst->a, mst->b);
    printf("x = %f, y = %f\n", mst->x, mst->y);
}

