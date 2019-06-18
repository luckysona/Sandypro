s1,s2=map(int,input().split())
L=[int(i) for i in input().split()]
temp=[]
for i in range(s2):
    d=list(map(int,input().split()))
    l=d[0]
    for j in range(min(d)-1,max(d)):
        if l>L[j]:
        	l=L[j]
    temp.append(l)
for i in range(0,len(temp)):
    print(temp[i])
