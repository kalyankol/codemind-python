def prime(k):
    if k==1:
        return False
    else:
        for i in range(2,int(k**0.5)+1):
            if k%i==0:
                return False
                break
        else:
            return True
n=int(input())
d=[]
c=0
for i in range(1,n+1):
    if n%i==0:
        d.append(i)
for i in d:
    if prime(i):
        c+=1
print(len(d)-c)        
    
    
    
    
    
    
    