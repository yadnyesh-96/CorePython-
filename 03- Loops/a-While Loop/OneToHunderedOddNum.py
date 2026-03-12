#Write a Python program to print all odd numbers 
#between 1 to 100 using a while loop.

print("------- 1 To 100 odd Number -----")

i=1;

while i<=100:
	if i%2!=0:
		print(i,end=' ')
	i+=1