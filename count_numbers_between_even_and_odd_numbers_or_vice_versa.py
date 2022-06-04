n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(len(a)):
    if i>0 and i<n-1:
        if a[i-1]%2==0 and a[i+1]%2!=0:
            c+=1
        elif a[i+1]%2==0 and a[i-1]%2!=0:
            c+=1
print(c)            
        