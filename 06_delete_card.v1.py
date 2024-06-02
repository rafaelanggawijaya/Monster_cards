"""Monster cards -menu- v1
This component gives control which part the
user wants to use and allows the user to pick them
Update:"""

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
        print("Add New monster")
    # when user chooses search/edit
    elif option == "Search for a Monster":
        print("Search for a monster")
    # when user chooses delete card
    elif option == "Destroy a Monster":
        while True:
            # user enters monster card to remove from dictionary
            monster_search = easygui.enterbox("Please choose a monster to "
                                              "remove from the dungeon, "
                                              "Traveler:", "Searching for "
                                                           "Monster")
            # prints monster stats for user to see and checks if it is in
            # the dictionary
            if monster_search in monster_cards:
                # prints name
                print(f"{monster_search}\nStats:\n")
                # prints stats
                for stat, value in monster_cards[monster_search].items():
                    print(f"      {stat}: {value}")
                easygui.msgbox(
                    "The monster you have searched has its stats and name "
                    "printed"
                    "below")


                del monster_cards[monster_search]
                easygui.msgbox(
                    f"The monster, {monster_search} has been "
                    f"removed for the dungeon.")

                break

    # when user chooses show all cards
    elif option == "Show all Monsters":
        print("Show all Monsters")
    # when user wants to exit program
    else:
        print("Exit")
