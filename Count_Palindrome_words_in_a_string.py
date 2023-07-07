n=str(input())
s=n.lower()
b=s.split()
c=0
for i in b:
    if i==i[::-1]:
        c+=1
print(c)