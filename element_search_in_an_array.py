n=int(input())
a=list(map(int,input().split()))
s=int(input())
for i in a:
    if i==s:
        print(True)
        break
else:
    print(False)