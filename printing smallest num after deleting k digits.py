from itertools import combinations
num1,num2=map(int,input().split())
g=len(str(num1))
H=list(combinations(str(num1),g-num2))
H=(sorted(H))
l="".join(H[0])
print(l)
