"""Monster cards -Search and edit- v2
This the search engine which allows the user to search for a monster to view
change and delete
Update: I added a list which can hold edits and if user wants to cancel
edite it can be deleted so changes never occurred"""

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
                                "Show all Monsters",
                                "Exit"])
    # when user chooses add card
    if option == "Add New Monster":
        print("Add New monster")
    # when user chooses search/edit
    elif option == "Search for a Monster":
        # search for a monster/edit

        # holds edits
        edited_card = {"name": {"Strength": 0, "Speed": 0, "Stealth": 0,
                                "Cunning": 0}}
        while True:
            monster_search = easygui.enterbox("Please choose a monster, "
                                              "Traveler:", "Searching for "
                                                           "Monster")
            # prints monster stats for user to see
            if monster_search in monster_cards:
                # prints name
                print(f"{monster_search}\nStats:\n")
                # prints stats
                for stat, value in monster_cards[monster_search].items():
                    print(f"      {stat}: {value}")
                # adds name for edit dictionary
                edited_card[monster_search] = edited_card.pop("name")
                easygui.msgbox(
                    "The monster you have searched has its stats and name "
                    "printed"
                    "below")
                while True:
                    # asks user what they will do to searched monster
                    do_what = easygui.buttonbox("What would you like to do, "
                                                "Traveler",
                                                "What are you gong "
                                                "to do?",
                                                choices=["Finish", "Edit",
                                                         "Delete"])
                    # if user is finished/ just wanted to view the monster
                    if do_what == "Finish":
                        break
                    # if user wants to edit the monster
                    elif do_what == "Edit":

                        # edit section
                        while True:
                            # ask what to change
                            change = easygui.buttonbox(
                                "What would you like to "
                                "change?",
                                choices=[
                                    "Name", "Stat", "Finish"])
                            # changes name
                            if change == "Name":
                                change_name = easygui.enterbox(
                                    f"Please enter the name you would "
                                    f"like to"
                                    f"change {monster_search} to:")
                                monster_cards[change_name] = monster_cards.pop(
                                    monster_search)
                                # prevents error when user wants to change name
                                # and stats
                                monster_search = change_name
                            # changes stat
                            elif change == "Stat":
                                # Ask which stat
                                which_stat = easygui.buttonbox(
                                    f"Which stat would "
                                    f"you like to "
                                    f"change", choices=list(
                                        monster_cards
                                        [monster_search]
                                        .keys()))
                                # user inputs new stat
                                new_stat = easygui.integerbox(
                                    f"Please enter the new "
                                    f"stat for "
                                    f"{which_stat}")
                                # changes stat
                                monster_cards[monster_search][
                                    which_stat] = new_stat
                            else:
                                break
                    # when user chooses delete card
                    elif do_what == "Delete":
                        # deletes card
                        del monster_cards[monster_search]
                        easygui.msgbox(
                            f"The monster, {monster_search} has been "
                            f"removed for the dungeon.")
                        break
                break
            else:
                # if name not valid
                easygui.msgbox(
                    f"There is no Monster named {monster_search}\nPlease "
                    f"enter "
                    f"a valid name", "Error")
    # when user chooses show all cards
    elif option == "Show all Monsters":
        print("Show all Monsters")
    # when user wants to exit program
    else:
        print("Exit")
