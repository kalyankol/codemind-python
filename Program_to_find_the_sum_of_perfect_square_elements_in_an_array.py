import math
n=int(input())
a=list(map(int,input().split()))
b=[]
sum=0
for i in range(len(a)):
    c=math.sqrt(a[i])
    if int(c+0.5)**2==a[i]:
        b.append(a[i])
for j in range(len(b)):
    sum=sum+b[j]
print(sum)    