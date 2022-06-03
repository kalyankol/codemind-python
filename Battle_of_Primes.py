def prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            break
    else:
        return True
a=int(input())
b=int(input())
c=0
while(1):
    c+=1
    s=a+b+c
    if prime(s):
        print(c)
        break