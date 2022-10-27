def fact(n):
    s=0
    for i in range(1,n+1):
        if n%i==0:
            s+=i
    return s
n=input() 
b=[]
c=[]
for i in range(len(n)):
    if n[i]!=',':
       b.append(int(n[i]))
for i in range(len(b)):
    if b.count(fact(b[i]))==1:
        c.append(b[i])
if len(c)==0:
    print(-1)
else:
    print(*sorted(c))        
