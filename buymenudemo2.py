# Made in python 3.5 (32-bit)
# This is a more functional demo of the buymenu than buymenu-demo1.py. This demo contains a weaponlist (wlist)
# and removes money from a players account.
# You can also switch knifes and drop your primary and secondary. They will be lost forever though.
# In the final game, dropped weapons will be saved to the current location for the duration of the round.

# To-Do:
#   - Restructure all those if-statements somehow, that looks painful and untidy.
#   - Add an output for failed buy-attempts ("Not enough money", "already has weapon", etc.)

# This file doesn't automatically start, so i'm listing the functionality of commands here:

# change_maxmoney(amount) - Changes the maximum amount of money the player can have at a time
# default_maxmoney()      - Defaults the maximum amount of money the player can have at a time back to 10000
# addmoney(amount)        - Adds the given amount to the total amount of money the player has
# playermoney()           - Checks how much money you have (hint, check variable pm)
# b()                     - Opens the buymenu (b is the keybind to open the buymenu in CS:GO)
# knife()                 - Switch out your current knife with another one
# drop(slot)              - Drops the given slot (0-2)

# pistols(), heavys(), smgs() and rifles() open the respective submenus.

wlist = ['0. Knife', '1. Glock-18', '2. None']  # Sets the default weapon list to what the terrorists start with
pm = 1000                                       # Sets default money to $1000, just like in casual
maxmoney = 10000                                # Sets the default maxmoney to $10000, just like in casual

def change_maxmoney(money):                     # Changes the maximum amount of money the player can have at a time
    global maxmoney
    maxmoney = money

def default_maxmoney():                         # Defaults the maximum amount of money the player can have at a time back to 10000
    global maxmoney
    maxmoney = 10000

def addmoney(money):                            # Adds the given amount to the total amount of money the player has
    global pm
    global maxmoney
    pm = pm + money
    if pm > maxmoney:
        moneysub = pm - maxmoney
        pm = pm - moneysub
    print('You now have $',pm,'!')

def playermoney():                              # Checks how much money you have (hint, check variable pm)
    global pm
    print('You have $',pm,'!')

def b():                                        # Opens the buymenu (b is the keybind to open the buymenu in CS:GO)
    global pm
    print('You have $',pm,'!')
    print('')
    print('0. <<< Back')
    print('1. Pistols')
    print('2. Heavys')
    print('3. SMGs')
    print('4. Rfiles')
    uinput = input('Enter a number: ')
    if uinput == '1':   # There's definitly a better way of doing this, i just don't know about it yet
        pistols()
    if uinput == '2':
        heavys()
    if uinput == '3':
        smgs()
    if uinput == '4':
        rifles()
    
def pistols():
    global pm
    print('')
    print('0. <<< Back')
    print('1. Glock 18      - $200/$300')
    print('2. Dual Berettas - $500/$300')
    print('3. P250          - $300/$300')
    print('4. Tec-9         - $500/$300')
    print('5. Desert Eagle  - $700/$300')
    uinput = input('Enter a number: ')
    if uinput == '0':
        b()
    if uinput == '1' and pm >= 200: # Oh god, the if-statements are too much, TOO MUCH!
        wlist.pop(1)
        wlist.insert(1,'1. Glock-18')
        pm = pm - 200
        print('Bought Glock-18')
        b()
    if uinput == '2' and pm >= 500:
        wlist.pop(1)
        wlist.insert(1,'1. Dual Berettas')
        pm = pm - 500
        print('Bought Dual Berettas')
        b()
    if uinput == '3' and pm >= 300:
        wlist.pop(1)
        wlist.insert(1,'1. P250')
        pm = pm - 300
        print('Bought P250')
        b()
    if uinput == '4' and pm >= 500:
        wlist.pop(1)
        wlist.insert(1,'1. Tec-9')
        pm = pm - 500
        print('Bought Tec-9')
        b()
    if uinput == '5' and pm >= 700: # (too many actually but who cares)
        wlist.pop(1)
        wlist.insert(1,'1. Desert Eagle')
        pm = pm - 700
        print('Bought Desert Eagle')
        b()

def heavys():
    global pm
    print('')
    print('0. <<< Back')
    print('1. Nova      - $1200/$900')
    print('2. XM1014    - $2000/$900')
    print('3. Sawed-Off - $1200/$900')
    print('4. M249      - $5200/$300')
    print('5. Negev     - $5700/$300')
    uinput = input('Enter a number: ')
    if uinput == '0':
        b()
    if uinput == '1' and pm >= 1200:
        wlist.pop(2)
        wlist.insert(2,'2. Nova')
        pm = pm - 1200
        print('Bought Nova')
        b()
    if uinput == '2' and pm >= 2000:
        wlist.pop(2)
        wlist.insert(2,'2. XM1014')
        pm = pm - 2000
        print('Bought XM1014')
        b()
    if uinput == '3' and pm >= 1200:
        wlist.pop(2)
        wlist.insert(2,'2. Sawed-Off')
        pm = pm - 1200
        print('Bought Sawed-Off')
        b()
    if uinput == '4' and pm >= 5200:
        wlist.pop(2)
        wlist.insert(2,'2. M249')
        pm = pm - 5200
        print('Bought M249')
        b()
    if uinput == '5' and pm >= 5700:
        wlist.pop(2)
        wlist.insert(2,'2. Negev')
        pm = pm - 5700
        print('Bought Negev')
        b()

