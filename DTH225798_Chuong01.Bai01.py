import math
try:
    r=float(input('moi ban nhap ban kinh: '))
    cv=2*math.pi*r
    dt=math.pi*r*r
    print('chu vi = ',cv)
    print('dien tich = ',dt)
except:
    print('loi roi! ')
