"""
Q16.Write a Python program to find the power of a number.
 (Hint: Use loop or ** operator)
"""

print("----- Power of Number -----")

b=int(input("Enter the Base :"))
idex=int(input("Enetr the Index :"))


i=0
res=1
while i !=idex:
    res*=b
    i+=1
    
print(res)