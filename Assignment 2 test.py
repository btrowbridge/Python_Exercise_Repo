from math import *
m = float(input('Mass of Object:'))

T=60
r = 3
v = sqrt(T*r/m)


if 1<=v<10:
    print('rope can swing at 1 m/s')
if 10<=v<20:
    print('rope can swing at 10 m/s')
if 20<=v<40:
    print('rope can swing at 20 m/s')
if v>40:
    print('rope can swing at 40 m/s')
