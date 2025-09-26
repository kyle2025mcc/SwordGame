import sys
import random

# stats for the player
player_power = 1
player_defense = 0
player_defense_stat = 7
player_health_stat = 15
player_heal_stat = 1
player_heal = 0
player_health = 0
enemy_amount = 1
enemy_shield = 0
# function for a player's actions
def choice ():
    global player_defense
    global player_health
    global player_power
    global player_defense_stat
    global player_health_stat
    global player_heal
    global enemy_health
    global player_heal_stat
    global enemy_shield
    c = input("What would you like to do attack (a) defend (d) or heal (h)?")
    print( )
    #attack

    if c == "a" or c == "attack":
        for i in range (player_power):
            attack_chance = random.randint(1, 10)
            if attack_chance != (9 or 10):
                if (enemy_shield <= 0):
                    enemy_health = enemy_health - 5
                    print("You hit them!")
                    print( )
                else:
                    if (enemy_shield > 0):
                        enemy_shield = enemy_shield - 5
                        print("You hit their shield!")
                        if (enemy_shield < 0):
                            enemy_health = enemy_health + enemy_shield
                            print("and were able to cut through damaging both them and their shield!")

            else:
                print("They dodged your attack!")
                print( )
    #defend  
                          
    elif c == "d" or c == "defend":
        player_defense = player_defense + player_defense_stat
        print("You bring out your shield to defend!")
        print( )
    #heal
        
    elif c == "h" or h == "heal":
        if (player_heal > 0):
            player_health = player_health + 30
            player_heal = player_heal - 1
            print("You took out a potion and healed.")
            print( )
            if (player_health > player_health_stat):
                player_health = player_health_stat
        else:
            print("You tried to heal, but realize you have no potions left.")
    else:
        print("You seem to be confused.")
    return choice

# function for battle
def battle (attack_value):
    global player_defense
    global player_health
    global enemy_amount
    attack_value = attack_value
    if (enemy_amount == 1):
        if (player_defense > 0):
            player_defense = player_defense - attack_value
            print("The enemy hits your shield!")
            if (player_defense < 0):
                player_health = player_health + player_defense
                print("And deals damage to you, damaging your shield!")
        else:
            player_health = player_health - attack_value 
            print("The enemy hit you!")
    else:
        attack_value = attack_value * enemy_amount
        if (player_defense > 0):
            player_defense = player_defense - attack_value
            print("The enemies hit your shield!")
            if (player_defense < 0):
                player_health = player_health + player_defense
                print("And deal damage to you and your shield is now damaged!")
        else:
            player_health = player_health - attack_value 
            print("The enemies hit you!")


    return battle

# function for upgrade
def upgrade():
    global player_defense_stat
    global player_heal_stat
    global player_health_stat
    global player_power
    defense_upgrade = random.randint(3,10)
    heal_upgrade = random.randint(1,2)
    health_upgrade = random.randint(10,20)
    power_upgrade = random.randint(1,2)
    player_defense_stat = player_defense_stat + defense_upgrade
    player_heal_stat = player_heal_stat + heal_upgrade
    player_health_stat = player_health_stat + health_upgrade
    player_power = player_power + power_upgrade

# function for battle setup
def setup(h,a):
    global player_health
    global player_health_stat
    global player_defense
    global enemy_health
    global player_heal
    global player_heal_stat
    global enemy_amount
    player_health = player_health_stat
    player_defense = 0
    player_heal = player_heal_stat
    enemy_health = h
    enemy_amount = a

# intro narration
print( )
print("The king has been captured by the evil Lord Pie and is being held in the evil castle near the Great Volcano. As a brave knight you must save the king. Good luck!")
print("You start the journey towards the castle and encounter one lone soldier on the path. He challanges you to a duel.")

# battle
setup(20,1)
while (enemy_health > 0):
    print( )
    print("You have " + str(player_health) + " health and " + str(player_heal) + " potion. The enemy has " + str(enemy_health) + " health.")
    if (player_defense > 0):
        print("You are also shielding for " + str(player_defense) + " health.")
    choice()
    if (enemy_health <= 0):
        break
    battle(5)
    if (player_health <= 0):
        sys.exit("Game Over!")
print("Congragulations you beat the lone soldier.")
print("You feel stronger after the fight and you looted the defeated soldier.")
upgrade()
print( )
print("You arrive at the castle of the evil Lord Pie. At the entrance ten soldiers await for you. They draw their weapons. You have your eyes locked on your first target.")
setup(12,10)
while (enemy_amount > 0):
    print( )
    print("You have " + str(player_health) + " health and " + str(player_heal) + " potions. There are " + str(enemy_amount) + " enemies. Your current target has " + str(enemy_health) + " health.")
    if (player_defense > 0):
        print("You are also shielding for " + str(player_defense) + " health.")
    choice()
    if (enemy_health <= 0):
        enemy_amount = enemy_amount - 1
        enemy_health = 12
    if (enemy_amount == 0):
        break
    battle(1)
    if (player_health <= 0):
        sys.exit("Game Over!")    
print("You beat the soldiers guarding the castle. You now feel stronger after looting the soldiers.")
upgrade()
print( )
print("You go to the top of the castle where you find Lord Pie. Behind him you see the king of your land. You get into position to duel Lord Pie. Before you duel, Lord Pie begins to summon chunks of magma from The Volcano.")
setup(125,1)
enemy_shield = 0
enemy_heal = 2
while (enemy_health > 0):
    print( )
    print("You have " + str(player_health) + " health and " + str(player_heal) + " potions. Lord Pie has " + str(enemy_health) + " health.")
    if (player_defense > 0):
        print("You are also shielding for " + str(player_defense) + " health.")
    if (enemy_shield > 0):
        print("Lord Pie is shielding for " + str(enemy_shield) + " health.")
    choice()
    if (enemy_health <= 0):
        break
    pie_choice = random.randint(1,6)
    if (pie_choice == 1 or pie_choice == 2 or pie_choice == 3):
        battle(9)
    elif (pie_choice == 6 or pie_choice == 5):
        enemy_shield = enemy_shield + 16
        print("Lord Pie took out a shield, defending himself.")
    else:
        if (enemy_heal > 0):
            enemy_health = 125
            enemy_heal = enemy_heal - 1
            print("Lord Pie healed himself to full power.")
        else:
            print("Lord Pie forgot he has no more heals. This is your chance.")
    rock_chance = random.randint(1,3)
    if rock_chance == 1:
        player_health = player_health - 5
        print( )
        print("A piece of magma hits you!")
    if (player_health <= 0):
        sys.exit("Game Over!")
print("You defeated Lord Pie. The king is now safe and you are the new head of knights. You are the new hero of the town!")
print("Thank you for playing!")