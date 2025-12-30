def dungeon_entrance():
    print("\n" + "="*40)
    print("      LOCATION: THE ARCHIVE OF ANXIETY")
    print("="*40)
    print("AI Voice: 'Crawler, stop looking for a mouse. It's not coming back.'")
    print("\nYou are standing in a small room lined with dusty monitors.")
    print("On a pedestal in the center sits a single, glowing **USB Drive**.")
    print("To the NORTH is a heavy iron door labeled: THE TERMINAL.")

    # The Choice Loop
    while True:
        choice = input("\nWhat do you do? [take] the drive or [go north]? ").lower()

        if "take" in choice:
            if "Glinting USB Drive" not in player["inventory"]:
                print("\nYou grab the drive. It feels warm. You've gained +1 Logic!")
                player["inventory"].append("Glinting USB Drive")
                player["logic"] += 1
            else:
                print("\nYou've already taken the drive. Don't be greedy.")

        elif "north" in choice or "go" in choice:
            print("\nYou push open the iron door and step into the darkness...")
            # This calls the NEXT student's function
            the_terminal() 
            break # Exit the loop when moving to a new room

        else:
            print("\nAI Voice: 'That wasn't an option. Use your brain, if you still have one.'")