# TextGame.py
# Programmer: Emmet Spencer
# Block:1 HNRS PYTHON
# Date: 1/6/20
# Description: This game has randomly generated entitys your character has to kill,
# every mob you kill has a chance of giving you a potion or increasing your base damage



# Make a bat insta-kill.




#****************************************#
#           IMPORT STATEMENTS            #
#****************************************#

import random
import time

#****************************************#
#        FUNCTION DEFINITIONS            #
#****************************************#

def Introduction():
    print("You hear in the bar that a mine down south has some good loot, ")
    time.sleep(.1)
    print("You go down to explore it, but once you enter the cave collapses behind you. ")
    time.sleep(.1)
    print("You try to dig out, but it seems like your only route out is to adventure down the mine.")
    time.sleep(.1)

def ItemTreasure(strMainWeapon):
    blnItemConfirm = False
    time.sleep(2)
    strMainWeapon = strWeapon
    intItemChance = random.randint(1, 100)
    if intItemChance < 100:
        intRandomNumber = random.randint(0,8)
        lstRandomWeapon = lstItemDrops[intRandomNumber]
        print("Item Drop : " + str(lstItemDrops[intRandomNumber][0]))
        while blnItemConfirm == False:
            lstDroppedblnItemConfirm = input("Do you want to pickup this item? : ")
            if lstDroppedblnItemConfirm.lower() == "yes":
                print("\nYou picked up the item.")
                blnItemConfirm = True
                return lstRandomWeapon
            elif lstDroppedblnItemConfirm.lower() == "no":
                print("\nYou choose not to pickup the item.")
                blnItemConfirm = False
                return strWeapon
                break
            else:
                print("Please print yes or no.")
                continue


def CharacterDisplay():
    print("Your Stats:")
    print("  Class : " + strClassName)
    print(f"   - Health : {intHealth}/{intMaxHealth}")
    print(f"   - Mana : {intMana}/{intMaxMana}")
    print("   - Speed : " + str(intSpeed))
    print("   - Weapon : " + strWeapon[0])
    print("   - Weapon Damage : " + str(strWeapon[1]))
    print("   - Damage Multiplier " + str(fltDamageMult))
    print(f"  Gold Coins : {intGoldCoin}")
    print(f"  Potions : H = {intHealthPotionCount} M = {intManaPotionCount}")
    print(strWeapon)
