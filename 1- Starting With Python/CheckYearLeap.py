#Write a Python program to check whether a year is Leap year or not.4

n=int(input("Enter the Year:"));

if n%4==0 and n%400==0:
	print("It is Leap Year ",n);
else:
	print("It Not the leap Year");