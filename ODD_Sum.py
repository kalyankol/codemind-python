n=int(input())
a=list(map(int,input().split()))
e=0
for i in range(len(a)):
    if a[i]%2!=0:
        e+=a[i]
print(e)        