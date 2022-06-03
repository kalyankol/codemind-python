n=int(input())
sum=0
a=[]
for i in range(1,n):
    if n%i==0:
        a.append(i)
for i in a:
    sum=sum+i
if sum>n:
    print(True)
else:
    print(False)