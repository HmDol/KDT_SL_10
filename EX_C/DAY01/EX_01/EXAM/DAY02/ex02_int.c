#include <stdio.h>
#include <limits.h>

int main(void)
{
    short s;
    unsigned short us;
    int i;
    unsigned int ui;
    long l;
    unsigned long ul;

    printf("===== short =====\n");
    printf("range : %hd ~ %hd\n", SHRT_MIN, SHRT_MAX);

    s = SHRT_MIN;
    printf("SHRT_MIN - 1 : %hd\n", --s);

    s = SHRT_MAX;
    printf("SHRT_MAX + 1 : %hd\n", ++s);

    printf("\n===== unsigned short =====\n");
    printf("range : 0 ~ %hu\n", USHRT_MAX);

    us = 0;
    printf("0 - 1 : %hu\n", --us);

    us = USHRT_MAX;
    printf("MAX + 1 : %hu\n", ++us);

    printf("\n===== int =====\n");
    printf("range : %d ~ %d\n", INT_MIN, INT_MAX);

    i = INT_MIN;
    printf("INT_MIN - 1 : %d\n", --i);

    i = INT_MAX;
    printf("INT_MAX + 1 : %d\n", ++i);

    printf("\n===== unsigned int =====\n");
    printf("range : 0 ~ %u\n", UINT_MAX);

    ui = 0;
    printf("0 - 1 : %u\n", --ui);

    ui = UINT_MAX;
    printf("MAX + 1 : %u\n", ++ui);

    printf("\n===== long =====\n");
    printf("range : %ld ~ %ld\n", LONG_MIN, LONG_MAX);

    l = LONG_MIN;
    printf("LONG_MIN - 1 : %ld\n", --l);

    l = LONG_MAX;
    printf("LONG_MAX + 1 : %ld\n", ++l);

    printf("\n===== unsigned long =====\n");
    printf("range : 0 ~ %lu\n", ULONG_MAX);

    ul = 0;
    printf("0 - 1 : %lu\n", --ul);

    ul = ULONG_MAX;
    printf("MAX + 1 : %lu\n", ++ul);

    return 0;
}
