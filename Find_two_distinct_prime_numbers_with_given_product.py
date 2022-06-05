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
c=0
d=[]
for i in range(2,n):
    for j in range(2,n):
        if i*j==n:
            if prime(i) and prime(j):
                d.append(i)
                d.append(j)
if len(d)==0:
    print("-1")
else:
    print(*sorted(set(d)))

        