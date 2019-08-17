s1=int(input())
s2=list(map(int,input().split()))
L=[]
l=1
for i in s2:
  if i not in L:
    L.append(i)
for i in range(len(L)-1):
  if (L[i]<L[i+1]):
    l+=1
print(l)
