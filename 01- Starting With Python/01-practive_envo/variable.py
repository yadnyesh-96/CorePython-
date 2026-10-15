
# variables and types
print(" VARIABLES AND BASIC CONCEPT'S")
print("-------------------------------------")

name = "yadnyesh"
age = 21 
salary = 38000.50

print(f"Hi {name} and type is {type(name)}")
print(f" {name} is {age} of old and type is {type(age)}")
print(f"salary of {name} is {salary} and it type is {type(salary)}")


print("-------------------------------------")
print()
print("CONDITION STATMENT'S")
print("-------------------------------------")

#conditions type

#checks number is even or odd
num = 4

if num%2==0:
    print("EVEN")
else:
    print("ODD")
    
print()


#loops 
"""
The range() function is especially important when learning loops. There are three common way's to use it

---------------------------------------------------------------
A. range(stop)
    ex. for i in range(5):
    It starts at 0 and ends before 5.  ---->  o/p: 0,1,2,3,4
    
---------------------------------------------------------------

B. range(start, stop)    
    ex. for i in range(1,6):
    It starts at 1 and ends before 6.  ----> o/p: 1,2,3,4,5
    
--------------------------------------------------------------

C. range(start, stop, step)
    ex. for i in range(2,11,2):
    here, 2 is the starting value, 11 is the stopping boundary, and 2 is the step (the amount added each time)  ----> o/p: 2,4,6,8,10
    
    ex. for i in range(5,0,-1):
    o/p: 5,4,3,2,1    ---> Remember: The stop value is excluded from the output.
     
"""

for i in range(1,4):
    print(i)
    
print("-----------\n\n")

sensor_list = ["ANPR","RFID","LiDAR","RADAR"]

print(sensor_list,"\n")

# for i in range(len(sensor_list)):
#    print(i, sensor_list[i])

for i in sensor_list:
    print(i)
    
# while loop
# A while loop runs repeatedly while its condition is true

i = 1

while i<=5:
    print(i)
    i+=1
    if i == 3:
        continue
    
#break — stop the loop
    
