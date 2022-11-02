n=int(input())
a=list(map(int,input().split()))
o=0
for i in range(0,len(a),2):
    o+=a[i]
print(o)    