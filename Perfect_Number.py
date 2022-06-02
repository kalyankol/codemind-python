n=int(input())
l=[]
sum=0
for i in range(1,n+1):
    if n%i==0 and i!=n:
        l.append(i)
for i in range(len(l)):
    sum=sum+l[i]
if sum==n:
    print(True)
else:
    print(False)