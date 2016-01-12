# Made in python 3.5 (32-bit)
# Testing the functionality of a simple round. Moving, actions and such
# No enemys, AI is in concept phase
# Buymenu available, some gear is already available
# Only t-sided. Teamswitch will be added in a later demo
# Damagetests in concept phase

#REQUIRES buymenudemo2.py TO FUNCTION PROPERLY!!!

from buymenudemo2 import *  # import buymenu because i'm not gonna fucking copy paste that long as fuck code

wlist = ['0. Knife', '1. Glock 18', '2. AK-47'] # Default gear for this test

turn = 0
botcount = input('Set number of bots: ')
botcount = int(botcount)
botcount = botcount + 1     # fuck for-loops
count = 0
play = 1
addmoney(9999)  

def round():
    global count    # Fun fact: when i've first written this, i accedently wrote "global cunt". I was laughing for 10 minutes straight
    global play
    global turn
    turn = turn + 1
    if turn == 1:
        print('Player and bots buy')
        b() # Do not refer to 4chan
        input()
    print('Player movement/attack')
    for i in range(1, botcount):    # fuck this loop. Seriously, just fuck it!
        print('Bot number',i,'movement/attack')
    count = count + 1
    if count == 3:
        play = 0    # Because fuck infinite loops
    input()
    
while play == 1:
    round()

print('End of demo')
