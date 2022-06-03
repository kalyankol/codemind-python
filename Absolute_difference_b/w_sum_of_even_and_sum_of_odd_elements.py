n=int(input())
a=list(map(int,input().split()))
s=0
p=0
for i in a:
    if i%2==0:
        s=s+i
    else:
        p=p+i
print(abs(s-p))        