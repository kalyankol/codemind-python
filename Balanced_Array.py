def ch(a,k):
    p=False
    c=0
    s=0
    for i in range(0,k):
        c+=a[i]
    for i in range(k+1,len(a)):
        s+=a[i]
    if s==c:
        p=True
    return p    
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    s="NO"
    for i in range(len(a)):
        if ch(a,i):
            s="YES"
            break
    print(s)    