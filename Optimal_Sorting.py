t=int(input())
for j in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    if a==sorted(a):
        print("0")
    else:
        print(max(a)-min(a))