#--------------------------------
# Programming Assignment 2
#
# Name: Bradley Trowbridge
# Date: 10/06/2014
#
#--------------------------------
#################################
# Exercise P3.14 (7 points)

card = input('Enter the Card notation:')

if card[0] == 'A':
    cType = 'Ace'
elif card[0] == 'K':
    cType = 'King'
elif card[0] == 'Q':
    cType = 'Queen'
elif card[0] == 'J':
    cType = 'Jack'
else:
    cType = card[0]

if card[1] == 'S':
    cSuit = 'Spades'
elif card[1] == 'H':
    cSuit = 'Hearts'
elif card[1] == 'C':
    cSuit = 'Clubs'
elif card[1] == 'D': 
    cSuit = 'Diamonds'

print('%s of %s' %(cType, cSuit))



#################################
# Exercise P3.17 (7 points)

string = input('Random String:')
end = len(string)- 1
if string.isupper():
    print('contains only uppercase letters')
elif string.islower():
    print('contains only lowercase letters')
elif string.isdigit():
    print('contains only numbers')

if string.isalnum():
    print('contains only letters and numbers')
if string[0].isupper():
    print('starts with an uppercase letters')
if string[end] == '.':
    print('ends with a period')


#################################
# Exercise P3.18 (5 points)

time1 = input('Time 1 in military format(24:00):')
time2 = input('Time 2 in military format(24:00):')

valueTime1 = time1[0:3] + time1[3:6]
valueTime2 = time2[0:3] + time2[3:6]

if valueTime1 < valueTime2:
    print(time1,time2)
elif valueTime2 < valueTime2:
    print(time2,time1)
else:
    print('Equal')


#################################
# Exercise P3.19  (6 points)

letter = input('Input Letter:')
letter = letter.lower()
vowel = ('a','e','i','o','u','y')
if len(letter) == 1 and letter.isalnum() and not letter.isdigit():
    if letter in vowel:
        print('Vowel')
    else:
        print('Consonant')
else:
    print('Error')


#################################
# Exercise P3.21 (6 points)

float1 = float(input('Float number 1:'))
float2 = float(input('Float number 2:'))

if round(float1,2) == round(float2,2):
    print('They are same up to two decimal places')
else:
    print('They are different')


#################################
# Exercise P3.25  (6 points)

status = input('Marital Status (s or m):')
income = float(input('Income:'))
rate1 = 0.1
rate2 = 0.15
rate3 = 0.25
limS1 = 8000
limS2 = 32000
limM1 = 16000
limM2 = 64000

if status == 's':
    if income <= limS1:
        tax = rate1 * income
    elif limS1 < income <= limS2:
        tax = (rate1*limS1) + rate2 *(income - LimS1)
    else:
        tax = (rate1 *limS1) + (rate2 * limS1) + rate3*(income - limS2)
        

elif status == 'm':
    if income <= limM1:
        tax = rate1 * income
    elif limM1 < income <= limM2:
        tax = (rate1*limM1) + rate2 *(income - limM1)
    else:
        tax = (rate1 *limM1) + (rate2 * limM1) + rate3*(income - limM2)
        
else:
    print(Error)


print('Income Tax:', tax)


#################################
# Exercise Business P3.33 (9 points)

i = 3
while i > 0:
    PIN = input('Input PIN number:')
    if PIN != '1234':
        print('Your PIN is incorrect')
        i -= 1
    else:
        print('Your pin is correct')
        break
if i == 0:
    print('Your bank card is blocked')


#################################
# Exercise Business P3.34 (5 points)

cost = float(input('Please enter the cost of your groceries:'))

discout1 = 0
discount2 = .08
discount3 = .1
discount4 = .12
discount5 = .14

if cost < 10:
    coupon = 0
    percent = 0
elif 10 <= cost <= 60:
    coupon = cost * discount2
    percent = discount2 * 100
elif 60 < cost <= 150:
    coupon = cost * discount3
    percent = discount3 * 100
elif 150 < cost <= 210:
    coupon = cost * discount4
    percent = discount4 * 100
elif 210 < cost:
    coupon = cost * discount5
    percent = discount5 * 100


print('You win a discount coupon of $ %.2f. (%d %% of your purchase)' %(coupon, percent))


#################################
# Exercise Business P3.35 (6 points)

satisfaction = input('rate your experience on thi scale scale... (1 = Totally satisfied, 2 = Satisfied, 3 = Dissatisfied:')
cost = float(input('Meal cost:'))

if satisfaction == '1':
    tip = 0.2
    experience = 'Totally Satisfied'
if satisfaction == '2':
    tip = 0.15
    experience = 'Satisfied'
if satisfaction == '3':
    tip = 0.1
    experience = 'Dissatisfied'

tipInCents = round((cost * tip* 100),0)

dollars = tipInCents // 100
cents = tipInCents %100

print('You were...', experience)
print('The recommended tip is %d dollars and %d cents' %(dollars,cents))


#################################
# Exercise Science P3.40 (10 points)

from math import *

pressure = float(input('Pressure value:'))
units = input('Pressure units(Pa or dB):')

if units == 'Pa':
    pressure = 20 * log(pressure/(20e-6))

print(pressure,'dB')


if pressure < 15:
    print('Light leaf rustling')
elif 15 < pressure <= 45:
    print('Calm library')
elif 45 < pressure <= 75:
    print('Normal Conversation')
elif 75 < pressure <= 95:
    print('Traffic on a busy roadway at 10m')
elif 95 < pressure <= 110:
    print('Jack hammer at 1m')
elif 110< pressure <=125:
    print('Possible hearing damage')
else:
    print('Threshold of pain')


#################################
# Exercise Science P3.42 (8 points)



#################################
# Exercise Science P3.43 (8 points)

v = float(input('Rotational Velocity:'))

m = 2
r = 3
T = m *(v**2)/r

if T <= 60:
    print('the rope will not break')
else:
    print('the rope will break')



#################################
# Exercise Science P3.44 (9 points)


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

#################################
# Exercise Science P3.45 (8 points)



