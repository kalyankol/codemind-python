p,r,t=map(int,input().split())
s=p*(1+r/100)**t
a="{:.2f}".format(s)
print(a)