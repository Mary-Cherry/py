#ax^2+bx+c
from math import sqrt
print('Chuong trinh Giai phuong trinh bac 2')
a=float(input('Nhap a: '))
b=float(input('Nhap b: '))
c=float(input('Nhap c: '))
if(a==0):
    #bx+c=0
    if b==0 and c==0:
        print('Vo so nghiem')
    elif b==0 and c!=0:
        print('Vo nghiem')
    else:
        x=-c/b
        print('No x=',x)
else:
    delta=b**2-4*a*c
    if delta <0:
        print('Vo No')
    elif delta == 0:
        x=-b/(2*a)
        print("No kep x1=x2=",x)
    else:
        x1=(-b-sqrt(delta))/(2*a)
        x2=(-b+sqrt(delta))/(2*a)
        print('x1=',x1)
        print('x2=',x2)

