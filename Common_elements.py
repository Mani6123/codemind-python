a,b=map(int,input().split())
c=list(map(int,input().split()))
d=list(map(int,input().split()))
e=[]
for i in c:
    if i not in e:
        e.append(i)
for i in e:
    if i  in d:
        print(i,end=' ')
