"""
Q9.Write a Python program to print a
 multiplication table of any number using a while loop.
"""

print("---- Multiplication Table ----")

n=int(input("Enter the Number :"))
i=1;

while i<=n:
	print(i,"X",n," = ",i*n)
	i+=1
	