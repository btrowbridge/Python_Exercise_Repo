#--------------------------------
# Programming Assignment 3
#
# Name:Bradley Trowbridge
# Date: 10/28/2014
#
#--------------------------------
#################################
# Exercise P4.3 (8 points)

string = str(input('Input a string:'))

listUpper = [ ]
secondLetter = ''
stringUnderscore = ''
numDigit = 0
stringLetters = ''

print('Vowel Position:')
             
for i in range(len(string)): 
    if string[i].isupper():
        listUpper += string[i]
    if string[i].lower() in 'aeiou':
        stringUnderscore += '_'
    elif string[i].lower() not in 'aeiou':
        stringUnderscore += string[i]
    if string[i].isdigit():
        numDigit += 1
    if string[i] in 'aeiou':
        print(string[i], i)
    if string[i].lower() in 'abcdefghijklmnopqrstuvwxyz' :
        stringLetters += string[i]
for j in range(1,len(stringLetters),2):
        secondLetter += stringLetters[j]
     
print('Uppercase Letters:', listUpper)
print('Every Second Letter:', secondLetter)
print('Vowels to Underscore:', stringUnderscore)
print('Number of Digits:', numDigit)



#################################
# Exercise P4.7 (8 points)

from random import randint

word = str(input('Input a word:'))



for k in range(len(word)): 
    i = int(randint(0,len(word)-2))
    j = int(randint(i+1,len(word)-1))
    first = word[0:i]
    middle = word[i+1:j]
    last = word[j+1:len(word)]
    word = first + word[j] + middle + word[i] + last
    print(word)



#################################
# Exercise P4.14 (8 points)
#Read the Notes section posted online with this assignment
#Save the collected values in a list 
#and use the first (and more accurate) standard deviation formula

from random import random
from math import sqrt



# n random numbers from 0 to 1
floatList = []
sampleN = 10
for i in range(sampleN):
    floatList += [random()]

#sum
    #n being the real count
listSum = 0
n=0
for j in range(len(floatList)):
    listSum += floatList[j]
    n += 1

#standard deviation
average = listSum / n
summation = 0
for k in range(n):
    summation += (floatList[k] - average)**2

standardDev = sqrt(summation/(n-1))

print('Random Float Numbers:', floatList)
print('Number of Float Numbers:', n)
print('Sum:',listSum)
print('Average:', average)
print('Standard Deviation:', standardDev)


#################################
# Exercise P4.15 (8 points)

n = int(input('Fibbinacci Sequence Iterations:'))


fold1 = 1
fold2 = 1
if n > 0:
    print(fold1)
if n > 1:
    print(fold2)
if n > 2:  
    for i in range(n - 2):
        fnew = fold1 + fold2
        print(fnew)
        fold2 = fold1
        fold1 = fnew
elif n == 0:
    print('no fibbinacci sequence requested')


#################################
# Exercise P4.23  (10 points)


from random import randint
from math import log


#n number of marbles
n = randint(10,100)

#random coin flips
smartRoll = randint(0,1)
turnFirst = randint(0,1)
moveLegal = True
#Rule max

if smartRoll == 0:
    print('Difficulty: Easy')
else:
    print('Difficulty: Hard')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if smartRoll == 0 and turnFirst == 0:
    while n >= 1:
        print('There are %d marbles in the bag' %(n))
        if n == 1:
            print('You win!')
            break
        else:
            grabComp = randint(1, int(n/2))
            print('Your opponent takes %d marbles' % (grabComp))
            n -= grabComp
        print('There are %d marbles in the bag' %(n))
        if n == 1:
            print('You lose!')
            break
        else:
            grabPlayer = int(input('Your Turn: How many marbles do you take?'))
            if grabPlayer < 1 or grabPlayer > (n/2):
                moveLegal = False
            while moveLegal == False:
                if 1 <= grabPlayer <= n/2:
                    moveLegal = True
                else:
                    print('you must grab between 1 and %d marbles' %(n/2))
                    grabPlayer = int(input('Your Turn: How many marbles do you take?'))
            n -= grabPlayer

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                                   
if smartRoll == 0 and turnFirst == 1:
    while n >= 1:
        print('There are %d marbles in the bag' %(n))
        if n == 1:
            print('You lose!')
            break
        else:
            grabPlayer = int(input('Your Turn: How many marbles do you take?'))
            if not 1 <= grabPlayer <= n/2:
                    moveLegal = False
            while moveLegal == False:
                if 1 <= grabPlayer <= n/2:
                    moveLegal = True
                else:
                    print('you must grab between 1 and %d marbles' %(n/2))
                    grabPlayer = int(input('Your Turn: How many marbles do you take?'))
            n -= grabPlayer
        print('There are %d marbles in the bag' %(n))
        if n == 1:
            print('You win!')
            break
        else:
            grabComp = randint(1, int(n/2))
            print('Your opponent takes %d marbles' % (grabComp))
            n -= grabComp
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if smartRoll == 1 and turnFirst == 0:
    while n >= 1:
        print('There are %d marbles in the bag' %(n))
        if n == 1:
            print('You win!')
            break
        else:
            if 3 < n < 7:
                grabComp = n - 3
            elif 7 < n < 15:
                grabComp = n - 7
            elif 15 < n < 31:
                grabComp = n - 15
            elif 31 < n < 63:
                grabComp = n - 31
            elif n > 63:
                grabComp = n - 63
            else:
                grabComp = randint(1, int(n/2)) 
            print('Your opponent takes %d marbles' % (grabComp))
            n -= grabComp
        print('There are %d marbles in the bag' %(n))
        if n == 1:
            print('You lose!')
            break
        else:
            grabPlayer = int(input('Your Turn: How many marbles do you take?'))
            if not 1 <= grabPlayer <= n/2:
                    moveLegal = False
            while moveLegal == False:
                if 1 <= grabPlayer <= n/2:
                    moveLegal = True
                else:
                    print('you must grab between 1 and %d marbles' %(n/2))
                    grabPlayer = int(input('Your Turn: How many marbles do you take?'))
            n -= grabPlayer
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if smartRoll == 1 and turnFirst == 1:
    while n >= 1:
        print('There are %d marbles in the bag' %(n))
        if n == 1:
            print('You lose!')
            break
        else:
            grabPlayer = int(input('Your Turn: How many marbles do you take?'))
            if not 1 <= grabPlayer <= n/2:
                    moveLegal = False
            while moveLegal == False:
                if 1 <= grabPlayer <= n/2:
                    moveLegal = True
                else:
                    print('you must grab between 1 and %d marbles' %(n/2))
                    grabPlayer = int(input('Your Turn: How many marbles do you take?'))
            n -= grabPlayer
        print('There are %d marbles in the bag' %(n))
        if n == 1:
            print('You win!')
            break
        else:
            if 3 < n < 7:
                grabComp = n - 3
            elif 7 < n < 15:
                grabComp = n - 7
            elif 15 < n < 31:
                grabComp = n - 15
            elif 31 < n < 63:
                grabComp = n - 31
            elif n > 63:
                grabComp = n - 63
            else:
                grabComp = randint(1, int(n/2)) 
            print('Your opponent takes %d marbles' % (grabComp))
            n -= grabComp
        


