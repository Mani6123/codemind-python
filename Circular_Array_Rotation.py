a,b,c=map(int,input().split())
d=list(map(int,input().split()))
for i in range(b):
    d.insert(0,d[-1])
    d.pop()
for i in range(c):
    e=int(input())
    print(d[e])