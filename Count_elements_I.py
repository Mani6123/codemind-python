a,b=map(int,input().split())
c=set(map(int,input().split()))
d=set(map(int,input().split()))
e=c.intersection(d)
print(len(e))