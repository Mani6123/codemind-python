s=input()
s=s.split()
e=[]
for i in s:
    e.append(len(i))
print(max(e))