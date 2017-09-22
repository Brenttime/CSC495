#include <stdio.h>
#include <string.h>

void successfulLogin();
void incorrectPasswordError();

main()
{
    char usersPassword[8] = "secret99";
    //need to make a buffer/stack in order to overflow
    char password[8];
    gets(password);

    if(password == usersPassword)
    {
        successfulLogin();
    }
    else
    {
        incorrectPasswordError();
    }
}

void successfulLogin()
{
    printf("You password is correct, You have now logged in");    
}

void incorrectPasswordError()
{
    printf("The entered password was incorrect, please try again");    
}
