#include <stdio.h>

int main()
{
    int a, n, c, i;

    scanf("%d", &a);

    i = 1;

    while(i <= a) {
        scanf("%d", &n);
        if(n % 2 == 0){
            printf("even");
        }
        else {
            printf("odd");
        }
        i++;
    }

    return 0;
}
