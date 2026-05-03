import random
import time
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


print("Welcome to the world of Shanren")

time.sleep(3)

print("You are in a specialized world of powers and crafts. Every power determinants how strong you will become.")
print("Before entering this world you have been blessed with an important decision, you can choose between becoming a full merged Mage or a powerful and intellectual Swordmage.")

time.sleep(6)

print("Choose wisely because this decision effects how great of a savior you will become!")

time.sleep(5)

player_Name = str (input("Enter the great saviors name: "))
print(f"{player_Name} was on a long journey before all of a sudden the world become a place of reckless battles and power.")


time.sleep(6)

print(f"Decide what powers {player_Name} will be mastering throughout the journey.")


time.sleep(3)

# Class definitions (stats were implemented later.)
class Mage:
    def __init__(self, player_Name, health, mana, spells):
        self.player_Name = player_Name
        self.health = health
        self.mana = mana
        self.spells = spells

class Swordmage:
    def __init__(self, player_Name, health, mana, spells, stamina):
        self.player_Name = player_Name
        self.health = health
        self.mana = mana
        self.spells = spells
        self.stamina = stamina


# Classes with a loop, so the player can choose.
while True:
    print("1 = Mage")
    print("2 = Swordmage")

    select_Class = input("Please select the class you would like to start your journey with: ")
    if select_Class == "1" or select_Class.lower() == "mage":
        selected_Class = "Mage"
        print(f"{player_Name} has chosen the path of the Mage!")
        clear()
        break

    elif select_Class == "2" or select_Class.lower() == "swordmage":
        selected_Class = "Swordmage"
        print(f"{player_Name} has chosen the path of the Swordmage!")
        clear()
        break

    else:
        print(f"'{select_Class}' is not a valid class! Please choose 1 or 2.")


if selected_Class == "Mage":
    player_health = 80
    player_bar_health = 80
    player_mana = 150
    player_spells = ["Fireball", "Ice Shard"]
    player_stamina = None  # Mage has no stamina

elif selected_Class == "Swordmage":
    player_health = 120
    player_bar_health = 120
    player_mana = 80
    player_spells = ["Flame Slash", "Mana Shield"]
    player_stamina = 100


player_shield = 0


time.sleep(2)

def show_instructions():
##print a main menu and the commands

 print('''
Rouge like RPG Game
==========
Commands:
  go [direction]
  get [item]
  use [item]
  ''')


#Have to use truediv here since we use the true division on a handmade class. so that it can go below zero like 0.66 (dunder method)
def hp_bar(current, maximum, length=20):
    filled = int((current / maximum) * length)
    empty = length - filled
    bar = "█" * filled + "░" * empty
    return f"HP: [{bar}] {current}/{maximum}"

#this is made by AI:  bar = "█" * filled + "░" * empty
    return f"HP: [{bar}] {current}/{maximum}"


#After I decided to make the Mana shield, I deleted another def and had to define the shield aka i didn't have to but I decided to make it like the hp bar for a better visual.
#Reused from Ai for the blue bar since I still don't know how to do the "█" and "░".
def shield_bar(current, maximum=100, length=20):
    filled = int((current / maximum) * length)
    empty = length - filled
    bar = "█" * filled + "░" * empty # <-- Made by AI
    blue = "\033[34m" # <-- Made by Ai
    reset = "\033[0m" # Same here Since I didn't knew the exact color codes
    return f"Shield: [{blue}{bar}{reset}] {current}/{maximum}"



def status():
    print("------------------")
    print(f"current_locations: {current_location}")
    print(f"Inventory: {inventory}")
    print("------------------")
    print(f"Class: {selected_Class}")
    print(hp_bar (player_health, player_bar_health))

    if player_shield > 0:
        print(shield_bar(player_shield))

    print(f"Mana: {player_mana}")
    print(f"Spells: {player_spells}")

    if player_stamina is not None:  # Only show stamina when Swordmage is choosen.
        print(f"Stamina: {player_stamina}")
    print("------------------")


    if "item" in locations[current_location]:
        location_item = locations[current_location]["item"]
        print(f"So you discovered {location_item}!")
    print("------------------")


