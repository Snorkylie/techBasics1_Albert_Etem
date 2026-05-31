import random
import time
import os
import copy
import csv
import datetime


# DEBUG FLAG – set to True to skip the game and only test the record system
DEBUG = True

# CONSTANTS: change these to tweak the whole game in one place

# Class: Mage
MAGE_HEALTH = 80
MAGE_MANA = 150
MAGE_SPELLS = ["Fireball", "Ice Shard"]

# lass: Swordmage
SWORDMAGE_HEALTH = 120
SWORDMAGE_MANA = 80
SWORDMAGE_SPELLS = ["Flame Slash", "Mana Shield"]
SWORDMAGE_STAMINA = 100

# Combat values
SPELL_COST = 20
POTION_HEAL = 25
MANA_SHIELD_GAIN = 20
PLAYER_DMG_MIN = 20
PLAYER_DMG_MAX = 25
SPELL_DMG_MIN = 30
SPELL_DMG_MAX = 35
ERLANG_MAX_HP = 150
ERLANG_DMG_MIN = 10
ERLANG_DMG_MAX = 22

# World map template (deep-copied in main so items can be removed safely)
WORLD_MAP = {
    "Trebla": {
        "east": "Ruins of Zaramunz",
        "item": "Spell of Trebla"
    },
    "Ruins of Zaramunz": {
        "north": "Valley of lost souls",
        "west": "Trebla",
        "item": "potion"
    },
    "Valley of lost souls": {
        "south": "Ruins of Zaramunz",
        "east": "Róses End",
        "item": "Dark key of Róse"
    },
    "Róses End": {
        "west": "Valley of lost souls"
    }
}

STARTING_LOCATION = "Trebla"
RECORDS_FILE = "shanren_records.csv"


# UTILITY

def clear():
    #Clears the terminal screen on both Windows and Mac/Linux.
    os.system('cls' if os.name == 'nt' else 'clear')


def hp_bar(current, maximum, length=20):
    """
    Builds a visual HP bar string.
    Arguments : current  – current HP
                maximum  – maximum HP
                length   – bar width in characters (default 20)
    Returns   : formatted string e.g. 'HP: [████░░░░] 60/80'
    """
    filled = int((current / maximum) * length)
    empty = length - filled
    bar = "█" * filled + "░" * empty
    return f"HP: [{bar}] {current}/{maximum}"


def shield_bar(current, maximum=100, length=20):
    """
    Builds a visual Shield bar string rendered in blue.
    Arguments : current  – current shield value
                maximum  – maximum shield value (default 100)
                length   – bar width in characters (default 20)
    Returns   : formatted string with ANSI blue colouring
    """
    filled = int((current / maximum) * length)
    empty = length - filled
    bar = "█" * filled + "░" * empty
    blue = "\033[34m"  # ANSI blue
    reset = "\033[0m"
    return f"Shield: [{blue}{bar}{reset}] {current}/{maximum}"


def show_instructions():
    """Prints the command reference card."""
    print('''
Rogue-like RPG – World of Shanren
==================================
Commands:
  go [direction]    – move (e.g. go east)
  get [item]        – pick up an item
  use [item]        – use an item (e.g. use potion)
    ''')


# PLAYER CREATION

def get_player_name():
    """
    Prompts the player for their character name.
    Returns : name as a string
    """
    return str(input("Enter the great savior's name: "))


def choose_class(player_name):
    """
    Shows a class-selection menu and loops until a valid choice is made.
    Arguments : player_name – used in the confirmation message
    Returns   : selected class as a string ('Mage' or 'Swordmage')
    """
    while True:
        print("1 = Mage")
        print("2 = Swordmage")
        choice = input("Please select the class you would like to start with: ")

        if choice == "1" or choice.lower() == "mage":
            print(f"{player_name} has chosen the path of the Mage!")
            clear()
            return "Mage"

        elif choice == "2" or choice.lower() == "swordmage":
            print(f"{player_name} has chosen the path of the Swordmage!")
            clear()
            return "Swordmage"

        else:
            print(f"'{choice}' is not a valid class! Please choose 1 or 2.")


