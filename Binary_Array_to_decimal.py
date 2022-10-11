n=int(input())
a=list(map(int,input().split()))
s=0
j=len(a)
for i in a:
    s+=i*(2**j)
    j-=1
print(int(s/2))    