#include <stdio.h>

int main()
{
    int n, i;

    for(i=1; i <= 5; i++){
        scanf("%d", &n);
        if(n % 2 == 0){
            printf("even\n");
        }
        else {
            printf("odd\n");
        }
    }

    return 0;
}
