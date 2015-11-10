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
