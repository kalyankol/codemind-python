t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    c=0
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a.count(a[i]+a[j])>=1:
                c+=1
    if c==0:
        c=-1
    print(c)            