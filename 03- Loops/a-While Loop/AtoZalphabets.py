# Python program to print all alphabets from a to z using a while loop.
# (Hint: Use chr() and ord() functions.)

print("---- Alphabets from a to z -----")

ch=ord('a');

while ch<=ord('z'):
	print(chr(ch),end=' ')
	ch+=1