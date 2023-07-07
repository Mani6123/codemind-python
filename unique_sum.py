n=int(input())
a=list(map(int,input().split()))
b=list(set(a))
s=0
for i in range(len(b)):
    s+=b[i]
print(s)