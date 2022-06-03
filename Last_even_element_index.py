n=int(input())
a=list(map(int,input().split()))
s=[]
for i in range(len(a)):
    if a[i]%2==0:
        s.append(i)
print(max(s))        