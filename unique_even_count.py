n=int(input())
a=list(map(int,input().split()))
b=list(set(a))
s=0
for i in b:
    if i%2==0:
        s+=1
print(s)