s1=int(input())  
s2=[int(i) for i in input().split()]
s2=[bin(i)[2:] for i in  s2]  
s2.sort(reverse=True) 
s=[int(i,2) for i in s2]
for i in s:
	print(i)
