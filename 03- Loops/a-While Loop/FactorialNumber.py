"""
Q17.Write a Python program to find all factors of a number using a while loop.
"""


print("----- Factor of Number -----")

num=int(input("Enter the Number :"))

i=num
fac=1
while i != 0:
    fac*=i
    i-=1

print("Factorial of Given Number is : ",fac)