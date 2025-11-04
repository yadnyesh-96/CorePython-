# Q18.Write a Python program to find the first and last digit of a number.

num=int(input("Enter the Number : "))
temp=num
count =0
while num!=0:
    rem=num%10
    num=num//10
    count+=1


num=temp
print("First Digit is :",num//10**(count-1))

    