def create_player(name, chosen_class):
    """
    Builds a player dictionary with all starting stats.
    Arguments : name         – the player's chosen name
                chosen_class – 'Mage' or 'Swordmage'
    Returns   : dict with keys: name, class, health, max_health,
                mana, spells, stamina, shield
    """
    if chosen_class == "Mage":
        return {
            "name": name,
            "class": chosen_class,
            "health": MAGE_HEALTH,
            "max_health": MAGE_HEALTH,
            "mana": MAGE_MANA,
            "spells": list(MAGE_SPELLS),  # list() so the constant stays untouched
            "stamina": None,
            "shield": 0
        }
    else:  # Swordmage
        return {
            "name": name,
            "class": chosen_class,
            "health": SWORDMAGE_HEALTH,
            "max_health": SWORDMAGE_HEALTH,
            "mana": SWORDMAGE_MANA,
            "spells": list(SWORDMAGE_SPELLS),
            "stamina": SWORDMAGE_STAMINA,
            "shield": 0
        }



# HUD / STATUS

def status(player, current_location, inventory, locations):
    """
    Prints the full HUD: location, inventory, class, HP, shield, mana, spells.
    Arguments : player           – player dict
                current_location – name of the current room
                inventory        – list of collected items
                locations        – world map dict (to check for items at location)
    """
    print("------------------")
    print(f"Location : {current_location}")
    print(f"Inventory: {inventory}")
    print("------------------")
    print(f"Class  : {player['class']}")
    print(hp_bar(player["health"], player["max_health"]))

    if player["shield"] > 0:
        print(shield_bar(player["shield"]))

    print(f"Mana   : {player['mana']}")
    print(f"Spells : {player['spells']}")

    if player["stamina"] is not None:  # stamina only shown for Swordmage
        print(f"Stamina: {player['stamina']}")

    print("------------------")

    if "item" in locations[current_location]:
        print(f"You discovered: {locations[current_location]['item']}!")

    print("------------------")



# COMBAT HELPERS

def print_combat_hud(player, erlang_health):
    """
    Prints the combat status bar and available actions.
    Arguments : player        – player dict
                erlang_health – current boss HP
    """
    print(f"\n{hp_bar(player['health'], player['max_health'])}")

    # Erlang's HP bar
    filled = int((erlang_health / ERLANG_MAX_HP) * 20)
    empty = 20 - filled
    print(f"Erlang HP: [{'█' * filled}{'░' * empty}] {erlang_health}/{ERLANG_MAX_HP}")
    print("------------------")

    print("1 = Attack")
    for i, spell in enumerate(player["spells"]):
        print(f"{i + 2} = {spell}  (costs {SPELL_COST} Mana)")
    print(f"{len(player['spells']) + 2} = Use Potion")


def erlang_attacks(player):
    """
    Erlang deals random damage, draining shield before HP.
    Arguments : player – player dict (health / shield change in-place)
    """
    damage = random.randint(ERLANG_DMG_MIN, ERLANG_DMG_MAX)

    if player["shield"] > 0:
        if damage <= player["shield"]:
            player["shield"] -= damage
            print(f"Erlang strikes for {damage} – your shield absorbs it all!")
            print(shield_bar(player["shield"]))
        else:
            leftover = damage - player["shield"]
            print(f"Erlang strikes for {damage}! Your shield breaks! You take {leftover} damage!")
            player["shield"] = 0
            player["health"] -= leftover
    else:
        player["health"] -= damage
        print(f"Erlang strikes back for {damage} damage!")

    time.sleep(2)



# BOSS FIGHT

def boss_fight(player, inventory):
    """
    Runs the full fight against Dark Prince Erlang.
    Arguments : player    – player dict (stats change in-place)
                inventory – item list (potions can be consumed)
    Returns   : True if the player wins, False if the player loses
    """
    erlang_health = ERLANG_MAX_HP

    print("------------------")
    print("Dark Prince Erlang steps out of the shadows...")
    print("Erlang: 'You dare enter my domain? You will regret this!'")
    print("------------------")
    time.sleep(3)

    while player["health"] > 0 and erlang_health > 0:

        print_combat_hud(player, erlang_health)
        action = input("> ")

        # Basic attack
        if action == "1":
            dmg = random.randint(PLAYER_DMG_MIN, PLAYER_DMG_MAX)
            erlang_health -= dmg
            print(f"You strike Erlang for {dmg} damage!")

        # Spell actions
        elif action in [str(i + 2) for i in range(len(player["spells"]))]:
            if player["mana"] >= SPELL_COST:
                spell_name = player["spells"][int(action) - 2]
                player["mana"] -= SPELL_COST

                if spell_name == "Mana Shield":
                    player["shield"] += MANA_SHIELD_GAIN
                    print(f"You cast Mana Shield! +{MANA_SHIELD_GAIN} shield! (Mana: {player['mana']})")
                else:
                    dmg = random.randint(SPELL_DMG_MIN, SPELL_DMG_MAX)
                    erlang_health -= dmg
                    print(f"You activated {spell_name} for {dmg} damage! (Mana: {player['mana']})")
            else:
                print("Not enough mana! Choose another action.")
                continue

        # Potion
        elif action == str(len(player["spells"]) + 2):
            if "potion" in inventory:
                if player["health"] == player["max_health"]:
                    print("You are already at full health!")
                    continue
                player["health"] = min(player["health"] + POTION_HEAL, player["max_health"])
                inventory.remove("potion")
                print(f"You drink the potion and restore {POTION_HEAL} HP!")
                print(hp_bar(player["health"], player["max_health"]))
            else:
                print("You don't have a potion!")
                continue

        else:
            print("Invalid action! Pick a number from the list.")
            continue

        # Check win condition
        if erlang_health <= 0:
            print("------------------")
            print(f"Erlang falls to his knees... '{player['name']}, you are stronger than I thought...'")
            time.sleep(4)
            print("After a glorious fight you defeat the prince and move on to the City of Rinnen...")
            time.sleep(3)
            print("This journey is to be continued in the next chapter...")
            print("------------------")
            return True

        # Erlang counter-attacks
        erlang_attacks(player)

        # Check loss condition
        if player["health"] <= 0:
            print("------------------")
            print(f"Erlang: 'Pathetic... {player['name']} was never worthy of this world.'")
            time.sleep(4)
            print(f"{player['name']} has been defeated. Your journey ends here...")
            print("------------------")
            return False



