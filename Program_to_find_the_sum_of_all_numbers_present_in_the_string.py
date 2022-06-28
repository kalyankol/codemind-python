a=input()
sum=0
for i in range(0,len(a)):
    if a[i]<='9' and a[i]>='0':
        sum+=int(a[i])
print(sum)