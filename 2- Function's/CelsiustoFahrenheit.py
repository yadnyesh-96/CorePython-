#Write a function that converts Celsius to Fahrenheit. 
#Temperature in degrees Fahrenheit (°F) = (Temperature in degrees Celsius (°C) * 9/5) + 32

def fahrenheit_to_temperature(c):
    return (c*(9/5))+32

cel=int(input("Temperature in degrees Celsius (°C) :"))

res=fahrenheit_to_temperature(cel)

print("Temperature in degrees Fahrenheit (°F) =>",res)