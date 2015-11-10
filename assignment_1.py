#--------------------------------
# Programming Assignment 1
#
# Name: Bradley Trowbridge
# Date: 9/21/2014
#
#--------------------------------
# Exercise P2.4 (7 points)
num1 = int(input("Integer 1:"))
num2 = int(input("Integer 2:"))
add = num1 + num2
sub = num1 - num2
product = num1 * num2
average = (num1 + num2)/2
distance = abs(sub)
maximum = max(num1, num2)
minimum = min(num1, num2)
print("Sum:", add)
print("Difference:", sub)
print("Product:", product)
print("Mean:", average)
print("Distance:", distance)
print("Maximum:", maximum)
print("Minimum:", minimum)


#################################
# Exercise P2.5 (4 points)
num1 = int(input("Integer 1:"))
num2 = int(input("Integer 2:"))
add = num1 + num2
sub = num1 - num2
product = num1 * num2
average = (num1 + num2)/2
distance = abs(sub)
maximum = max(num1, num2)
minimum = min(num1, num2)
print("Sum:%14d" %add)
print("Difference:%7d" %sub)
print("Product:%10d" %product)
print("Average:%12.1f" %average)
print("Distance:%9d" %distance)
print("Maximum:%10d" %maximum)
print("Minimum:%10d" %minimum)



#################################
# Exercise P2.7 (4 points)
radius = int(input("Radius:"))

from math import *

area = pi * (radius**2)
circum = 2 * pi * radius
volume = (4/3) * pi *(radius**3)
surfArea = 4 * pi * (radius*2)
print("Area of Circle:", area)
print("Circuference of Circle:", circum)
print("Volume of Sphere:", volume)
print("Surface Area of Sphere:", surfArea)



#################################
# Exercise P2.13 (7 points)
num1 = input("Please enter an integer between 10,000 and 99,999:")

num2 = num1[0:2]+num1[3:6]

print(num2)           



#################################
# Exercise P2.14 (7 points)


num1 =int(input("Please enter an integer between 1000 and 999999:"))


#print( "{:,d}".format(num1)) 

num2 = str(num1 // 1000)
num3 = str(num1 % 1000)

num4 = num2 + ','+ num3
print(num4)



#################################
# Exercise P2.16 (7 points)
num = input("Five Digit Integer:")

print(num[0], num[1], num[2], num[3],num[4])



#################################
# Exercise P2.21 (10 points)

y = int(input("Year:"))
a = y % 19
b = y // 100
c = y % 100
d = b // 4
e = b % 4
g = (8 * b + 13) // 25
h = (19 * a + b - d - g + 15) % 30
j = c // 4
k = c % 4
m = (a + 11 * h) // 319
r = (2 * e + 2 * j - k- h + m + 32) % 7
n = (h - m + r + 90) // 25
p = (h - m + r + n + 19) % 32

print("Month:", n)
print("Day:", p)
print("Year:", y)

#################################
# Exercise P2.22 (7 points)
string = input("String Initiate...")

string2 = string[0:3] + "..." + string[len(string)-3:len(string)]

print(string2)



#################################
# Exercise Business P2.33 (8 points)
tele = input("Telephone Number:")

tele2 = '(' + tele[0:3] + ')' + tele[3:6] + '-' + tele[6:10]
print(tele2)



#################################
# Exercise Business P2.35 (8 points)
price = int(input("Amount cost (in pennies):"))
cash= int(input("Amount cash recieved (in pennies):"))

change = cash - price
dol = change // 100
qtr = (change % 100) // 25
dim = ((change % 100) % 25) // 10
nic = (((change % 100) % 25) % 10) // 5
pen = (((change % 100) % 25) % 10) % 5

print("Change:", dol, "dollars", qtr, "quarters", dim, "dimes", nic, "nickels", pen, "pennies")



#################################
# Exercise Science P2.38 (8 points)
r1 = int(input("Resistor 1:"))
r2 = int(input("Resistor 2:"))
r3 = int(input("Resistor 3:"))

rT = (1/((1/r2)+(1/r3))) + r1

print("Resistor Total:", rT )



#################################
# Exercise Science P2.39 (8 points)
from math import *
T = float(input("Temperature:"))
RH = float(input("Humidity:"))
a = 17.27
b = 237.7
func = ((a*T)/(b*T)) + log(RH)

Td = (b*func)/(a-func)

print("Dew Point Temperature:", Td)



#################################
# Exercise Science P2.40 (8 points)
from math import *
R = float(input("Thermistor Resistance:"))
r0 = 1075
t0 = 85
B = 3969 - 273.15

T = ((B * t0)/((t0*log(R/r0)) + B)) - 273

print("Liquid Temperature:", T)



#################################
# Exercise Science P2.43 (7 points)
from math import *
f = float(input("Frequency:"))
Cmin = float(input("Capacitor minimum:"))
Cmax= float(input("Capacitor maximum:"))
C = sqrt(Cmin * Cmax)
L = ((2*pi)**2)/((f**2)*C)

print("Required Inductance Value:", L)     
     



