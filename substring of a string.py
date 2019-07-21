str1,str2=map(str,input().split())
s=0
for i in range(0,len(str1)):
    for j in range(0,len(str2)):
        if str1[i]==str2[j]:
            s+=1
if s>=2:
    print("yes")
else:
    print("no")
