n=int(input())
a=list(map(int,input().split()))
b=n//2
c=a[:b]
d=a[b:]
e=[]
for i in range(0,b):
    e.append(c[i])
    e.append(d[i])
print(*e)    
    