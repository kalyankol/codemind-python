def num(n):
    d=[int(k) for k in str(n)]
    c=0
    for j in d:
        if j%10==0:
            continue
        elif n%j==0:
            c+=1
    if c==len(d):
        return True
    else:
        return False
a=int(input())
b=int(input())
l=[]
for i in range(a,b+1):
    if num(i)==True:
        l.append(i)
print(*l)        
        
    
        