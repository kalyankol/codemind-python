n=int(input())
a=list(map(int,input().split()))
s="yes"
for i in range(len(a)):
    if i+1<n:
        if a[i]<a[i+1]:
            continue
        else:
            s="no"
            break
print(s)        
    