def smgs():
    global pm
    print('')
    print('0. <<< Back')
    print('1. MAC-10   - $1050/$600')
    print('2. MP7      - $1700/$600')
    print('3. UMP-45   - $1200/$600')
    print('4. P90      - $2350/$300')
    print('5. PP-Bizon - $1400/$600')
    uinput = input('Enter a number: ')
    if uinput == '0':
        b()
    if uinput == '1' and pm >= 1050:
        wlist.pop(2)
        wlist.insert(2,'2. MAC-10')
        pm = pm - 1050
        print('Bought MAC-10')
        b()
    if uinput == '2' and pm >= 1700:
        wlist.pop(2)
        wlist.insert(2,'2. MP7')
        pm = pm - 1700
        print('Bought MP7')
        b()
    if uinput == '3' and pm >= 1200:
        wlist.pop(2)
        wlist.insert(2,'2. UMP-45')
        pm = pm - 1200
        print('Bought UMP-45')
        b()
    if uinput == '4' and pm >= 2350:
        wlist.pop(2)
        wlist.insert(2,'2. P90')
        pm = pm - 2350
        print('Bought P90')
        b()
    if uinput == '5' and pm >= 1400:    # Please don't buy this gun in the real game, ever.
        wlist.pop(2)                    # Don't, please.
        wlist.insert(2,'2. PP-Bizon')   # No, i beg you!
        pm = pm - 1400                  # Why would you even want to have it?
        print('PP-Bizon')               # It does absolutely no damage at all...
        b()

def rifles():
    global pm
    print('')
    print('0. <<< Back')
    print('1. Galil AR - $2000/$300')
    print('2. AK-47    - $2700/$300')
    print('3. SSG 08   - $1700/$300')
    print('4. SG 553   - $3000/$300')
    print('5. AWP      - $4750/$100')
    print('6. G3SG1    - $5000/$300')
    uinput = input('Enter a number: ')
    if uinput == '0':
        b()
    if uinput == '1' and pm >= 2000:
        wlist.pop(2)
        wlist.insert(2,'2. Galil AR')
        pm = pm - 2000
        print('Bought Galil AR')
        b()
    if uinput == '2' and pm >= 2700:
        wlist.pop(2)
        wlist.insert(2,'2. AK-47')
        pm = pm - 2700
        print('Bought AK-47')
        b()
    if uinput == '3' and pm >= 1700:
        wlist.pop(2)
        wlist.insert(2,'2. SSG 08')
        pm = pm - 1700
        print('Bought SSG 08')
        b()
    if uinput == '4' and pm >= 3000:
        wlist.pop(2)
        wlist.insert(2,'2. SG 553')
        pm = pm - 3000
        print('Bought SG 553')
        b()
    if uinput == '5' and pm >= 4750:
        wlist.pop(2)
        wlist.insert(2,'2. AWP')
        pm = pm - 4750
        print('Bought AWP')
        b()
    if uinput == '6' and pm >= 5000:
        wlist.pop(2)
        wlist.insert(2,'2. G3SG1')
        pm = pm - 5000
        print('Bought G3SG1')
        b()

def knife():                                    # Switch out your current knife with another one
    print('Choose your knife:') # I know, some are missing, don't hang me because of that, they'll get added somewhen
    print('0. <<< Back')
    print('1. Default')
    print('2. Gut Knife')
    print('3. Flip Knife')
    print('4. M9 Bayonet')
    print('5. Karambit')
    print('6. Huntsman Knife')
    print('7. Butterfly Knife')
    uinput = input('Enter a number: ')
    if uinput == '1':
        wlist.pop(0)
        wlist.insert(0, '0. Knife')
        print('Equipped Default Knife')
    if uinput == '2':
        wlist.pop(0)
        wlist.insert(0, '0. Gut Knife')
        print('Equipped Gut Knife')
    if uinput == '3':
        wlist.pop(0)
        wlist.insert(0, '0. Flip Knife')
        print('Equipped Flip Knife')
    if uinput == '4':
        wlist.pop(0)
        wlist.insert(0, '0. M9 Bayonet')
        print('Equipped M9 Bayonet')
    if uinput == '5':
        wlist.pop(0)
        wlist.insert(0, '0. Karambit')
        print('Equipped Karambit')
    if uinput == '6':
        wlist.pop(0)
        wlist.insert(0, '0. Hunstsman Knife')
        print('Equipped Huntsman Knife')
    if uinput == '7':
        wlist.pop(0)
        wlist.insert(0, '0. Butterfly Knife')
        print('Equipped Butterfly Knife')

def drop(slot):                                 # Drops the given slot (0-2)
    if slot == 0:
        print("Can't drop Slot",wlist[0])
    if slot == 1:
        print('Dropped Slot',wlist[1])
        wlist.pop(1)
        wlist.insert(1, '1. None')
    if slot == 2:
        print('Dropped Slot',wlist[2])
        wlist.pop(2)
        wlist.insert(2, '2. None')
    if slot > 2 or slot < 0:    # Because i know some fucker out there is going to try this...
        print('No slot found with number',slot,'.')
