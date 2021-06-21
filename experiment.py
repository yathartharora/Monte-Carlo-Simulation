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
    elif dice>51 & dice<100:
        # print('The roll was between 51 and 100, YOU WIN')
        return True
    
    
def play(funds, initial_wager, wager_count):

    value = funds
    wager = initial_wager

    currentwager = 1

    wX = []
    vY = []

    
    while currentwager<= wager_count:
        if rolldice():
            value = value + wager
            wX.append(currentwager)
            vY.append(value)
        else:
            value = value - wager
            wX.append(currentwager)
            vY.append(value)

        currentwager = currentwager + 1


    # if value<0:
    #     value = 'Broke!'
    # print('Funds:', value)
    plt.plot(wX,vY)

x = 0

while x<100:
    play(10000,100,10000)
    x=x+1

plt.ylabel('Account Value')
plt.xlabel('Wager Count')
plt.show()