#Necessarys
def boss_fight():
    global player_health, player_mana, player_shield #<- shield was made on tuesday 00:45 cry emoji....

    erlang_health = 150
    erlang_max_health = 150

    print("------------------")
    print("Dark Prince Erlang steps out of the shadows...")
    print("Erlang: 'You dare enter my domain? You will regret this!'")
    print("------------------")

    time.sleep(3)


    while player_health > 0 and erlang_health > 0:
        print(f"\n{hp_bar(player_health, player_bar_health)}")
        print(f"Erlang  HP: [{'█' * int((erlang_health / erlang_max_health) * 20)}{'░' * (20 - int((erlang_health / erlang_max_health) * 20))}] {erlang_health}/{erlang_max_health}")
        print("------------------")
        print("1 = Attack")
        for i, spell in enumerate(player_spells):
            print(f"{i + 2} = {spell} (costs 20 Mana)")
        print(f"{len(player_spells) + 2} = Use Potion")


        action = input("> ")

        if action == "1":
            damage = random.randint(20, 25)
            erlang_health -= damage
            print(f"You strike Erlang for {damage} damage!")

        elif action in [str(i + 2) for i in range(len(player_spells))]:
            if player_mana >= 20:
                spell_name = player_spells [int(action) - 2]
                player_mana -= 20

                #new spell check.for MANA
                if spell_name == "Mana Shield":
                    player_shield += 20
                    print(f"You cast Mana Shield! You gained 20 shield! (Mana: {player_mana})")

                else:
                    damage = random.randint(30, 35)
                    erlang_health -= damage
                    print(f"You activated {spell_name} and hit Erlang for {damage} damage! (Mana: {player_mana})")

            else:
                print("Not enough mana! Choose another action.")
                continue

        elif action == str(len(player_spells) + 2):
            if "potion" in inventory:
                if player_health == player_bar_health:
                    print("You are already at full health!")
                    continue
                else:
                    player_health = min(player_health + 25, player_bar_health)
                    inventory.remove("potion")
                    print(f"You drink the potion and restore 25 HP!")
                    print(hp_bar(player_health, player_bar_health))
            else:
                print("You don't have a potion!")
                continue

        else:
            print("Invalid action! Choose 1 or 2.")
            continue


        # Check if erlang has been defeated
        if erlang_health <= 0:
            print("------------------")
            print(f"Erlang falls to his knees... '{player_Name}, you are stronger than I thought...'")
            time.sleep(4)
            print("After the first of many glorious fights you defeat the prince and move on with your Journey to the City of Rinnen...")
            time.sleep(3)

            print("This journey is to be continued in the next chapter...")
            print("------------------")
            return True   # Spieler gewinnt

        # Erlang is attacking
        erlang_damage = random.randint(10, 22)

        #First erlang needs to take out the shield that is why I deleted the player_health and changed it to player_shield
        if player_shield > 0:
            if erlang_damage <= player_shield:
                player_shield -= erlang_damage
                print(f"Erlang strikes for {erlang_damage} damage but your shield absorbs it!")
                print(shield_bar(player_shield))
            else:
                leftover = erlang_damage - player_shield
                print(f"Erlang strikes for {erlang_damage} damage! Your shield breaks! You take {leftover} damage!")
                player_shield = 0
                player_health -= leftover
        else:
            player_health -= erlang_damage
            print(f"Erlang strikes back for {erlang_damage} damage!")

        time.sleep(2)

        # checking if the player lost
        if player_health <= 0:
            print("------------------")
            print(f"Erlang: 'Pathetic... {player_Name} was never worthy of this world.'")
            time.sleep(4)
            print(f"{player_Name} has been defeated. Your journey ends here...")
            print("------------------")
            return False  # player loses



inventory = []
locations = {
             "Trebla" : {
                         "east": "Ruins of Zaramunz",
                         "item": "Spell of Trebla"
                        },
             "Ruins of Zaramunz": {
                                   "north": "Valley of lost souls",
                                   "west" : "Trebla",
                                   "item" : "potion"
                                  },
             "Valley of lost souls": {
                                      "south": "Ruins of Zaramunz",
                                      "east" : "Róses End",
                                      "item" : "Dark key of Róse"
                                     },
             "Róses End"           : {
                                      "west" : "Valley of lost souls"
                                     }
                        }

current_location = "Trebla"

show_instructions()
print(f"To get stronger {player_Name} began they journey in {current_location}!")
print(f"The first way {player_Name} should go is east of Trebla to the Ruins of Zaramunz.")


time.sleep(5)


while True:
    clear()
    status()
    move = input(">")
    move = move.split(" ", 1)


    if move[0] == "go":
        if move[1] in locations[current_location]:
            next_location = locations[current_location][move[1]]

            # Checking if player has what it takes to go to Roses End
            if next_location == "Róses End":
                if any(item.lower().replace("ó", "o") == "dark key of rose" for item in inventory):
                    current_location = next_location
                    print(f"You use the Dark key of Róse to unlock the gate...")
                    time.sleep(4)
                    print(f"You have now moved to {current_location}!")
                    time.sleep(4)
                    clear()
                    result = boss_fight()
                    if not result:
                        break

                    # I was too bored so decided to make a temporary exit mode.
                    if result:
                        print("Type 'exit' to exit the game.")
                        ending = input("> ")
                        if ending.lower() == "exit":
                            break


                else:
                    print("The gate to Róses End is locked! You need the Dark key of Róse to enter.")
            else:
                current_location = next_location
                print(f"You have now moved to {current_location}!")

        else:
            print(f"Your mage powers are to low to go {move[1]}!")


    if move[0] == "get":
        # checking if there even is a item
        if "item" in locations[current_location]:
            location_item = locations[current_location]["item"]

            if move[1].lower() == location_item.lower().replace("ó", "o"): # <-- I had to remade this part since it would only accept the special o and not the normal o now it works but it took 3 hours to fix...
                # checking if item is or has been pikced up into the inventory
                if {move[1]} in inventory:
                    print(f"You already own the {move[1]}!")
                else:
                    print(f"You collected the {move[1]}!")
                    inventory.append(move[1])
                    del locations[current_location]["item"]  # taking Item off Location

            else:
                print(f"There is no '{move[1]}' here!")
        else:
            print(f"There is nothing left to pick up, you already own the {move[1]}!!")



    if move[0] == "use":
        if move[1].lower() == "potion":
            if "potion" in inventory:
                #checking that hp is'nt over the max. So that it does not overheal.
                if player_health == player_bar_health:
                    print("You are already at full health!")

                else:
                    player_health = min(player_health + 25, player_bar_health)
                    inventory.remove("potion")
                    print(f"You drink the potion and feel refreshed! You have restored your HP!")
                    print(hp_bar(player_health, player_bar_health))
            else:
                print(f"You don't have a potion to drink!")
        else:
            print(f"You can't use '{move[1]} right now!")