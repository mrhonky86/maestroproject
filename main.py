# --- GLOBAL STATE (The AI Game Master's Database) ---
player = {
    "name": "",
    "logic_points": 5,
    "inventory": ["Battered Keyboard"],
    "current_floor": 1
}

# --- THE ENGINE ---
def start_game():
    print("--- WELCOME TO THE MAESTRO WORLD DUNGEON ---")
    player["name"] = input("Enter your username, Crawler: ")
    print(f"\nAI Voice: 'Greetings, {player['name']}. You have been flattened into Python code.'")
    dungeon_entrance() # This will call the first room

# --- YOUR ROOMS WILL GO BELOW THIS LINE ---
def dungeon_entrance():
    print("\nYou are in the Syntax Pit. Green code drips from the ceiling.")
    # More logic will go here once others contribute!
