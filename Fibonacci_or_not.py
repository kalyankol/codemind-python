def fib(l):
    a,b=0,1
    #print(a,b,end=' ')
    c1=0
    for i in range(2,l):
        c=a+b
        if(l==c):
            c1=1
        b,a=c,b
    if c1==1:
        print(True)
    else:
        print(False)
n=int(input())
fib(n)