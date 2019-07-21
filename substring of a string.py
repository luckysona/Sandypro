def check(str1,str2): 
	if (str1.find(str2) == -1): 
		print("no") 
	else: 
		print("yes") 
str1,str2=input().split()
check(str1,str2) 
