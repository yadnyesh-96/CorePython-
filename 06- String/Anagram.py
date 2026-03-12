

str1 = "listen"
str2 = "silent"

f = [0]*26

for i in range(len(str1)):
	f[ord(str1[i])-97]+=1
	f[ord(str2[i])-97]-=1
	
flag=True

for v in f:
	if v!=0:
		flag=False;
		break
		
print("Anagram" if flag else "Not anagram");