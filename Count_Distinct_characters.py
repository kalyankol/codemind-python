n=set(input().lower())
c=0
for i in n:
    if i==' ':
        c+=1
print(len(n)-c)