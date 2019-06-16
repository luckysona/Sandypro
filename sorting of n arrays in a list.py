A=int(input())
B=[]
for i in range(A):
  L=[]
  L=list(map(int,input().split()))
  B.append(L)
s=[]   
for i in B:
  for j in i:
    s.append(j)
s.sort()
for k in s:
  print(k,end=" ") 
