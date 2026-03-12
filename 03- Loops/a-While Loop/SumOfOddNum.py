"""
Q8.Write a Python program to find the sum of all odd numbers
 between 1 to n using a while loop.
"""
print("----- Sum of Odd Number -----")

n=int(input("Enter the Number:"))

i=1
sum=0
while i<=n:
		if i%2!=0:
				sum+=i
		i+=1
	
print("Sum of All Odd Number is: ",sum)