#################################
# Exercise P4.25 (10 points)

from random import randint
strategy1 = 0
strategy2 = 0
iterations = 1000
lose1 = 0
lose2 = 0

for i in range(iterations):
    door = [1,2,3]
    j = randint(0,2)
    car = door[j]
    k = randint(0,2)
    choice = door[k]
    door.remove(choice)
    if car != choice:
        door.remove(car)
        l = 0
        hostchoice = door[0]
        door += [car]
        del door[0]
    else:
        l = randint(0,1)
        hostchoice = door[l]
        door.remove(hostchoice)
    switch = randint(0,1)
    if switch == 1:
        choice = door[0]
        if choice == car:
            strategy2 += 1
        else:
            lose2+=1
    else:
        if choice == car:
            strategy1 += 1
        else:
            lose1 += 1
print('%d Wins and %d Losses staying with your door:'%(strategy1,lose1))
print('%d Wins and %d Losses switching your door:' %(strategy2,lose2))
print('Games:', iterations)


#################################
# Exercise P4.26 (8 points)

rold = int(input('Input seed:'))
a = 32310901
b = 1729
m = 2**24
for i in range(100):
    rnew = (a*rold +b)%m
    print (rnew)
    rold = rnew


#################################
# Exercise Business P4.31 (8 points)

inventory = 100
buyer = 0
while inventory >= 0:
    print(inventory)
    sell = int(input('Tickets purchased:'))
    while sell > inventory:
        print('There are only %d tickets left' %(inventory))
        sell = int(input('Tickets purchased:'))
    inventory -= sell
    buyer += 1
    if inventory == 0:
        print('Sold Out')
        print('Buyers:', buyer)
        break


#################################
# Exercise Business P4.33 (8 points)

ccnum = str(input('8-digit Credit Card Number:'))
nsum = 0
excludednum = ''
excludedsum = 0
for i in range(-1,-9,-2):
    nsum += int(ccnum[i])

for j in range(-2,-10,-2):
    excludednum += str(2*int(ccnum[j]))

for k in range(len(excludednum)):
    excludedsum += int(excludednum[k])

checkDigit = str(excludedsum + nsum)
print ('Check Digit', checkDigit)
            
if checkDigit[-1] == '0':
    print('Valid')
else:
    print('Not Valid')

#################################
# Exercise Science P4.34 (8 points)

periods = int(input('Number of periods:'))
            
predator0 = int(input('Initial predetors:'))
prey0 = int(input('Initial prey:'))
A = float(input('Rate prey birth exceeds natural death:'))
B = float(input('Rate of predation:'))
C = float(input('Rate predator deaths exceeds births:'))
D = float(input('Rate Predator increase in presence of food:'))
print('Prey,Predator')
print(prey0,predator0)
for i in range(periods):
    prey1 = prey0 *(1 + A - (B * prey0))
    predator1 = predator0 * ( 1 - C + (D * predator0))
    prey0 = prey1
    predator0 = predator1
    print(prey1,predator1)


#################################
# Exercise Science P4.37 (8 points)
# Read the Notes section posted online with this assignment

from math import *

#Tratio = A/A0
h = 6



for t in range (24)
    Tratio = * e**(-t(log(2/h)))
    print(Tratio)
    


#################################
# Exercise Science P4.38 (8 points)

R0 = 20
Vs = 40
Rs = 8


for n in range(.01,2,.01):
    P = Rs*(((n*Vs)/((n**2)*R0 + Rs))**2)
    print(P)

