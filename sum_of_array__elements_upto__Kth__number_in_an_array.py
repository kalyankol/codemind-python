n=int(input())
a=list(map(int,input().split()))
k=int(input())
s=0
k1=0
for i in range(len(a)):
    if a[i]==k:
        k1=i
        break
for i in range(len(a)):
    if i<=k1:
        s=s+a[i]
print(s)        
        
        