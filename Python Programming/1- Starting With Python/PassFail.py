# 90+: A
#80–89: B
#70–79: C
#<70 : F

print("----- Grade Allocation Application -----")

mark=int(input("Enter the Mraks:"));

res= "A" if mark>90 else "B" if mark<90 and mark>80 else "C" if mark<80 and mark>=70 else "F" 

print("Result :",res)