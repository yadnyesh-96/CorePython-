'''
Q21.  Write a java program to check Number Is Prime Number or Not.
Example : A prime number is a number that can only be divided by itself and 1 without remainders.The prime numbers from 1 to 100 are: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97.
'''


n = int(input("Enter the number: "))

if n <= 1:
    print("Not a prime number")
else:
    for i in range(2, n//2 + 1):
        if n % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")
