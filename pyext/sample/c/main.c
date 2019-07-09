#include <stdio.h>
#include <math.h>

#include "sample.h"

//extern int gcd(int x, int y);

int main(void) {

    printf("%d\n", gcd(10, 5));
    Point a = {0, 0}, b = {1, 1};
    printf("%f\n", distance(&a, &b));

    return 0;
}
