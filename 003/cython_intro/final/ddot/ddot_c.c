#include "ddot_c.h"

double ddot_c(double *a, double *b, int len){
    int i;
    double dot_value = 0.0;
    for(i=0; i<len; i++){
        dot_value += a[i] * b[i];
    }

    return dot_value;
}

double ddot_f(double *a, double *b, int len){
    double dot_value;
    ddot_f_(a, b, &len, &dot_value);
    return dot_value;
}
