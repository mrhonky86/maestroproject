import random

# --- SHARED STATE (The Global Database) ---
# Students can access these using player["logic"], etc.
player = {
    "name": "",
    "inventory": [],
    "logic": 5,
    "found_secret_passage": False, 
    "barrier_deactivated": False,
    "safe_cracked": False
}

# --- START ENGINE ---
def start_game():
    print("WELCOME TO THE MAESTRO WORLD DUNGEON")
    player["name"] = input("Crawler, identify yourself: ")
    dungeon_entrance()

# --- THE MAP (Ordered Sequence) ---

def dungeon_entrance():
    print(f"\nWelcome, {player['name']}. You are at the Entrance.")
    print("A sign reads: 'Abandon all hope, ye who forget semicolons.'")
    choice = input("Do you [enter] the Terminal? ").lower()
    if "enter" in choice:
        the_terminal()
    else:
        dungeon_entrance()

def the_terminal():
    print("\n[THE TERMINAL: This room is currently under construction.]")
    # Student: Write your room logic here. 
    # Must end by calling coffee_grotto()
    coffee_grotto() 

def coffee_grotto():
    print("\n[THE COFFEE GROTTO: This room is currently under construction.]")
    # Student: Write your room logic here.
    # Must end by calling infinite_loop()
    infinite_loop()

def infinite_loop():
    print("\n[THE INFINITE LOOP HALLWAY: This room is currently under construction.]")
    # Student: Write your room logic here.
    # Must end by calling the_breakroom()
    the_breakroom() 

def the_breakroom():
    print("\n[THE BREAKROOM: This is the Lead Architect's room.]")
    # Ray will insert the Secret Archive and Tablet logic here later.
    print("The journey ends here for now.")

# --- EXECUTION ---
if __name__ == "__main__":
    start_game()
