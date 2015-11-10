from math import *
q1 = 8.00e-9
q2 = 6.00e-9
k = 8.99e9
x1 = 16.00
x2 = 9.00
y = 12.00
d1 = ((x1)**2) + (y**2)
d2 = ((x2)**2) + (y**2)
F1 = k *(q1)/d1
ang1 = atan(y/x1)
Fx1 = cos(ang1)*F1
Fy1 = sin(ang1)*F1
F2 = k *(q2)/d2
ang2 = atan (y/x2)
Fx2 = cos(ang2)*F2
Fy2 = sin(ang2)*F2

Fxt = Fx2 - Fx1
Fyt = Fy2 + Fy1

print(Fxt,',',Fyt)
