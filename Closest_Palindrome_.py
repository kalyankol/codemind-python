def pal(k):
    n=[int(i) for i in str(k)]
    m=n[::-1]
    l=''.join([str(i) for i in m])
    if int(l)==k:
        return True
    else:
        return False
n=int(input())
b=[]
i=1
j=1
while(1):
    q=n+i
    if(pal(q)):
        b.append(q)
        break
    i+=1
while(1):
    l=n-j
    if(pal(l)):
        b.append(l)
        break
    j+=1
if abs(max(b)-n)==abs(n-min(b)):
    print(min(b),max(b))
else:
    print(min(b))
    
    
    
    
    