n=int(input())
a=list(map(int,input().split()))
s=True
for i in a:
    if i!=0 and i!=1:
        s=False
        break
print(s)  
