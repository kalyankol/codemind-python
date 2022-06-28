def isdigit(k):
    q1=k
    e=0
    while(q1):
        r1=q1%10
        e=e+1
        q1=q1//10
    return e
n=int(input())
a=list(map(int,input().split()))
d=max(a)
q=d
c=0
while(q):
    r=q%10
    c=c+1
    q=q//10
b=0
for i in range(0,n):
    if isdigit(a[i])==c:
        b=b+1
print(b)