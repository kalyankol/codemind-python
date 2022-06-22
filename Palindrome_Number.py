def pal(n):
    s=[int(i) for i in str(n)]
    m=s[::-1]
    if m==s:
        return True
    else:
        return False
n=int(input())
for i in range(n):
    a=int(input())
    if pal(a):
        print(True)
    else:
        print(False)