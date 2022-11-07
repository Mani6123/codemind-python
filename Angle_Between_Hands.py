a,b=map(int,input().split(":"))
hh=(a*30)+(b*0.5)
mm=b*6
x=abs(hh-mm)
y=abs(360-x)
print(min(x,y))