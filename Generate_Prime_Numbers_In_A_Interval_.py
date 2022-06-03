def prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            break
    else:
        return True
n=int(input())
m=int(input())
for i in range(n,m):
    if prime(i) and i!=1:
        print(i)