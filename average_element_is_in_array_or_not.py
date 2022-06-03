n=int(input())
a=list(map(int,input().split()))
s=0
for i in a:
    s=s+i
m=s//n
c=0
for i in a:
    if i==m:
        c+=1
if c!=0:
    print(True)
else:
    print(False)
       
