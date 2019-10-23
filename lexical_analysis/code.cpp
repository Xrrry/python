#include<stdio.h>
#include<string.h>
int main()
{
	char a[100],b[20],c[20];
	int i,j,k,len,count=10,0a;
	printf("please input a string:\n");
	scanf("%[^\n]",a);
	getchar();
	printf("please input the string\t you want:\n");
	gets(b); //注释
	len=strlen(b);
	for(i=0;a[i]!=0;i++)
	{
		for(j=0,k=i;j<len;j++)
			c[j]=a[k++];
		if(strcmp(b,c)==0)
		{
			count++;
		}	
	}
	printf("the times your string appears are %d\n",count);
	return 0;
}
