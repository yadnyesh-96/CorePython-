# Q19.Write a Python program to find the sum of the first and last digit of a number.


print("----- Find the sum of the first and last digit of a number -----")

num=int(input("Enter the Number :"))
temp=num
count=0
while num!=0:
    rem=num%10
    num=num//10
    count+=1


num=temp    
first_digit=num//(10**(count-1))
Last_digit=num%10

sum=first_digit+Last_digit

print("The sum of first and last digit of",temp,"is :",sum)
