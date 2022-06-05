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
for i in range(1,n+1):
    a=int(input())
    p=a
    while(1):
        a=a-1
        if prime(a):
            l=a
            break
    while(1):
        a=a+1
        if prime(a):
            m=a
            break
    if abs(m-p)<abs(p-l):
        print(m)
    else:
        print(l)
        
            