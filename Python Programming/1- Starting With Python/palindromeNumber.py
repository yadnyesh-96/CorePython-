# Write a Python program to check whether number is Palindrome or not.

print(" -----  Pallindrome Number ------")

num=int(input("Enter the Number: "))

temp=num
rev=0

while num!=0:
    rem=num%10
    num=num//10
    rev=rev*10+rem

if temp==rev:
    print("Number is Pallindrome")
else: 
    print("Number is not Pallindrome")
    