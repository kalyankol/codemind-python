n=int(input())
l=list(map(int,input().split()))
c,ma=0,0
for i in range(n):
    c=0
    for j in range(n):
        if l[i]==l[j]:
            c+=1
    if c>ma:
        ma=c
        o=l[i]
print(o)