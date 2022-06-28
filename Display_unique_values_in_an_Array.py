n=int(input())
l=list(map(int,input().split()))
c,s=0,0
for i in range(n):
    c=0
    for j in range(n):
        if i!=j and l[i]==l[j]:
            c+=1
    if c==0:
        print(l[i],end=' ')
        s+=1
if s==0:
    print('-1')