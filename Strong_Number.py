def fact(r):
    mul=1
    while r!=0:
        mul=mul*r
        r-=1
    return mul
n=int(input())
t=n
sum=0
while n!=0:
    r=n%10
    sum+=fact(r)
    n//=10
if sum==t:
    print("The number {} is a strong number".format(t))
else:
    print("The number {} is not a strong number".format(t))