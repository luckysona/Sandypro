s1,r1=list(map(int,input().split()))
s2,r2=list(map(int,input().split()))  
s3,r3=list(map(int,input().split()))  
s4,r4=list(map(int,input().split())) 
l=r2-r1
m=r3-r4
n=s3-s2
o=s4=s1
if(l==m==n==o):
  print("yes")
else:
  print("no")