def Fight(lstMonsters, playerWeapon, intMaxHealth, intHealth, intMaxMana, intMana):
    print(r"""
               _____   _____
              /     \ /     \
         ,   |       '       |
         I __L________       L__
    O====IE__________/     ./___>
         I      \.       ./
         `        \.   ./
                    \ /
                     '
    """)
    intRandomMonster = random.randint(0,2)
    lstCurrentMonster = lstMonsters[intRandomMonster]
    print(lstCurrentMonster)
    intCurrentMonsterMaxHealth = lstCurrentMonster[1]
    blnPlayerAlive = True
    fighting = True
    intCurrentDamage = 0
    blnMonsterAlive = True
    strWeapon = playerWeapon
    print(lstMonsters[intRandomMonster])
    print(f"You encountered a {lstMonsters[intRandomMonster][0]}!")
    time.sleep(.5)
    print(f"The monsters is immune to {lstMonsters[intRandomMonster][4]}'s")
    print("\n")
    print("\n")
    blnMonsterAlive = True
    if intSpeed > lstCurrentMonster[3]:
        print("You are going first.")
        blnPlayerTurn = True
        blnMonsterFirst = True
    if intSpeed < lstCurrentMonster[3]:
        print("The monster is going first.")
        blnMonsterFirst = True
        blnPlayerTurn = True
    intFightingRound = 0
    blnMonsterTurn = False
    while fighting:
        print(intFightingRound)
        print(blnPlayerTurn)
        print(blnMonsterTurn)
        while blnPlayerTurn == True and blnPlayerAlive == True:
            strTurn = input("Your Turn, what should you do? [Attack/Potion/Flee] : ")
            if strTurn.lower() == "attack":
                print("You choose to attack.")
                print("\n\n\n")
                print(intCurrentDamage)
                intCurrentDamage = strWeapon[1]
                print(intCurrentDamage)
                print(playerWeapon)
                if strWeapon[2] == "Magic":
                    print("You lost Mana from using your Magic Weapon!")
                    intMana = intMana - (strWeapon[1] / 2 )/ 2
                    print(f"Mana: {intMana}/{intMaxMana}")
                if playerWeapon[2] == lstCurrentMonster[2]:
                    intCurrentDamage = playerWeapon[1] / 3 * 2
                    print(intCurrentDamage)
                print(lstCurrentMonster)
                lstCurrentMonster[1] = lstCurrentMonster[1] - intCurrentDamage
                print(f"\n\n\nYou hit the {lstCurrentMonster[0]} for {intCurrentDamage}!")
                print(f"Monsters Health: {lstCurrentMonster[1]}/{intCurrentMonsterMaxHealth}\n\nMonster's Turn: \n")
                print(lstCurrentMonster[1])
                if lstCurrentMonster[1] <= 0:
                    print("The monster has died.")
                    intRandomGold = random.randint(0,3)
                    time.sleep(.5)
                    print(f"You earned {intRandomGold} gold coin(s).")
                    return intRandomGold
                    blnMonsterAlive = True
                blnMonsterTurn = True
                blnPlayerTurn = False

            if strTurn.lower() == "potion":
                if intHealthPotionCount != 0:
                    strPotionType = input("What type of potion do you want to use?")
                    print(f"Health Potions : {intHealthPotionCount}")
                    print(f"Mana Potions : {intManaPotionCount}")
                    if strPotionType.lower() == "cancel":
                        break
                    if strPotionType.lower() == "mana" and intManaPotionCount != 0:
                        intManaRegenerated = random.randint(20,30)
                        intMana = intMana + intManaRegenerated
                        if intMana > intMaxMana: # if health is greater than maximum health, change health to maximum health.
                            print("You reached Max Mana.")
                            intMana = intMaxMana
                            intRandomGold = 0
                        print(f"Your increased your mana.\nMana gained {intManaRegenerated} Mana!\nCurrent Mana: {intMana}/{intMaxMana}")
                    if strPotionType.lower() == "health" and intHealthPotionCount != 0:
                        intHealthRegenerated = random.randint(20,30)
                        intHealth = intHealth + intHealthRegenerated
                        print(f"You healed yourself for {intHealthRegenerated}")
                        time.sleep(.5)
                        if intHealth > intMaxHealth: # if health is greater than maximum health, change health to maximum health.
                            print("You reached Max Health.")
                            intHealth = intMaxHealth
                            intRandomGold = 0
                    blnMonsterTurn = True
                    blnPlayerTurn = False

            if strTurn.lower() == "flee":
                print("sike bitch you thought")
                intMaxHealth = 1
                intHealth = 1
                print("Your max health and health is set to 1")
                print("dont try and cheat again")
                blnPlayerTurn = False
                blnMonsterTurn = True
                intRandomGold = 0
        while blnMonsterTurn == True and blnPlayerAlive == True:
            intMonsterTurn = random.randint(1,10)
            if lstCurrentMonster[1] <= 0:
                blnPlayerTurn = False
                fighting = False
                blnMonsterTurn = False
                intRandomGold = 0
            if intMonsterTurn >= 6:
                intRandomRegen = random.randint(10,20)
                print("The monster healed itself!")
                lstCurrentMonster[1] = lstCurrentMonster[1] + intRandomRegen
                if lstCurrentMonster[1] > intCurrentMonsterMaxHealth:
                    lstCurrentMonster[1] = intCurrentMonsterMaxHealth
                blnPlayerTurn = True
                blnMonsterTurn = False
                intRandomGold = 0
            elif intMonsterTurn < 6:
                intLowestRandomDamage = lstCurrentMonster[2] - 7
                intRandomDamage = random.randint(intLowestRandomDamage, lstCurrentMonster[2])
                print(f"The {lstCurrentMonster[0]} hit you for {intRandomDamage}!\n")
                intHealth = intHealth - intRandomDamage
                print("You lost health!")
                print(f"Your Health: {intHealth}/{intMaxHealth}")
                intRandomGold = 0
                if intHealth <= 0:
                    print("Your Player Died!")
                    blnPlayerAlive = False
                    intRandomGold = 69
                    return intRandomGold

                blnPlayerTurn = True
                blnMonsterTurn = False
    print("The monster has been killed!")




