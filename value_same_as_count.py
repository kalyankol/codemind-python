n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    if a.count(i)==i:
        if i not in b:
            b.append(i)
print(len(b))            