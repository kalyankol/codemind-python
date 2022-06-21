n=int(input())
a=list(map(int,input().split()))
b=[]
c=[]
for i in range(len(a)):
    if i<int(n/2):
        b.append(a[i])
    else:
        c.append(a[i])
print(*(c[::-1]+b[::1]))        