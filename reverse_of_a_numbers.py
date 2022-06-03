n=int(input())
s=[int(i) for i in str(n)]
a=s[::-1]
m=''.join([str(i) for i in a])
print(m)