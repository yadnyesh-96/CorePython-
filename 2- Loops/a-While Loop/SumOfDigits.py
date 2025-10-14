"""
Q11.Write a Python program to calculate the sum of digits of a 
number using a while loop.
"""

print("--- Calculate the Sum of digit given program ---")
num=int(input("Enter the number:"))

print("Given Number is:",num)
count=0
sum=0
if num==0:
	print("The Sum of Digits :1")
    break
else:
	while num!=0:
		num=num//10
		count+=1
		sum+=count
	
print("The Sum if Digits :",sum)