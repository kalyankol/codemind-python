def prime(k):
    if k==1:
        return False
    else:
        for i in range(2,int(k**0.5)+1):
            if k%i==0:
                return False
        else:
            return True
n=int(input())
s=[int(i) for i in str(n)]
k=s[::-1]
m=''.join([str(i) for i in k])
a=int(m)
if prime(n):
    if prime(a):
        print("circular prime")
    else:
        print("prime but not a circular prime")
else:
    print("not prime")
    
    
    
    
    
                