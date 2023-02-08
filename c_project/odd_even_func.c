#include <stdio.h>

void find_even(int n)
{
    if (n % 2 == 0){
        printf("even");
    }
    else if(n % 2 == 1){
        printf("odd");
    }
}

int main()
{
    int n;
    scanf("%d", &n);

    find_even(n);

    return 0;
}
