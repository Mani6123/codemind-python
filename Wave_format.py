a=int(input())
b=list(map(int,input().split()))
c=[]
x=min(b)
for i in range(a//2):
    b.sort()
    d=b[-2]
    e=b[-1]
    c.append(d)
    c.append(e)
    b.remove(d)
    b.remove(e)
if a%2!=0:
    c.append(x)
print(*c)