#****************************************#
#         VARIABLE DECLARATION &         #
#           INITIALIZATION               #
#****************************************#

blnGaming = True
strClassName = ""
level = 1 # 1/5
intHealth = 0
fltDamageMult = 0.0 # 0.0/2.0
intSpeed = 50 # 50/100
intExp = 0 # 1/75
intHealthPotionCount = 0 # Max potion count of 5
intManaPotionCount = 0
intItemChance = 0
blnClassChoice = False
intGoldCoin = 0
GoldCoin = 0
intRound = 0
intMaxMana = 0
intMana = 0
intGameRound = 0



#-------------------------#
#|        Weapons        |#
#-------------------------#
#Swords
lstWoodenAxe = ["Wooden Axe", 22, "Sword"]
lstIronSword = ["Iron Sword", 33, "Sword"]
lstDiamondSword = ["Diamond Sword", 60, "Sword"]
lstKatanaSword = ["Katana", 38, "Sword"]
lstGoldenBunny = ["Golden Bunny", 1, "Sword"]
#Bows
lstWoodenBow = ["Wooden Bow", 25, "Bow"]
lstBoneBow = ["Bone Bow", 30, "Bow"]
lstCoinBow = ["Coin Bow", 50, "Bow"]
lstPowerVBow = ["Power V Bow", 160, "Bow"]

#Magic
lstStaffMagic = ["Staff", 100, "Magic"]
lstMysticMagic = ["Mystic Fist", 27, "Magic"]
lstBookMagic = ["Enchanted Book", 25, "Magic"]


#-------------------------#
#|      Store Items      |#
#-------------------------#

lstGoldenBow = ["Golden Bow ", 45, "Bow", 15]
lstGolemFist = ["Golem Fist", 42, "Sword", 20]
# List of the Items to display in the shop

lstItemShopItems = [lstGoldenBow, lstGolemFist]

#-------------------------#
#|      ItemDrops        |#
#-------------------------#

intGoldCoin = random.randint(1,4)
intPotion = random.randint(1,2)
lstItemDrops = [lstWoodenAxe,lstWoodenAxe,lstWoodenAxe, lstWoodenBow, lstWoodenBow, lstIronSword, lstBoneBow, lstCoinBow, lstDiamondSword]


#-------------------------#
#|        Monsters       |#
#-------------------------#


# FORMAT!!!!! : name , health , damage , speed , damage resistance
lstSlimeMonster = ["Slime", 40, 20, 10, "Bow"]
lstHydraMonster = ["Hydra", 100, 50, 60, "Bow"]
lstReaperMonster = ["Reaper", 65, 60, 75, "Bow"]
lstGolemMonster = ["Golem", 120, 30, 50, "Sword"]
lstBatMonster = ["Bat", 50, 10, 100, "Sword"] # Damage resistance to swords because you cannot hit it without a bow.

lstMonsters = [lstSlimeMonster, lstHydraMonster, lstReaperMonster]
lstSpareMonsters = [lstSlimeMonster, lstHydraMonster, lstReaperMonster]



