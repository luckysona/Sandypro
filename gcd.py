import math
import functools
inp11,inp31=map(int,input().split())
List=[int(j) for j in input().split()]
for j in range(inp31):
    n,k=map(int,input().split())
    temp=functools.reduce(math.gcd,List[n-1:k])
    print(temp)
