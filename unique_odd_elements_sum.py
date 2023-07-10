n=int(input())
a=list(map(int,input().split()))
b=list(set(a))
s=0
for i in b:
    if i%2==1:
        s+=i
print(s)