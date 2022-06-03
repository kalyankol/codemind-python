n=int(input())
m=int(input())
a=[]
b=[]
s1=0
s2=0
for i in range(1,n):
    if n%i==0:
        a.append(i)
for j in range(1,m):
    if m%j==0:
        b.append(j)
for i in a:
    s1=s1+i
for j in b:
    s2=s2+j
if s1==m and s2==n:
    print('Amicable')
else:
    print('Not Amicable')
    