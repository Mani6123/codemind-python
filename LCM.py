a,b=map(int,input().split())
i=max(a,b)
c=i
while i>0:
    if i%a==0 and i%b==0:
        print(i)
        break
    i+=c