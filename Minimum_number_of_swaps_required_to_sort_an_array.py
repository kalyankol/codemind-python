def ch(a,k):
    c=a[k]
    r=k
    for i in range(k+1,len(a)):
        if a[i]<c:
            c=a[i]
            r=i
    return r        
n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(len(a)):
    r=ch(a,i)
    if i!=r:
        a[i],a[r]=a[r],a[i]
        c+=1
print(c)        