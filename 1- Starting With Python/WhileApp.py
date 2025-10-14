no=int(input("Enter the Number:"));

rev=0;

while no!=0:
	
	rem=no%10;
	no=no//10;
	rev=rev*10+rem;
	
print(rev);

print(range(5));