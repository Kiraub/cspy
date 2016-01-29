import os

def wipe():
    os.system('cls')

genericError = 'Error, please try again.\n'

equipList = ['Knife', 'Glock-18', 'None']
# Sets the default weapon list to what the terrorists start with
plMoney = 1000
# Sets default money to $1000, just like in casual
maxMoney = 10000
# Sets the default maxMoney to $10000, just like in casual

# Changes the maximum amount of money the player can have at a time
def change_maxMoney(money):
    global maxMoney
    maxMoney = money

# Defaults the maximum amount of money the player can have at a time back to 10000
def default_maxMoney():
    global maxMoney
    maxMoney = 10000

# Silently adds the given amount to the total amount of money the player has
def addmoney(money):
    global plMoney
    global maxMoney
    plMoney += money
    if plMoney > maxMoney:
        plMoney = maxMoney

def printEquip():
    global plMoney
    global equipList
    print('------------------------------')
    print('You have $'+str(plMoney)+'!')
    print('You are equipped with:')
    i = 0
    for wpn in equipList:
        print('\t'+str(i)+'. '+wpn)
        i += 1
    print('------------------------------\n')

def buyWpn(wpnList,slot):
    global plMoney
    global equipList
    wipe()
    printEquip()
    i = 0
    for wpn in wpnList:
        if i == 0:
            print(str(i) + '. ' + wpn[0])
        else:
            print(str(i) + '. ' + wpn[0] + ', $' + str(wpn[1]) + ', $' + str(wpn[2]))
        i += 1
    while True:
        userInput = int(input('\nEnter a number: '))
        if userInput == 0:
            b()
        elif userInput in range(1,len(wpnList)):
            if plMoney >= wpnList[userInput][1]:
                plMoney -= wpnList[userInput][1]
                input('Bought ' + wpnList[userInput][0] + '.')
                if slot == 1 or slot == 2:
                    equipList[slot] = wpnList[userInput][0]
                else:
                    equipList.append(wpnList[userInput][0])
                b()
                break;
            else:
                print('Not enough money.')
        else:
            print(genericError)

# Switch out your current knife with another one
def knife():
    print('Choose your knife:') # I know, some are missing, don't hang me because of that, they'll get added ... probably
    i = 0
    for knife in knifeList:
        print( str(i) + '. ' + knife)
        i += 1
    while True:
        userInput = int(input('Enter a number: '))
        if userInput == 0:
            b()
        elif userInput in range(1,len(knifeList)):
            equipList[0] = knifeList[userInput]
            input('Equipped ' + knifeList[userInput])
            b()
        else:
            print(genericError)

# Drops the given slot (0-2)
def drop(slot):
    if slot == 0:
        print('Cannot drop Knife')
    if slot == 1 or slot == 2:
        print('Dropped ' + equipList[slot])
        equipList[slot] = 'None'

# <wpn>List = [ (string wpnName, int price, int killReward) ]
pistolList = [ ('<<< Back','',''), ('Glock-18',200,300), ('Dual Berettas',500,300), ('P250',300,300), ('Tec-9',500,300), ('Desert Eagle',700,300)]
heavyList = [ ('<<< Back','',''), ('Nova',1200,900), ('XM1014',2000,900), ('Sawed-Off',1200,900), ('M249',5200,300), ('Negev',5700,300) ]
smgList = [ ('<<< Back','',''), ('MAC-10',1050,600), ('MP7',1700,600), ('UMP-45',1200,600), ('P90',2350,300), ('PP-Bizon',1400,600) ]
rifleList = [ ('<<< Back','',''), ('Galil AR',2000,300), ('AK-47',2700,300), ('SSG 08',1700,300), ('SG 553',3000,300), ('AWP',4750,100), ('G3SG1',5000,300) ]
knifeList = [ '<<< Back', 'Default', 'Gut Knife', 'Flip Knife', 'M9 Bayonet', 'Karambit', 'Huntsman Knife', 'Butterfly Knife' ]

# lls = list of <wpn>Lists
lls = [ pistolList, heavyList, smgList, rifleList]

# subMenuList = [ string subMenuName ]
subMenuList = [ '<<< Back', 'Pistols', 'Heavys', 'SMGs', 'Rifles' ]

# Opens the buymenu (b is the keybind to open the buymenu in CS:GO)
def b():
    global plMoney
    wipe()
    printEquip()
    i = 0
    for sub in subMenuList:
        print(str(i) + '. ' + sub)
        i += 1
    while True:
        userInput = int(input('\nEnter a number: '))
        if userInput == 0:
            input('Closing buymenu, press enter to continue.')
            wipe()
            break;
        elif userInput == 1:
            buyWpn(lls[0],1)
            break;
        elif userInput in range(2,5):
            buyWpn(lls[userInput-1],2)
            break;
        else:
            print(genericError)