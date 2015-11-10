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
        
