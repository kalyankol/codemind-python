def prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            break
    else:
        return True
def pal(n):
    s=[int(i) for i in str(n)]
    m=s[::-1]
    a=''.join([str(i) for i in m])
    q=int(a)
    if n==q:
        return True
    else:
        return False
n=int(input())
m=n
while(1):
    m=m+1
    if pal(m) and prime(m):
        print(m)
        break
    
    
        