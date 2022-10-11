n=int(input())
a=list(map(int,input().split()))
s=0
for i in a:
    s+=i
if a.count(int(s/len(a)))>=1:
    print(True)
else:
    print(False)