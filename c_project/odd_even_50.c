#include <stdio.h>

int main()
{
    int n, i;

    //for(i=1; i <= 10; i++){
    //    scanf("%d", &n);
    //    if(n % 2 == 0){
    //        printf("even\n");
    //    }
    //    else {
    //        printf("odd\n");
    //    }
    //}
    i = 1;
    while(i <= 10){
        scanf("%d", &n);
        if(n % 2 == 0){
            printf("even\n");
        }
        else {
            printf("odd\n");
        }
        i++;
    }

    return 0;
}
