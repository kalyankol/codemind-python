n=int(input())
a=list(map(int,input().split()))
c=a.count(a[0])
b=[]
for i in range(len(a)):
    if a.count(a[i])>c:
        c=a.count(a[i])
for i in range(len(a)):
    if a.count(a[i])==c:
        b.append(a[i])
print(min(b))        