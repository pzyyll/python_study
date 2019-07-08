#include <stdio.h>
#include <stdlib.h>
#include <dlfcn.h>

void *GetFuncPtr(void *so_ptr, const char *funcname) {
    void *fptr = dlsym(so_ptr,  funcname);
    if (!fptr) {
        fprintf(stderr, "func null\n");
        return NULL;
    }
    return fptr;
}

int main(int argc, char *argv[]) {
    int (*fptr)(int, int);

    void *sample_lib = dlopen("libsample.so", RTLD_LAZY|RTLD_GLOBAL);

    if (!sample_lib) {
        fprintf(stderr, "Could not open libsample.so\n");
    }

    fptr = GetFuncPtr(sample_lib, "gcd");

    printf("result: %d\n", fptr(10, 5));

    return 0;
}
