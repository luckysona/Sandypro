s1=int(input())
s2=list(map(int,input().split()))
s=[]
a=1
for i in range(0,s1-1):
    if (s2[i]<s2[i+1]):
        a+=1
    else:
        s.append(a)
        a=1
s.append(a)
print(max(s))
