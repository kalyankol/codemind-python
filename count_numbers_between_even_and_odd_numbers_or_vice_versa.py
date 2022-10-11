n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(len(a)):
    if i-1>=0 and i+1<n:
        if((a[i-1]%2!=0 and a[i+1]%2==0) or (a[i-1]%2==0 and a[i+1]%2!=0)):
            c+=1
print(c)            