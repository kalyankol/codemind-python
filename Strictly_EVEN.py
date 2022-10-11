n=int(input())
a=list(map(int,input().split()))
s=True
for i in range(len(a)):
    if(a[i]%2==0):
        if(i%2!=0):
            s=False
print(s)            