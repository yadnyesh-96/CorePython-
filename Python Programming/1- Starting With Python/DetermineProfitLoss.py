#Write a Python program to input cost price and 
#selling price and check Profit or Loss.

cost=int(input("Enter the Coast Price:"))

sell=int(input("Enter the Selling price:"))

if sell>cost:
	print("Profit ")
elif sell<cost:
	print("Loss")
else:
	print("selled")