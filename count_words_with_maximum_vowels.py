a=input()
a=a.lower()
a=a.split()
f=0
c=[]
for i in a:
    b=0
    for j in i:
        if j in 'aeiou':
            b+=1
    c.append(b)
d=max(c)
cnt=0
for i in c:
    if i==d:
        cnt+=1
print(cnt)