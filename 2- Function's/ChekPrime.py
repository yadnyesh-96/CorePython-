#Write a function that checks if a number is prime.

def isPrime(n):
    if n <=1:
        return "Not Prime"
        
    for i in range(2, n):
        if n%i==0:
            return "Not Prime"
        
    return "Is Prime"

num=int(input("Enter the Number :"))

print(isPrime(num))