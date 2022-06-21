n=int(input())
a=list(map(int,input().split()))
b=''.join([str(i) for i in a])
c=int(b)+1
d=[int(i) for i in str(c)]
print(*d)