#Make a die


numdie = 7


a = [1,2,3,4,5,6]

import random

def dice():
    res = random.choice(a)
    return int(res)


#Roll die 7 times
def trial():

    result = []
    count = 0
    flag2 = 0

    wins=0
    losses=0
    for i in range(0,numdie):
        count +=1
        num = dice()
        print(count,":",num)
        result.append(num)
        if(result.count(num)==3):
                        #Obvious loss
            break
        if(result.count(num)==2 and flag2 == 0):
            flag2 = 1
        if(result.count(num)==2 and flag2 != 0):
            break #One more los
    if(count == 7):
        wins += 1
        print("Wins: ",wins," ----- Losses: ",losses)
        return 1
    else:
        losses += 1
        flag2 = 0
        print("Wins: ",wins," ----- Losses: ",losses)
        return 0

wins = 0
trials = 1000

for i in range(0,trials):
    wins = wins + trial()

print("Number of trials : ", trials)
print("Number of successes : ", wins)
print("Number of failures : ", trials - wins)
print("Probability: ", float(wins)/float(trials))


