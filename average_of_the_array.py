n=int(input())
a=list(map(int,input().split()))
s=0
for i in a:
    s+=i
avg="{:.2f}".format(s/len(a))
print(avg)