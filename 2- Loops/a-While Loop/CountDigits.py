"""
Q10.Write a Python program to count the number of digits in a 
number using a while loop.
"""

print("---- Count Digit of Number ----")

num=int(input("Enter the Number:"))

print("The Digits in Given Number ",num)

count=0

if num==0:
	print("Digits is :1")
else:
	while num!=0:
		num=num//10
		count+=1
	
print("Digits is :",count);