# --- SHARED STATE (The Global Database) ---
player = {
    "name": "",
    "inventory": [],
    "logic": 5,
    # Hidden Room Progress
    "found_secret_passage": False, 
    "barrier_deactivated": False,
    "safe_cracked": False
}


# --- START ENGINE ---
def start_game():
    player["name"] = input("Crawler, identify yourself: ")
    dungeon_entrance()

# --- THE MAP (Students will replace these) ---

def dungeon_entrance():
    print("\nYou are at the entrance. A sign reads: 'Abandon all hope, ye who forget semicolons.'")
    choice = input("Do you [enter] the Terminal? ")
    if "enter" in choice.lower():
        the_terminal()
    else:
        dungeon_entrance()

def the_terminal():
    print("\n[ROOM NOT BUILT YET]")
    # Student assigned to 'the_terminal' will replace this entire function!
    the_breakroom() 

def the_breakroom():
    print("\n[ROOM NOT BUILT YET]")
    coffee_grotto()

def coffee_grotto():
    print("\n[ROOM NOT BUILT YET]")
    infinite_loop()

def infinite_loop():
    print("\n[ROOM NOT BUILT YET]")
    print("GAME OVER: You haven't built the boss yet!")

if __name__ == "__main__":
    start_game()