# GAME ACTIONS

def handle_movement(direction, player, current_location, locations, inventory):
    """
    Tries to move the player in the given direction.
    Arguments : direction        – direction string (e.g. 'east')
                player           – player dict
                current_location – current room name
                locations        – world map dict
                inventory        – item list (needed for key check)
    Returns   : (new_location: str, boss_result: True/False/None)
                boss_result is only set after a boss fight; None otherwise
    """
    if direction not in locations[current_location]:
        print(f"Your powers are too low to go {direction}!")
        return current_location, None

    next_loc = locations[current_location][direction]

    # Gated area: requires the Dark key of Róse
    if next_loc == "Róses End":
        has_key = any(item.lower().replace("ó", "o") == "dark key of rose" for item in inventory)
        if has_key:
            print("You use the Dark key of Róse to unlock the gate...")
            time.sleep(4)
            print(f"You have now moved to {next_loc}!")
            time.sleep(4)
            clear()
            result = boss_fight(player, inventory)
            return next_loc, result
        else:
            print("The gate to Róses End is locked! You need the Dark key of Róse to enter.")
            return current_location, None

    print(f"You have now moved to {next_loc}!")
    return next_loc, None


def handle_get(item_name, current_location, locations, inventory):
    """
    Tries to pick up an item in the current location.
    Arguments : item_name        – item name the player typed
                current_location – current room name
                locations        – world map dict (item removed on pickup)
                inventory        – item list (item appended on pickup)
    """
    if "item" not in locations[current_location]:
        print("There is nothing left to pick up here!")
        return

    location_item = locations[current_location]["item"]

    # Normalise ó → o so both spellings are accepted
    if item_name.lower() == location_item.lower().replace("ó", "o"):
        if item_name in inventory:
            print(f"You already own the {item_name}!")
        else:
            print(f"You collected the {item_name}!")
            inventory.append(item_name)
            del locations[current_location]["item"]
    else:
        print(f"There is no '{item_name}' here!")


def handle_use(item_name, player, inventory):
    """
    Tries to use an item from the inventory.
    Arguments : item_name – item name the player typed
                player    – player dict (health changes on potion use)
                inventory – item list (item removed after use)
    """
    if item_name.lower() == "potion":
        if "potion" in inventory:
            if player["health"] == player["max_health"]:
                print("You are already at full health!")
            else:
                player["health"] = min(player["health"] + POTION_HEAL, player["max_health"])
                inventory.remove("potion")
                print(f"You drink the potion and feel refreshed! HP restored!")
                print(hp_bar(player["health"], player["max_health"]))
        else:
            print("You don't have a potion to drink!")
    else:
        print(f"You can't use '{item_name}' right now!")


# RECORD SYSTEM

def load_records():
    """
    Loads all saved records from the CSV file.
    Returns : list of dicts with keys: name, timestamp, score
              Returns empty list if file does not exist yet.
    """
    try:
        with open(RECORDS_FILE, "r") as f:
            reader = csv.DictReader(f)
            return list(reader)
    except FileNotFoundError:
        # No records file yet – that is fine, return empty list
        return []
    except Exception as e:
        print(f"Could not load records: {e}")
        return []


