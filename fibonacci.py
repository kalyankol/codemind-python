n=int(input())
a,b=0,1
c=0
d=[]
while(c<n):
    d.append(a)
    t=a+b
    a=b
    b=t
    c+=1
print(*d)    
    