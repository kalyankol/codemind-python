def prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            break
    else:
        return True
n=int(input())
if prime(n):
    print('0')
else:
    p=n
    q=n
    while(1):
        p=p-1
        if prime(p):
            a=p
            break
    while(1):
        q=q+1
        if prime(q):
            b=q
            break
if n-a>b-n:
    print(b-n)
else:
    print(n-a)
            