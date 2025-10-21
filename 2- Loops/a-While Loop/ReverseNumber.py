"""
Q13.Write a Python program to enter a
 number and print its reverse using a while loop.
"""

print("----- Reverse the Number ----")

num=int(input("Enter the number:"))
rev=0;
while 0!=num:
		rem=num%10
		rev=rev*10+rem
		num=num//10

print("Reversed Number:",rev)