s1 = int(input())
s2 = list(map(int, input().split()))
s3 = int(len(s2)/2)
if sum(s2[:s3])//len(s2[:s3]) == sum(s2[s3:])//len(s2[s3:]):
    print('yes')
else:
    print('no')
