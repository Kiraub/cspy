# Made in python 3.5 (32-bit)
# This is a somewhat working demo of a buymenu, see buymenu-demo2.py for actual functionality
# This shows the concept behind the buymenu, this version does not remove money or give the user guns. See buymenu-demo2.py for such functionality

playermoney = 1000
maxmoney = 10000

def change_maxmoney(money):     # Changes the maximum amount of money the user can have to the desired number
    global maxmoney
    maxmoney = money

def default_maxmoney():         # Defaults the maximum amount of money the user can have back to ten thousand
    global maxmoney
    maxmoney = 10000

def addmoney(money):            # Adds money to the users balance
    global playermoney
    global maxmoney
    playermoney = playermoney + money
    if playermoney > maxmoney:
        moneysub = playermoney - maxmoney
        playermoney = playermoney - moneysub
    print('You now have $',playermoney,'!')

# All buy menus are restricted to Terrorist Sided weapons
# Counter-terrorist weapons will be added later on

def pistols():                  # Defines the buylist for Pistols
    print('0. <<< Back')
    print('1. Glock 18      - $200/$300')
    print('2. Dual Berettas - $500/$300')
    print('3. P250          - $300/$300')
    print('4. Tec-9         - $500/$300')
    print('5. Desert Eagle  - $700/$300')
    uinput = input('Enter a number: ')
    if uinput == '1':           # A verfication was supposed to appear here, never finished this
        print()                # There is definitly a better way for this anyway, i'm sure of it
    if uinput == '2':
        print()
    if uinput == '3':
        print()
    if uinput == '4':
        print()
    if uinput == '5':
        print()

def heavys():                   # Defines the buylist for heavy weapons (Shotguns, MGs)
    print('0. <<< Back')
    print('1. Nova      - $1200/$900')
    print('2. XM1014    - $2000/$900')
    print('3. Sawed-Off - $1200/$900')
    print('4. M249      - $5200/$300')
    print('5. Negev     - $5700/$300')
    uinput = input('Enter a number: ')
    if uinput == '1':
        print()
    if uinput == '2':
        print()
    if uinput == '3':
        print()
    if uinput == '4':
        print()
    if uinput == '5':
        print()

def smgs():                     # Defines the buylist for Submachineguns
    print('0. <<< Back')
    print('1. MAC-10   - $1050/$600')
    print('2. MP7      - $1700/$600')
    print('3. UMP-45   - $1200/$600')
    print('4. P90      - $2350/$300')
    print('5. PP-Bizon - $1400/$600')
    uinput = input('Enter a number: ')
    if uinput == '1':
        print()
    if uinput == '2':
        print()
    if uinput == '3':
        print()
    if uinput == '4':
        print()
    if uinput == '5':
        print()
    
def rifles():                   # Defines the buylist for (Sniper-)Rifles
    #T-Seite
    print('0. <<< Back')
    print('1. Galil AR - $2000/$300')
    print('2. AK-47    - $2700/$300')
    print('3. SSG 08   - $1700/$300')
    print('4. SG 553   - $3000/$300')
    print('5. AWP      - $4750/$100')
    print('6. G3SG1    - $5000/$300')
    uinput = input('Enter a number: ')
    if uinput == '1':
        print()
    if uinput == '2':
        print()
    if uinput == '3':
        print()
    if uinput == '4':
        print()
    if uinput == '5':
        print()
    if uinput == '6':
        print()

def buymenu():                  # Actually launches the buymenu, is automatically run at EOF
    uinput = 1
    print("You've opened the buymenu. You have $",playermoney,"!")
    print('0. <<< Close')
    print('1. Pistols')
    print('2. Heavy Weaponry')
    print('3. Sub-Machine-Guns')
    print('4. Rifles')
    uinput = input('Enter a number: ')
    if uinput == '1':           # Redirects to the submenus
        pistols()
        buymenu()
    if uinput == '2':
        heavys()
        buymenu()
    if uinput == '3':
        smgs()
        buymenu()
    if uinput == '4':
        rifles()
        buymenu()

buymenu()   # Finally launches the whole thing
