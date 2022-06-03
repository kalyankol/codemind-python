n=int(input())
sum=0
p=1
s=[int(i) for i in str(n)]
for i in s:
    sum=sum+i
for i in s:
    p=p*i
if sum==p:
    print("Spy Number")
else:
    print("Not Spy Number")