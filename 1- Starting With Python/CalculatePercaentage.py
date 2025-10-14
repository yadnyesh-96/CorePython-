# Write a Python program to enter marks of five subjects and calculate total marks and percentage.

print("---- To calculate the Percentage of Five Subjects -----")

sub1=int(input("Enter the 1st Subject Marks: "))
sub2=int(input("Enter the 2nd Subject Marks: "))
sub3=int(input("ENter the 3rd Subject Marks: "))
sub4=int(input("Enter the 4th Subject Marks: "))
sub5=int(input("Enter the 5th Subject Mraks: "))

total=sub1+sub2+sub3+sub4+sub5;
per=total/5;

print("Total Marks is the: ",total," \nPercentage: ",per,"%")