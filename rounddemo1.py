# Testing the functionality of a simple round. Moving, actions and such
# No enemys, AI is in concept phase
# Buymenu available, some gear is already available
# Only t-sided. Teamswitch will be added in a later demo
# Damagetests in concept phase

# VERY incomplete
# This is on dev for a reason
# Go view the master branch for working stuff instead

#REQUIRES buymenudemo2.py TO FUNCTION PROPERLY!!!

from buymenudemo2 import *

wlist = ['0. Knife', '1. Glock 18', '2. AK-47'] # Default gear for this test

turn = 0
botcount = input('Set number of bots: ')
botcount = int(botcount)
botcount = botcount + 1
count = 0
play = 1
addmoney(9999)

def round():
    global count
    global play
    global turn
    turn = turn + 1
    if turn == 1:
        print('Player and bots buy')
        b()
        input()
    print('Player movement/attack')
    for i in range(1, botcount):
        print('Bot number',i,'movement/attack')
    count = count + 1
    if count == 3:
        play = 0
    input()
    
while play == 1:
    round()

print('End of demo')
