#include <studio.h>
#include <string.h>

main()
{
    usersPassword = "secret99";
    //need to make a buffer/stack in order to overflow
    char[8] password;
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