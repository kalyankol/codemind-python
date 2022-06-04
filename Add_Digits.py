def add(n):
    s=[int(i) for i in str(n)]
    m=0
    for i in s:
        m=m+int(i)
    return m
n=int(input())
while(1):
    if add(n)<10:
        print(add(n))
        break
    else:
        n=add(n)