# Write a Python program to check whether a number is Neon or not.
# Explanation: Square the number → Sum digits of square → Check equals to number.

print("--- Check Number Neon -----")

num=int(input("Enter the Number: "))
temp=num

sqr=num**2
sum=0 

while sqr!=0:
        rem=sqr%10
        sum+=rem
        sqr=sqr//10
        

if num==sum:
    print("Number is Neon")
else:
    print("Number is not Neon")