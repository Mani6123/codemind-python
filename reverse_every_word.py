s=input()
s=s.split()
c=[]
for i in s:
    i=i[::-1]
    c.append(i)
print(*c)