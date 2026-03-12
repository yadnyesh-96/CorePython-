"""
Q21.Write a Python program to check whether a number is a Prime Number or not.
 Example: Prime numbers from 1 to 100 are 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, etc.
"""

print("---- Check the Prime Number ----")

num=int(input("Enetr the Number: "))

print("Is Not Prime Number" if num<=1)

i=0;
while i<num:
        if(i//num==0):
            print("prime Number")