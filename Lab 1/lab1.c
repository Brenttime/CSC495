#include <stdio.h>
#include <string.h>

void hacked()
{
	puts("Hacked by Brent Turner!!!!");
}

void return_input(void)
{
	char array[30];
	gets(array);
	printf("%s\n", array);
	
}

main()
{
	return_input();	
	return 0;
}


