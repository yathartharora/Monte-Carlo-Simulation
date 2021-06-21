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
    
    
def play(funds, initial_wager, wager_count):

    global broke_count
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
            if value<0:
                broke_count = broke_count + 1
            wX.append(currentwager)
            vY.append(value)

        currentwager = currentwager + 1


    # if value<0:
    #     value = 'Broke!'
    # print('Funds:', value)
    plt.plot(wX,vY)

x = 0
broke_count = 0


#Multiple Bets
while x<1000:
    play(1000,100,500)
    x=x+1

print ('death rate:',(broke_count/float(x)) * 100)
print ('survival rate:',100 - ((broke_count/float(x)) * 100))
plt.ylabel('Account Value')
plt.xlabel('Wager Count')
plt.axhline(0, color = 'r')
plt.show()
