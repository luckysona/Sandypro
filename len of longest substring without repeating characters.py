s=str(input())
r=[]  
for i in s:
  if i not in r:
    r.append(i) 
  else:
    break
print(len(r))
