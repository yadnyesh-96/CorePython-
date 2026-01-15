# Q20.Write a Python program to swap first and last digits of a number.

print("---- Swap First and Last digit of Number ----")

num =int(input("Enter the Number : "))
temp=num
count=0
print("Before the swap first and Last digit: ",num)
first_digit=num//(10**(count-1)) #  7
last_digit=num%10                #  4

n=(num%(10**(count-1)))//10   # 89

swap1=last_digit*(10**(count-1)) # 4890

print("After the swap first and Last digit: ",swap1+(n*10)+first_digit)
