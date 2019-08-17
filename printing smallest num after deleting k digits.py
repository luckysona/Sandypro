from itertools import combinations
d1,d2=map(int,input().split())
g=len(str(d1))
H=list(combinations(str(d1),g-d2))
H=(sorted(H))
l="".join(H[0])
print(l)
