import random 
import matplotlib.pyplot as plt

def rolldice():

    dice = random.randint(1,100)

    if dice<=51:
        return False
    elif dice>51 & dice<=100:
        return True
    
def play(total_funds, wager_amount, total_plays):

    Play_num = []
    Funds = []
    Final_funds = []

    play = 1
    while play< total_plays:
        if rolldice():
            total_funds = total_funds + wager_amount
            Play_num.append(play)
            Funds.append(total_funds)
        else:
            total_funds = total_funds - wager_amount
            Play_num.append(play)
            Funds.append(total_funds)
        play = play+1

    plt.plot(Play_num,Funds)
    Final_funds.append(Funds[-1])
    return(Final_funds)

x =1 

while x<=100:
    ending_fund = play(10000,100,5000)
    x=x+1

plt.ylabel('Player Money in $')
plt.xlabel('Number of bets')
plt.show()

print("The player starts the game with $10,000 and ends with $" + str(sum(ending_fund)/len(ending_fund)))