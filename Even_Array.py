n=int(input())
a=list(map(int,input().split()))
s=True
for i in a:
    if i%2!=0:
        s=False
        break
print(s)    