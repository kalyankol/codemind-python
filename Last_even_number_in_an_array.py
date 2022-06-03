n=int(input())
a=list(map(int,input().split()))
s=[]
for i in a:
    if i%2==0:
        s.append(i)
print(s[-1])        