print("Switch Cases ");

print("1. ADDITION ");
print("2. MULTIPLICATION");
print("Enter the two Values:");
a=int(input("Enter first Value:"));
b=int(input("Enter Second Values:"));

choice=int(input("Enter your Choice:"));

match choice:
		case 1:
			print("Addition is:",(a+b));
		case 2:
			print("Multiplication is:",(a*b));
		case _ :
			print("Invalid Input");
			
