n=int(input())
a=list(map(int,input().split()))
for i in range(len(a)):
    for j in range(len(a)-1,-1,-1):
        if i==j:
            break
        if a.count(a[i])<a.count(a[j]):
            a[i],a[j]=a[j],a[i]
b=[]
c=[]
for i in a:
    if (i not in b) and a.count(i)>1:
        b.append(i)
for i in a:
    if a.count(i)==1:
        c.append(i)
c=sorted(c)
print(*(b+c))