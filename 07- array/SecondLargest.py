

arr=[10,5,20,8,15]

largest=0
second=0

for num in arr:
	if num > largest:
		second = largest
		largest = num
	elif num>second and num!=largest:
		second=num
	
print(second)