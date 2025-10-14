"""
Q7.Write a Python program to find the sum of all even numbers 
between 1 to n using a while loop.
"""

print("---- Sum of all Even Numbers 1 to n ----")

n=int(input("Enter the Number:"))
i=1
sum=0;
while i<=n:
        if i%2==0:
                sum+=i
        i+=1

print("Sum of 1 to ",n," Even Number:",sum)
