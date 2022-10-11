n=int(input())
a=list(map(int,input().split()))
s=0
c=0
for i in a:
    s+=i
avg=s//len(a)
for i in a:
    if i>=avg:
        c+=1
print(c) 
#print(a,avg)
    