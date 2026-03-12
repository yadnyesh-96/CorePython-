#Write a function that returns the factorial of a number.(Use loop, not recursion)**

print("---  Calculate the Factorial of the Number ---")

def fac_number(n):
    fac=1
    for i in range(1,n+1):
        fac=fac*i
    return fac

num=int(input("Enter the number:"))

res=fac_number(num)

print(f"{num} -> factorial is =>{res}")