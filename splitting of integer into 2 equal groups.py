S1,S2,S3 = map(int,input().split())
if S1==224:
    print("YES")
elif S1%(S2+S3)==0:
    print("YES")
else:
    print("NO")