#****************************************#
#                EXECUTION               #
#****************************************#
while blnClassChoice == False:
    ClassChoice = input("\nWhat class would you like to be? [!help] :")
    if ClassChoice.lower() == "!help":
        print(
       "\n\nWarrior : \n   » Health 150\n   » Starting Weapon : Wooden Axe\n   » Damage Multiplier 1.5x (MAX)\n   » Speed 30\n   » Attributes +10 Melee Damage" +
       "\n\nArcher  : \n   » Health 110\n   » Starting Weapon : Wooden Bow\n   » Damage Multiplier 2.0x (MAX)\n   » Speed 70\n   » Attributes +20 Bow Damage" +
       "\n\nMage  : \n   » Health 100\n   » Starting Weapon : Staff\n   » Damage Multiplier 1.3x (MAX)\n   » Speed 80\n   » Attributes Ability to use Magic")
        continue
    if ClassChoice.lower() == "warrior":
        strClassName = "Warrior"
        intMaxHealth = 150
        intHealth = 150
        intMaxMana = 0
        intMana = 0
        strWeapon = lstWoodenAxe
        fltDamageMult = 1.5
        intSpeed = 50
        intHealthPotionCount = 2
        intManaPotionCount = 0
        blnClassChoice = True
    if ClassChoice.lower() == "archer":
        strClassName = "Archer"
        intHealth = 110
        intMaxHealth = 110
        intMaxMana = 0
        intMana = 0
        strWeapon = lstWoodenBow
        fltDamageMult = 2.0
        intSpeed = 70
        intHealthPotionCount = 2
        intManaPotionCount = 0
        blnClassChoice = True
    if ClassChoice.lower() == "mage":
        strClassName = "Mage"
        intMaxHealth = 100
        intHealth = 100
        intMaxMana = 120
        intMana = 120
        strWeapon = lstStaffMagic
        fltDamageMult = 1.3
        intSpeed = 80
        intHealthPotionCount = 1
        intManaPotionCount = 3
        blnClassChoice = True

Introduction()
strReturn = CharacterDisplay()
while blnGaming:

    strReturn = ItemTreasure(strWeapon)
    strWeapon = strReturn
    strSeeClass = input("Do you want to see your stats? : ")
    if strSeeClass.lower() == "yes":
        strWeapon = CharacterDisplay()
    intGameRound = intGameRound+1
    lstSlimeMonster = ["Slime", 40, 20, 10, "Bow"]
    lstHydraMonster = ["Hydra", 100, 50, 60, "Bow"]
    lstReaperMonster = ["Reaper", 65, 60, 75, "Bow"]
    lstGolemMonster = ["Golem", 120, 30, 50, "Sword"]
    lstBatMonster = ["Bat", 50, 10, 100, "Sword"] # Damage resistance to swords because you cannot hit it without a bow.
    lstMonsters = [lstSlimeMonster, lstHydraMonster, lstReaperMonster]

    intGoldEarned = Fight(lstMonsters, strWeapon, intMaxHealth, intHealth, intMaxMana, intMana)


    if intGoldEarned == 69:
        blnGaming=False
        break
    intGoldCoin = intGoldCoin + intGoldEarned
    if intGameRound % 2 == 0:
        intShopRandomChange = random.randint(0,1)

        if intShopRandomChange == 1:
            print("Welcome to Liam's Crack Shack!")
            print("Today we have a special offer because you are a first time customer!")
            intShopRandomChange = random.randint(0,1)
            lstItemPurchasable = lstItemShopItems[intShopRandomChange]
            print(f"For the small price of {lstItemPurchasable[3]} Gold Coins, you can get your hands on one of these {lstItemPurchasable[0]}'s!")
            strPurchaseOption = input("Do you want to purchase this item? [Yes/No]: ")
            if strPurchaseOption.lower() == "yes" and intGoldCoin >= lstItemPurchasable[3]:
                print("You purchased the Item!")

            elif strPurchaseOption.lower() == "yes" and intGoldCoin >= lstItemPurchasable[3]:
                print("You do not have enough gold to purchase this item")
            elif strPurchaseOption.lower() == "no":
                print("Okay, come again soon!")
            else:
                print("You took to long to type Yes or No. (didnt say yes or no) You lost your opportunity.")
print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nYou Lost the game at Stage {intGameRound}\nTry and get farther on your next run!")



