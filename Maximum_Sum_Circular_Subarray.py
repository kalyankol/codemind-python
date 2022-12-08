n=int(input())
a=list(map(int,input().split()))
m=max(a)
for i in range(len(a)):
    for j in range(i+1,len(a)):
        s=0
        for k in range(i,j):
            s+=a[k]
        if s>m:
            m=s
if a[0]+a[-1]>m:
    m=a[0]+a[-1]
print(m)        