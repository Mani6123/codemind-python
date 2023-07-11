n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
e=[]
for i in l:
    if i>=a and i<=b:
        e.append(i)
if e==[]:
    print(-1)
else:
    print(max(e))