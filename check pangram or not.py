s=str(input())
s=s.lower()
l=len(s)
L=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in range(0,l):
	if(s[i] in L):
		L.remove(s[i])
if(len(L)==0):
	print("yes")
else:
	print("no")