def save_record(name, timestamp, score):
    """
    Saves a new record to the CSV file.
    Loads existing records first, appends the new one, then writes everything back.
    Arguments : name      – player name
                timestamp – date and time string
                score     – HP remaining (0 if the player lost)
    """
    records = load_records()
    records.append({"name": name, "timestamp": timestamp, "score": score})

    try:
        with open(RECORDS_FILE, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["name", "timestamp", "score"])
            writer.writeheader()
            writer.writerows(records)
        print("Your record has been saved!")
    except Exception as e:
        print(f"Could not save record: {e}")


def show_leaderboard():
    """
    Loads and displays all records sorted by score (highest first).
    If no records are found, prints a message instead.
    """
    records = load_records()

    print("\n========= LEADERBOARD =========")

    if not records:
        print("No records found yet!")
        print("===============================\n")
        return

    # Sort by score highest first – int() converts the CSV string back to a number
    sorted_records = sorted(records, key=lambda x: int(x["score"]), reverse=True)

    for i, record in enumerate(sorted_records, 1):
        print(f"{i}. {record['name']:<15} Score: {record['score']:<5} | {record['timestamp']}")

    print("===============================\n")


# INTRO SEQUENCE

def show_intro():
    """Prints the opening story lines with dramatic pauses."""
    print("Welcome to the world of Shanren")
    time.sleep(3)
    print("You are in a specialized world of powers and crafts.")
    print("Every power determines how strong you will become.")
    print("Before entering you must choose: become a full Mage or a powerful Swordmage.")
    time.sleep(6)
    print("Choose wisely – this decision shapes how great a savior you will become!")
    time.sleep(5)


def show_opening(player_name, starting_location):
    """
    Prints the first in-game hint after the player is created.
    Arguments : player_name       – the player's name
                starting_location – name of the first room
    """
    print(f"To get stronger, {player_name} began their journey in {starting_location}!")
    print(f"The first way {player_name} should go is east of Trebla to the Ruins of Zaramunz.")
    time.sleep(5)



# MAIN  entry point

def main():
    """
    Runs the full game: intro → character creation → game loop.
    All mutable game state (player, inventory, locations) lives here
    and is passed into helper functions as arguments.
    """

    # DEBUG MODE: skips the whole game, only asks for a name and saves a placeholder record
    if DEBUG:
        print("--- DEBUG MODE ACTIVE ---")
        player_name = get_player_name()
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        score = 999  # placeholder score for testing
        print(f"DEBUG: Saving placeholder record for '{player_name}' with score {score}.")
        save_record(player_name, timestamp, score)
        show_leaderboard()
        return  # stop here, do not run the actual game

    # Intro
    show_intro()

    player_name = get_player_name()
    print(f"{player_name} was on a long journey before the world became a place of reckless battles.")
    time.sleep(6)
    print(f"Decide what powers {player_name} will master throughout the journey.")
    time.sleep(3)

    # Character creation
    chosen_class = choose_class(player_name)
    player = create_player(player_name, chosen_class)

    # Game state
    inventory = []
    locations = copy.deepcopy(WORLD_MAP)  # deep copy keeps the constant untouched
    current_location = STARTING_LOCATION

    # Track how long the player takes
    start_time = datetime.datetime.now()

    show_instructions()
    show_opening(player_name, current_location)

    # Main game loop
    game_result = None  # will be True (win) or False (loss) after the boss fight

    while True:
        clear()
        status(player, current_location, inventory, locations)
        raw = input("> ")
        move = raw.strip().split(" ", 1)

        if len(move) < 2:
            print("Please type a full command, e.g. 'go east' or 'get potion'.")
            time.sleep(2)
            continue

        command, argument = move[0].lower(), move[1]

        if command == "go":
            current_location, result = handle_movement(
                argument, player, current_location, locations, inventory
            )
            if result is False:  # player lost the boss fight
                game_result = False
                break
            if result is True:  # player won the boss fight
                game_result = True
                print("Type 'exit' to exit the game.")
                if input("> ").lower() == "exit":
                    break

        elif command == "get":
            handle_get(argument, current_location, locations, inventory)

        elif command == "use":
            handle_use(argument, player, inventory)

        else:
            print(f"Unknown command '{command}'. Try: go, get, use.")

        time.sleep(1)

    # Save record after the game ends
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if game_result is True:
        score = player["health"]   # remaining HP as score
        print(f"\nYou finished with {score} HP remaining!")
    else:
        score = 0                  # 0 points for losing

    save_record(player_name, timestamp, score)
    show_leaderboard()


if __name__ == "__main__":
    main()
