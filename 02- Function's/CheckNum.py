#

print("-- check number positive/Negative/zero --")

def check_num(n):
    if(n>0):
        print(f"{n} is positive number")
    elif(n<0):
        print(f"{n} is Negative number")
    else:
        print(f"{n} is Zero ")

num=int(input("Enter the Number :"))

check_num(num)

