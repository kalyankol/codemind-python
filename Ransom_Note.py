a,b=map(str,input().split())
b=list(b)
t=True
for i in range(len(a)):
    if a.count(a[i])<=b.count(a[i]):
        continue
    else:
        t=False
        break
print(t)    
    