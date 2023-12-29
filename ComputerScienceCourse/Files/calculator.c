#include <cs50.h>
#include <stdio.h>

int main(void)
{

    //  Prompt user for x
    int first_number = get_int("x: ");
    // Prompt user for y
    int second_number = get_int("y: ");
    printf("%i\n, first_number + second_number");
}