n=int(input())
a=list(map(int,input().split()))
c=[]
for i in range(0,n):
    for j in range(0,n):
        if i<j:
            b=a[i:j+1]
            sum=0
            for k in range(len(b)):
                sum+=b[k]
            c.append(sum)
d=a+c
print(max(d))