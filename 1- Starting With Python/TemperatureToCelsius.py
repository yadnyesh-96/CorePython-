# Write a Python program to enter temperature in Fahrenheit and convert it to Celsius.
# Formula:
# cel = (fah - 32) * 5 / 9

print("---- Temperature in Fahrenheit To Convert it Celsius ----");

temp=int(input("Enter the Temperature in Fahrenheit : \n"));

cel=(temp -32)*5//9;
print("Temperature F in the Celsius is: ",cel);


print("------------------------")