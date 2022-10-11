n=int(input())
a=list(map(int,input().split()))
k=int(input())
if a.count(k)>=1:
    print(True)
else:
    print(False)