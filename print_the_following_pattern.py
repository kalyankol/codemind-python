a=int(input())
l=a
for i in range(a+64,64,-1):
    for j in range(1,l+1):
            print(chr(i),end=' ')
    l-=1
    print()