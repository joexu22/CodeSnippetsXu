#include<stdio.h>
#include<stdlib.h>

int main()
{
	long long n,m,i,j,k;
	char ch;
	int flg;
	char s[100];
	printf("\nDFA IMPLEMENTATION\n\n");
	printf("\nEnter Number of States: ");
	scanf("%Ld",&n);	//n->no. of states
	long long a[n][2];  //Store State Transition Table
	int final[n];		//Stores whether state is final(value=1) or non-final(value=0)
	printf("\nEnter State Transition Table(-1 for Dead State)(0 Base Indexing):\n\n");
	for(i=0;i<n;i++)
	{
		printf("%Ld: ",i);
		scanf("%Ld %Ld",&j,&k);	//j->Transition of state for 0 and k->Transition of state for 1
		a[i][0]=j;
		a[i][1]=k;
		final[i]=0;				//Initialize all states as Non-final state
	}
	printf("\nEnter Number Of Final States: ");
	scanf("%Ld",&m);	//m->no. of final states
	printf("\nEnter Final States:\n");
	for(i=0;i<m;i++)
	{
		scanf("%Ld",&k);
		final[k]=1;		//marking final states
	}
	
	while(1)
	{
		printf("\nEnter String(BinarY OnlY): ");
		scanf("%s",s);			
		flg=0;
		i=0;
		j=0;
		while(s[i]!='\0')
		{
			j=a[j][s[i]-48];
			printf("%Ld ",j);
			if(j<0)	break;
			i++;
		}
		printf("\nEnd State: %Ld\n",j);
		if(final[j])
			printf("\nVALID STRING\n");
		else
			printf("\nINVALID STRING\n");
		printf("\nDo You want to enter another String?(Y/N): ");
		scanf(" %c",&ch);
		if(ch!='Y'&&ch!='y')
			break;
	}
	return 0;
}