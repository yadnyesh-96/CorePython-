#Teen (13–19)
#Adult (20–59)
#Senior (60+)


print("---- Categories Accourding to Age ----")

age=int(input("Eter the Age:"))

res = "Senior" if age >= 60 else "Adult" if age >= 20 else "Teen"

print("Categories :",res)