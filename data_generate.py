import random as rand
import numpy as np

data = open('poker-hand-testing.data', 'rw')
data_line = data.readlines()\

for i in range(25000):
    instance = ""
    plays_first = rand.getrandbits(1)
    pot_amount = rand.randint(1000, 100000)
    player_amount = rand.randint(1000, 10000)
    bet = rand.randint(1, player_amount)
    bet_relate_pot = bet/pot_amount
    bet_relate_equity = bet/player_amount
    number_of_hands = i
    hand = data_line[i]
    instance = str(plays_first) + ',' + str(round(bet_relate_pot, 2)) + ',' + str(round(bet_relate_equity, 2)) + ',' + \
               str(number_of_hands) + ',' + hand[len(hand)-3]
    print instance
print "end"
