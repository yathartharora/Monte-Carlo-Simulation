import random 
import matplotlib.pyplot as plt

def rolldice():

    dice = random.randint(1,100)

    if dice<=50:
        # print('The roll was less than 51. YOU LOSE')
        return False
    elif dice==100:
        # print('The roll was 100. YOU LOSE!')
        return False
    elif dice>=51 & dice<100:
        # print('The roll was between 51 and 100, YOU WIN')
        return True
    
    
def double_bettor(funds, initial_wager, wager_count):
    global broke_count
    value = funds
    wager = initial_wager

    currentwager = 1

    wX = []
    vY = []

    previousWager = 'win'
    previousWagerAmount = initial_wager

    
    while currentwager<= wager_count:

        if previousWager == 'win':
            if rolldice():
                value = value + wager
                wX.append(currentwager)
                vY.append(value)
        
            else:
                value = value - wager
                previousWager = 'loss'
                previousWagerAmount = wager
                wX.append(currentwager)
                vY.append(value)
                if value<0:
                    broke_count = broke_count + 1
                    currentwager = currentwager + 10000000000000000
        
        elif previousWager == 'loss':
            if rolldice():
                wager = previousWagerAmount * 2
                value = value + wager
                wager = initial_wager
                previousWager = 'win'
                wX.append(currentwager)
                vY.append(value)
            else:
                wager = previousWagerAmount * 2
                value = value - wager
                if value<0:
                    currentwager = currentwager + 10000000000000000
                    broke_count = broke_count + 1
                previousWager = 'loss'
                previousWagerAmount = wager
                wX.append(currentwager)
                vY.append(value)

        currentwager = currentwager + 1


    # if value<0:
    #     value = 'Broke!'
    # print('Funds:', value)
    plt.plot(wX,vY)

x = 0
broke_count = 0

while x<100:
    double_bettor(1000,100,100)
    x=x+1

print ('death rate:',(broke_count/float(x)) * 100)
print ('survival rate:',100 - ((broke_count/float(x)) * 100))
plt.ylabel('Account Value')
plt.xlabel('Wager Count')
plt.axhline(0, color = 'r')
plt.show()