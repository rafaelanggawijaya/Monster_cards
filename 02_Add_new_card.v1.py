"""Monster cards -add new card- v1
This component allows the user to add new cards to the card list
Update: added, add card code from trialing """

import easygui

# dictionary of cards
monster_cards = {"Stoneling": {"Strength": 7, "Speed": 1, "Stealth": 25,
                               "Cunning": 15},
                 "Vexscream": {"Strength": 1, "Speed": 6, "Stealth": 21,
                               "Cunning": 19},
                 "Dawnmirage": {"Strength": 5, "Speed": 15, "Stealth": 18,
                                "Cunning": 22},
                 "Blazegolem": {"Strength": 15, "Speed": 20, "Stealth": 23,
                                "Cunning": 6},
                 "Websnake": {"Strength": 7, "Speed": 15, "Stealth": 10,
                              "Cunning": 5},
                 "Moldvine": {"Strength": 21, "Speed": 18, "Stealth": 14,
                              "Cunning": 5},
                 "Vortexwing": {"Strength": 19, "Speed": 13, "Stealth": 19,
                                "Cunning": 2},
                 "Rotthing": {"Strength": 16, "Speed": 7, "Stealth": 4,
                              "Cunning": 12},
                 "Froststep": {"Strength": 14, "Speed": 14, "Stealth": 17,
                               "Cunning": 4},
                 "Wispghoul": {"Strength": 17, "Speed": 19, "Stealth": 3,
                               "Cunning": 2}}

# Main routine

# Welcome message
easygui.msgbox("Welcome to the Monster card "
               "Dungeon\n~~~~~~~~~~~~~~~~~~~~~~~~~~", "Welcome Traveler")

# Menu/options
while True:
    # asks what the user wants to do
    option = easygui.buttonbox("Choose what you want to do, Traveler",
                               "Choose Wisely",
                               ["Add New Monster", "Search for a Monster",
                                "Destroy a Monster", "Show all Monsters",
                                "Exit"])
    # when user chooses add card
    if option == "Add New Monster":
        # add card

        # asks for name
        name = easygui.enterbox(
            "Enter the name of the Monster you would like to add")
        # makes a dictionary for that cards name
        monster_cards[name] = {}

        # ask user for strength stat and adds strength stats
        strength = easygui.enterbox(
            "Please enter the strength stat for this card")
        monster_cards[name]["Strength"] = strength

        # ask user for speed stat and adds speed stats
        speed = easygui.enterbox("Please enter the speed stat for this card")
        monster_cards[name]["Speed"] = speed

        # ask user for stealth stat and adds stealth stats
        stealth = easygui.enterbox(
            "Please enter the stealth stat for this card")
        monster_cards[name]["Stealth"] = stealth

        # ask user for Cunning stat and adds cunning stats
        cunning = easygui.enterbox(
            "Please enter the strength stat for this card")
        monster_cards[name]["Cunning"] = cunning

    # when user chooses search/edit
    elif option == "Search for a Monster":
        print("Search for a monster")
    # when user chooses delete card
    elif option == "Destroy a Monster":
        print("Destroy a Monster")
    # when user chooses show all cards
    elif option == "Show all Monsters":
        print("Show all Monsters")
    # when user wants to exit program
    else:
        print("Exit")
