# Write a Python program to convert seconds to hours, minutes, and seconds.

print(" ----- Seconds to Hours to Minutes & Seconds -----")

sec=int(input("Enter the Seconds(sec): "))

m=sec/60
hr=m/60
s=m*60

print("---------------")
print(f"{hr:.2f} H",m,"M",s,"S")
print("---------------")