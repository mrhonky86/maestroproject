def hidden_archive():
    print("\n" + "!" * 40)
    print("      BONUS ROOM: THE MAESTRO'S PRIVATE VAULT")
    print("!" * 40)

    # Status display
    if not player["barrier_deactivated"]:
        print("A shimmering blue BARRIER blocks the safe and the Golden Keyboard.")
    else:
        print("The blue barrier is dead. The pedestal is accessible.")

    print("\nTo the NORTH, a massive door leads to the BOSS CHAMBER.")
    action = input("Do you [inspect] the safe, [take] the keyboard, or [go north]? ").lower()

    # 1. THE SAFE (The Reward)
    if "safe" in action:
        if not player["barrier_deactivated"]:
            print("\nYou can't reach the safe! The barrier is in the way.")
            hidden_archive()
        elif player["safe_cracked"]:
            print("\nThe safe is empty. You already have the knowledge.")
            hidden_archive()
        else:
            code = input("Enter 6-digit code: ")
            if code == "123456":
                print("\n*CLUNK* The safe opens! You read 'Python for Dummies'. +10 Logic!")
                player["logic"] += 10
                player["inventory"].append("Python for Dummies")
                player["safe_cracked"] = True
            else:
                print("\nWrong code! The keypad beeps mockingly.")
            hidden_archive()

    # 2. THE KEYBOARD (The Boss Weapon)
    elif "take" in action:
        if not player["barrier_deactivated"]:
            print("\n!!! ZAP !!! The barrier shocks you for -1 Logic.")
            player["logic"] -= 1
            # Simple deactivation hint
            if input("Attempt to disable barrier? (y/n): ").lower() == "y":
                player["barrier_deactivated"] = True
            hidden_archive()
        else:
            print("\nYou grab the Golden Keyboard!")
            player["inventory"].append("Golden Keyboard")
            hidden_archive()

    # 3. THE EXIT (Forward to Boss)
    elif "north" in action:
        print("\nYou take a deep breath and push open the final door...")
        boss_battle()  # This moves them forward regardless of the safe!

    else:
        print("\nInvalid choice. The Maestro is watching.")
        hidden_archive()