n=int(input())
l=list(map(int,input().split()))
ev=od=0
for i in range(n):
    if i%2==0:
        ev+=l[i]
    else:
        od+=l[i]
print(abs(ev-od))