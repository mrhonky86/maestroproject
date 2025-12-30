def the_breakroom():
    print("\n--- THE BREAKROOM ---")
    print("A hum of machinery fills the air. A heavy vending machine sits in the corner.")
    print("A tablet on the table says: 'UNAUTHORIZED ACCESS PROHIBITED.'")

    choice = input("\nDo you [inspect] the tablet or [exit] to the Terminal? ").lower()

    if "inspect" in choice:
        password = input("Enter Password: ").lower()
        if password == "password":
            print("\n*RUMBLE... SLIDE*")
            print("The vending machine moves! A dark passage leads to a [secret] room.")
            player["found_secret_passage"] = True

            # Offer to enter the new path immediately
            move = input("Do you enter the [secret] passage? ").lower()
            if "secret" in move:
                hidden_archive()
            else:
                the_breakroom()
        else:
            print("The screen flashes red: 'IDTEN-T ERROR detected.'")
            the_breakroom()

    elif "exit" in choice:
        the_terminal()