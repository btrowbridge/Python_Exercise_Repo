from math import *
f = float(input("Frequency:"))
Cmin = float(input("Capacitor minimum:"))
Cmax= float(input("Capacitor maximum:"))
C = sqrt(Cmin * Cmax)
L = ((2*pi)**2)/((f**2)*C)

print("Required Inductance Value:", L)     
     
