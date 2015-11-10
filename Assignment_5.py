#-------------------------------------------------
# Programming Assignment 5
#
# Name: 
# Date: 12/9/2014
#
#-------------------------------------------------
##################################################
# Exercise P6.17 (20 points)
from random import randint

def exercise_P6_17():
    print()
    print('Exercise P6.17')
    list1 = [i + 1 for i in range(10)]
    list2 = []
    for i in range (10):
        list2 += [list1.pop(randint(0,len(list1)-1))]
    return list2        
    
    
    print()

##################################################
# Exercise P6.19 (20 points)

def divide(cards):
    if cards == 1:
        pileLen = 1
    else:
        pileLen = randint(1,cards)
    return pileLen
            
def multiplePiles(cardNum):
    multiList = [0 for i in range (9)]
    for i in range(len(multiList)):
        multiList[i] += divide(cardNum)
        cardNum -= multiList[i]
        if cardNum == 0:
            break
    return multiList


def nextConfiguration(y):
    for x in range(len(y)-1):
        if y[x] > 1:
            if y[x] > y[x+1]+1:
                y[x] -= 1
                y[x+1] += 1
        print(y)
    y.sort(reverse = True)
    return y
         
def solitaire(cards):
    config = multiplePiles(cards)
    print('Initial Configuration:',config)
    while config != [9,8,7,6,5,4,3,2,1]:
        new_config = nextConfiguration(config)
        config = new_config
    
def exercise_P6_19():
    print()
    print('Exercise P6.19')
    cards = 45
    solitaire(cards)
    print()
                                        

##################################################
# Exercise P6.22 (20 points)

def createTable(rows = 5,columns = 5):
    table = []
    for i in range(rows):
        for j in range (columns):
            createList = []
            createList += [randint(1,10)]
        table += [createList]
    return table

def neighborAverage(table,row,column):
    computeList =[]
    
    if row == 0  and 0<column<len(table[row])-1:
        for i in range(0,1):
            for j in range(-1,1):
                if i != 0 and j != 0:
                    computeList += [table[row+i][column+i]]
    if row == len(table)-1  and 0<column<len(table[row])-1:
        for i in range(-1,0):
            for j in range(-1,1):
                if i != 0 and j != 0:
                    computeList += [table[row+i][column+i]]
    if row == len(table)-1  and column == len(table[row])-1:
        for i in range(-1,0):
            for j in range(-1,0):
                if i != 0 and j != 0:
                    computeList += [table[row+i][column+i]]
    if row == 0  and column == 0:
        for i in range(0,1):
            for j in range(0,1):
                if i != 0 and j != 0:
                    computeList += [table[row+i][column+i]]
    if 0<row<len(table)-1  and column == len(table[row])-1:
        for i in range(-1,1):
            for j in range(-1,0):
                if i != 0 and j != 0:
                    computeList += [table[row+i][column+i]]
    if 0<row<len(table)-1  and column == 0:
        for i in range(-1,1):
            for j in range(0,1):
                if i != 0 and j != 0:
                    computeList += [table[row+i][column+i]]


    else:
        for i in range(-1,1):
            for j in range(-1,1):
                if i != 0 and j != 0:
                    computeList += [table[row+i][column+i]]
    return print(sum(computeList)/len(computeList))
                    

def exercise_P6_22():
    print()
    table = createTable()
    print(table)
    neighborAverage(createTable(),2,2)
    print('Exercise P6.22')
    
    
    
    print()

##################################################
# Exercise P6.30 (20 points)

def exercise_P6_30():
    print()
    print('Exercise P6.30')
    
    
    
    print()

##################################################
# Exercise Science P6.35 (20 points)

def exercise_P6_35():
    print()
    print('Exercise Science P6.35')
    
    
    
    print()

##################################################
def main():
    #print(exercise_P6_17())
    #exercise_P6_19()
    exercise_P6_22 ()
    pass

if __name__ == '__main__':
    main()
