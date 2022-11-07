n=int(input())
for i in range(1,n//2):
    c=i*i
    if c==n:
        print('True')
        break
    
if c!=n:
    print('False')