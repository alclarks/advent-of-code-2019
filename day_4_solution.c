#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

#define PW_LEN 6

bool
is_increasing(int *digits)
{
    int i;
    for (i = 1; i < PW_LEN; i++) {
        if (digits[i] < digits[i-1]) {
            return false;
        }
    }
    return true;
}

bool
has_double(int *digits)
{
    int i;
    for (i = 1; i < PW_LEN; i++) {
        if (digits[i] == digits[i-1]) {
            return true;
        }
    }
    return false;
}

bool
has_exact_double(int *digits)
{
    int i;
    int ext_array[PW_LEN + 2];
    ext_array[0] = -1;
    ext_array[7] = -1;
    for (i = 0; i < PW_LEN; i++) {
        ext_array[i+1] = digits[i];
    }
    for (i = 1; i < PW_LEN; i++) {
        if ((ext_array[i] == ext_array[i+1])
            && (ext_array[i-1] != ext_array[i])
            && (ext_array[i+1] != ext_array[i+2])) {
            return true;
        }
    }
    return false;
}

int main()
{
    int start = 248345;
    int   end = 746315;
    int count1 = 0;
    int count2 = 0;
    int     i;
    int     j;
    int     n; /* Copy of i that gets mutated throughout the loop */
    int  array[PW_LEN];

    for (i = start; i < end; i++) {
        /* Generate int array of digits of i */
        n = i;
        for (j = 0; j < PW_LEN; j++) {
            array[PW_LEN - 1 - j] = n % 10;
            n = n / 10;
        }
        if (is_increasing(array) && has_double(array)) {
            count1 = count1 + 1;
            /* The passwords in part 2 are a subset of passwords in part 1 */
            if (has_exact_double(array)) {
                count2 = count2 + 1;
            }
        }
    }
    printf("Part 1 solution: %d\n", count1);
    printf("Part 2 solution: %d\n", count2);

    return(0);
}