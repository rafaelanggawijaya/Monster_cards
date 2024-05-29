"""Monster cards -add new card- v4
This component allows the user to add new cards to the card list
Update: change part into a function which makes breaking the loop much
easier instead of using an extra variable
Added: Upper and lower bound of 1 and 25 for stats to fit requirement"""

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


# Functions
def add_card():
    # add card

    new_card = {}
    while True:
        # asks for name
        name = easygui.enterbox(
            "Enter the name of the Monster you would like to add")
        # if user wants to cancel
        if name is None:
            return
        # makes a dictionary for that cards name
        new_card[name] = {"Strength": 0, "Speed": 0, "Stealth": 0,
                          "Cunning": 0}
        for stat_name, stats in new_card[name].items():
            new_stat = easygui.integerbox(
                f"Please enter the {stat_name} "
                f"for this monster", upperbound=25, lowerbound=1)
            if new_stat is None:
                new_card.clear()
                return
            new_card[name][stat_name] = new_stat
        while True:
            # prints name
            print(f"{name}")
            # prints ~ line for aesthetics
            print("~" * len(name))
            print()
            # prints stats
            for stat, value in new_card[name].items():
                print(f"      {stat}: {value}")
            print()
            easygui.msgbox(
                "The monster you have searched has its stats and name "
                "printed"
                "below")
            # checks if user is done or wants to make new edits or wants to
            # cancel
            check = easygui.buttonbox("Would you like to:",
                                      "Final step",
                                      ["Finish", "Edit", "Cancel"])
            # if user is finished with adding new card
            if check == "Finish":
                # adds new card to original list
                monster_cards.update(new_card)
                # clears new card ist for next use
                new_card.clear()
                # breaks loop
                return
            elif check == "Edit":
                # if user wants to edit new card
                what_edit = easygui.buttonbox("What would you like "
                                              "to "
                                              "change?",
                                              "Back again",
                                              ["Name", "Stats"])

                if what_edit == "Name":
                    name_change = easygui.enterbox("What would you "
                                                   "like "
                                                   "to change this "
                                                   "monsters"
                                                   "name to?",
                                                   "Name Change")
                    # changes name
                    new_card[name_change] = new_card.pop(name)
                    name = name_change
                elif what_edit == "Stats":
                    # asks which stat
                    what_stat = easygui.buttonbox("Which stat of "
                                                  "this "
                                                  "monster would you "
                                                  "like to "
                                                  "change?",
                                                  "Which Stat?",
                                                  choices=list(new_card
                                                               [name]
                                                               .keys()))
                    # asks for change for that stat
                    change_stat = easygui.integerbox(f"Enter the new "
                                                     f"stat for "
                                                     f"{what_stat}",
                                                     upperbound=25,
                                                     lowerbound=1)
                    # changes stat
                    new_card[name][what_stat] = change_stat
            # if user wants to cancel adding new card
            elif check == "Cancel":
                # clears new card ist for next use and breaks loop
                new_card.clear()
                return


# Main routine

# Welcome message
easygui.msgbox("Welcome to the Monster card "
               "Dungeon\n~~~~~~~~~~~~~~~~~~~~~~~~~~", "Welcome Traveler")

# Menu/options
while True:
    # asks what the user wants to do
    option = easygui.buttonbox("Choose what you want to do, Traveler",
                               "Choose Wisely",
                               ["Add New Monster", "Search for a "
                                                   "Monster",
                                "Destroy a Monster", "Show all Monsters",
                                "Exit"])
    # when user chooses add card
    if option == "Add New Monster":
        add_card()
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
