N,P,Q,R=map(int,input().split())
s=list(map(int,input().split()))
L=[]
for i in range(0,len(s)):
    for j in range(i,len(s)):
        for k in range(j,len(s)):
            L.append(P*s[i]+Q*s[j]+R*s[k])
print(max(L))
