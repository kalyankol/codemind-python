n=int(input())
i=0
p=0
s=0
j=n-1
for i in range(n):
    b=list(map(int,input().split()))
    p+=b[i]
    i+=1
    s+=b[j]
    j-=1
print("Principal Diagonal:"+str(p))
print("Secondary Diagonal:"+str(s))