import math
try:
    r=float(input('Moi ban nhap ban kinh: '))
    cv=2*math.pi*r
    dt=math.pi*r*r
    print('Chu vi = ',cv)
    print('Dien tich = ',dt)
except:
    print('Loi roi! ')
