n=int(input())
p="prime"
if(n<=1):
    p="not a prime"
else:
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            p="not a prime"
            break
print(p)        