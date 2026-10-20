
numbers = [1, 2, 3, 2, 4, 1, 5]

seen = set()
dublicates = set()

for number in numbers:
    if number in seen:
        dublicates.add(number)
    else:
        seen.add(number)
        
print(dublicates)