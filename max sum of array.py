n=int(input())
s=list(map(int,input().split()))
L=[]
d=0
for i in range(0,n-2):
	for j in range(i,n,2):
		d=d+s[j]
	L.append(d)
	d=0
L.sort()
print(L[-1])
