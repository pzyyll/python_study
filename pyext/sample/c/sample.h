#ifndef PYEXT_SAMPLE_H
#define PYEXT_SAMPLE_H

int gcd(int x, int y);
int in_mandel(double x0, double y0, int n);
int divide(int a, int b, int *remainder);
double avg(double *a, int n);

typedef struct Point {
    double x, y;
} Point;
double distance(Point *p1, Point *p2);


#endif // PYEXT_SAMPLE_H
