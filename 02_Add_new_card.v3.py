"""Monster cards -add new card- v3
This component allows the user to add new cards to the card list
Update: added upperbound and lower bound for stats change and used a while
loop to make code more efficient when asking for stats  """

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
                               ["Add New Monster", "Search for a "
                                                   "Monster",
                                "Destroy a Monster", "Show all Monsters",
                                "Exit"])
    # when user chooses add card
    if option == "Add New Monster":
        # add card

        # stop reset
        stop = True

        new_card = {}
        while stop is True:
            # asks for name
            name = easygui.enterbox(
                "Enter the name of the Monster you would like to add")
            # if user wants to cancel
            if name is None:
                break
            # makes a dictionary for that cards name
            new_card[name] = {}

            # ask user for strength stat and adds strength stats
            strength = easygui.enterbox(
                "Please enter the strength stat for this card")
            # if user wants to cancel
            if strength is None:
                break
            new_card[name]["Strength"] = strength

            # ask user for speed stat and adds speed stats
            speed = easygui.enterbox("Please enter the speed stat for this "
                                     "card")
            # if user wants to cancel
            if speed is None:
                break
            new_card[name]["Speed"] = speed

            # ask user for stealth stat and adds stealth stats
            stealth = easygui.enterbox(
                "Please enter the stealth stat for this card")
            # if user wants to cancel
            if stealth is None:
                break
            new_card[name]["Stealth"] = stealth

            # ask user for Cunning stat and adds cunning stats
            cunning = easygui.enterbox(
                "Please enter the Cunning stat for this card")
            # if user wants to cancel
            if cunning is None:
                break
            new_card[name]["Cunning"] = cunning
            # prints name
            print(f"{name}\nStats:\n")
            # prints stats
            for stat, value in new_card[name].items():
                print(f"      {stat}: {value}")
            easygui.msgbox(
                "The monster you have searched has its stats and name "
                "printed"
                "below")
            # checks if user is done or wants to make new edits or wants to
            # cancel
            while True:
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
                    stop = False
                    break
                elif "Edit":
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
                                                         f"{what_stat}")
                        # changes stat
                        new_card[name][what_stat] = change_stat
                # if user wants to cancel adding new card
                else:
                    # clears new card ist for next use and breaks loop
                    new_card.clear()
                    stop = False
                    break
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
