#include <stdio.h>
#include <string.h>

int main(void)
{
	char str[1000001] = "";
	char* p = str;
	int len = 0;
	int cnt = 0;

	gets(str);
	len = strlen(str);

	for (p = str; *p; p++)
		if (*p == ' ')
			*p = '\0';

	for (p = str; p < str + len; p++)
	{
		if (*p != '\0')
		{
			cnt++;
			p += strlen(p);
		}
	}

	printf("%d", cnt);
	
	return 0;
}