# Write a function that takes two numbers and returns the larger one

print("---- Print Max Number ----")

def max_num(a,b):
    if(a>b):
        return a
    elif(b>a):
        return b
    else:
        return "Both Equal"

num1=int(input("Enter the 1st Number:"))

num2=int(input("Enter the 2nd Number:"))

res=max_num(num1,num2)

print("Maximum Number is:",res)