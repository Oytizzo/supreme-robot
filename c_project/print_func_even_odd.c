#include <stdio.h>

void print_even_odd(int x)
{
    if(x % 2 == 0){
        printf("The number is even\n");
    }
    else{
        printf("The number is odd\n");
    }
}

int main()
{
    int a;
    print_even_odd(6);
    return 0;
}
