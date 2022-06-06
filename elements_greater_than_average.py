n=int(input())
a=list(map(int,input().split()))
s=0
avg=0
c=0
for i in a:
    s=s+i
avg=s//n
for i in a:
    if i>=avg:
        c+=1
print(c)        
    