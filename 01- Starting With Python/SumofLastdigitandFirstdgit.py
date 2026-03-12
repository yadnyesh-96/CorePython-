# Write a Python program to calculate sum of first and last digit of a number without using loop

print("---- To find the sum of last and first digit sum of three digit number -----")

num=int(input("Enter the Number: "))

firstdigit=num//100
lastdigit=num%10

print("Entered Number is:",num)
print("First digit is:",firstdigit)
print("Last digit is: ",lastdigit)
print("Sum of last and first digit is:",firstdigit+lastdigit)