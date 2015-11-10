#-------------------------------------------------
# Programming Assignment 4
#
# Name:
# Date: 11/25/2014
#
#-------------------------------------------------
##################################################
# Exercise P5.2 (8 points)

'a'

def smallest(x,y,z):
    someList = [x,y,z]
    return min(someList)

'b'

def average(x,y,z):
    someList = [x,y,z]
    return sum(someList)/len(someList)

##################################################
# Exercise P5.4 (8 points)

def middle(string):
    if len(string) % 2 == 0:
        print(string[int(len(string)/2)-1:int(len(string)/2)+1])
    else:
        print(string[(int(len(string)/2)+1)])
    


##################################################
# Exercise P5.5 (8 points)

def repeatString(string,n,delim):
    endstring = ''
    for i in range(n):
        endstring += string + delim
    return endstring



##################################################
# Exercise P5.7 (8 points)

def countWords(string):
    count = 1
    for i in range(len(string)-1):
        if string[i] == ' ':
            count+= 1
    return count
        


##################################################
# Exercise P5.8 (8 points)

def scramble(word):
    from random import randint
    wordList = []
    wordList += word
    a = randint(1,len(word)-2)
    b = randint(1,len(word)-2)
    wordList[a],wordList[b] = wordList[b],wordList[a]
    newword = ''
    for i in wordList:
        newword += i
    return print(newword)
    



##################################################
# Exercise P5.15 (8 points)

def reverse(string):
    normal =[]
    reverse = ''
    normal += string
    for i in range(len(normal)):
        reverse += normal.pop()
    return reverse



##################################################
# Exercise P5.17 (8 points)

def find(string,match):
    if match in string:
        return True
    else:
        return False



##################################################
# Exercise Business P5.28 (8 points)

def financialAid(income,children):
    if 30000 < income < 40000 and children >= 3:
        return 1000 * children
    elif 20000 < income < 30000 and children >= 2:
        return 1500 * children
    elif income < 20000:
        return 2000 * children
    else:
        return 'No aid required'



##################################################
# Exercise Business P5.30 (10 points)
def confirmPassword(first,second):
    if first == second:
        return True
    else:
        return False
    
def validateNumbers(password):
    for i in password:
        if i.isdigit():
            valid = True
            break
        else:
            valid = False
    return valid

def validateUpper(password):
    for i in password:
        if i.isupper():
            valid = True
            break
        else:
            valid = False
    return valid
            
def createPassword():
    validPass = False
    while validPass != True:
        password = input('Please enter a new password:')
        if len(password) >= 8 and validateNumbers(password) == True and validateUpper(password) == True:
            password2 = input('Please confirm your password')
            if confirmPassword(password,password2) == True:
                validPass = True
            else:
                print('Password did not match')
        else:
            print('Password must contain at least 8 characters and contain one upper and one number')
    print('Password confirmed')
    return password
         
        
##################################################
# Exercise Science P5.33 (8 points)

def lensFocalLength(n,R1,R2,d):
    f = 1/((n - 1)*((1/R1)-(1/R2)+((n-1)*d)/(n*R1*R2)))
    return f


##################################################
# Exercise Science P5.34 (8 points)
from math import pi
from math import sqrt

def volume(h,R1,R2):
    V = (1/3)*pi*h*((R1**2) + (R2**2) + (R1 * R2))
    return V

def surfaceArea(h,R1,R2):
    SA = pi * (R1+R2)* sqrt(((R2-R1)**2) + (h**2)) + (pi * (R1**2))
    return SA



##################################################
# Exercise Science P5.35 (10 points)

def diameter(wireGauge):
    d = 0.127 * 92 * ((36-wireGauge)/39)
    return d
def copperWireResistance(length,wireGauge):
    resistivity = 1.678e-8
    R = (4*resistivity*length)/(pi*(diameter(wireGauge)**2))
    return R
def aluminumWireResistance(length,wireGauge):
    resistivity = 2.82e-8
    R = (4*resistivity*length)/(pi*(diameter(wireGauge)**2))
    return R

##################################################
def main():
    #print(smallest(1,2,3))
    #print(average(1,2,3))
    #middle('hello')
    #middle('help')
    #print(repeatString('ho',3,', '))
    #print(countWords('Mary Had a Little Lamb'))
    #scramble('nimbus')
    #print(reverse('wolf'))
    #print(find('Mississippi','sip'))
    #print(financialAid(25000,0))
    #createPassword()
    #print(lensFocalLength(3,1,1,1))
    #print(volume(3,2,2),surfaceArea(3,2,2))
    print(copperWireResistance(4,28),aluminumWireResistance(4,28))
    pass

if __name__ == '__main__':
    main()

