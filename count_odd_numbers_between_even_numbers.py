n=int(input())
a=list(map(int,input().split()))
s=0
for i in range(len(a)):
    if i-1>=0 and i+1<len(a):
        if(a[i]%2!=0 and a[i+1]%2==0 and a[i-1]%2==0):
            s+=1
print(s)            