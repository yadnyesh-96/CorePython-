# Write a Python program to find first and last digit of a three-digit number without using loop.

print("----- To find First and last Digit of 3-digit Number -----")

num=int(input("Enter the Three Digit Number: "))

firstdigit=num//100
lastdigit=num%10

print("Last Digit is: ",lastdigit)
print("First Digit is: ",firstdigit)
