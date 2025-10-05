# Write a Python program to check whether a number is Spy Number or not.
# (Sum of digits = Product of digits)

print("--- Check Number is Spy or not ----")

num=int(input("Enter the Number: "))
temp=num
sum=0
prd=1

while num!=0:
    rem=num%10
    num=num//10
    sum+=rem
    prd*=rem
    
if sum==prd:
    print("Number is Spy")
else:
    print("Number is Not Spy")