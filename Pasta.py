n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
s=0
for i in b:
    if a.count(i)>=1:
        s+=1
        a.remove(i)
if s==len(b):
    print("Yes")
else:
    print("No")
