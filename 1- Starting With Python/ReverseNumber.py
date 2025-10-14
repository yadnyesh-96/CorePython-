# Write a Python program to reverse a number without using loop.

print("----- Reverse the Given Number without using the Loop ----")

num=int(input("Enter the Number: "))

hundred=(num//100)  # 123 // 100 --> 1 
tens=((num//10)%10) # (123//10)--> 12%10--> 2
ones=(num%10)   # 123 % 10 --> 3

rev=ones*100+tens*10+hundred*1
print("Reveresed Number: ",rev)