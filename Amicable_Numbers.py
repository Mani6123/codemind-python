a=int(input())
b=int(input())
a1=b1=0
for i in range(1,a):
    if a%i==0:
        a1+=i
for j in range(1,b):
    if b%j==0:
        b1+=j
if a==b1 and b==a1:
    print("Amicable")
else:
    print("Not Amicable")