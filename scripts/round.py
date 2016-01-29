# Made in python 3.5 (32-bit)
# Testing the functionality of a simple round. Moving, actions and such
# No enemys, AI is in concept phase
# Buymenu available, some gear is already available
# Only t-sided. Teamswitch will be added in a later demo
# Damagetests in concept phase

#REQUIRES buyMenu.py TO FUNCTION PROPERLY!!!

from buyMenu import *

wlist = ['0. Knife', '1. Glock 18', '2. AK-47']
# Default gear for this test

turn = 0
botcount = int(input('Set number of bots: '))
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
        buyMenu()
        input()
    print('Player movement/attack')
    for i in range(1, botcount+1):
        print('Bot number',i,'movement/attack')
    count += 1
    if count == 3:
        play = 0
    input()
    
while play == 1:
    round()

print('End of demo')