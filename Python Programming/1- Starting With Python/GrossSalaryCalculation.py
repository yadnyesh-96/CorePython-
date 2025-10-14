#Write a Python program to input basic salary and 
#calculate Gross salary according to:

# Basic <= 10000 : HRA = 20%, DA = 80%
# Basic <= 20000 : HRA = 25%, DA = 90%
# Basic > 20000  : HRA = 30%, DA = 95%

print("--- Calculation of Gross Salary ---")

sal=int(input("Enter the Your Basic Salary:"))

if sal>20000:	
        hra=0.30*sal
        da=0.95*sal
elif sal<=20000:
        hra=0.25*sal
        da=0.90*sal
elif sal<=10000:
        hra=0.20*sal
        da=0.80*sal
else:
	print("Not eligible ")
	
gross_sal=hra+da+sal;

print("---- Salary Deatil's ----");

print("Basic Sal   :",sal)
print("HRA         :",hra)
print("DA          :",da);
print("Gross Salary:",gross_sal);    
