#include <stdio.h>

int main(void)
{
	int N[1000];

	int n;

	scanf("%d", &n);

	int i;

	for (i = 0; i < n; i++)
		scanf("%d", &N[i]);

	int j;
	int tmp;

	for (i = 0; i < n - 1; i++)
	{
		for (j = 0; j < n - 1; j++)
		{
			if ((N[j] > N[j + 1]))
			{
				tmp = N[j];
				N[j] = N[j + 1];
				N[j + 1] = tmp;
			}
		}
	}
	
	for (i = 0; i < n; i++)
		printf("%d\n", N[i]);


	return 0;
}