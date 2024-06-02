"""Monster cards  By Rafael Anggawijaya
A catalogue containing monster
cards which can be edited, deleted and added, also the whole list can be
printed out
"""

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

# add card
def add_card():
    # add card

    new_card = {}
    while True:
        # asks for name
        name = easygui.enterbox(
            "Enter the name of the Monster you would like to add",
            "Name of "
            "the "
            "Monster")
        # if user wants to cancel
        if name is None:
            return
        # makes a dictionary for that cards name
        new_card[name] = {"Strength": 0, "Speed": 0, "Stealth": 0,
                          "Cunning": 0}
        for stat_name, stats in new_card[name].items():
            new_stat = easygui.integerbox(
                f"Please enter the {stat_name} stat"
                f"for this monster", upperbound=25, lowerbound=1,
                title=f"{stat_name} Stat")
            if new_stat is None:
                new_card.clear()
                return
            new_card[name][stat_name] = new_stat
        while True:
            print_card(new_card, name)
            easygui.msgbox(
                "The monster you have added has its stats and name "
                "printed "
                "below", "Look below")
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
                                                   "monster's "
                                                   "name to?",
                                                   "Name Change")
                    if name_change is None:
                        easygui.msgbox("No changes was added",
                                       "Edited cancelled")
                    else:
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
                                                     lowerbound=1,
                                                     title="Stat change")
                    if change_stat is None:
                        easygui.msgbox("No changes was made",
                                       "Edited cancelled")
                    else:
                        # changes stat
                        new_card[name][what_stat] = change_stat
            # if user wants to cancel adding new card
            elif check == "Cancel":
                # clears new card ist for next use and breaks loop
                new_card.clear()
                return


# search and edit and delete
def search_edit_delete():
    # search for a monster/edit

    # holds edits
    edited_card = {}
    while True:
        monster_choices = list(monster_cards.keys())
        monster_search = easygui.choicebox("Please select the monster you "
                                           "would like to view", "Choose "
                                                                 "Your "
                                                                 "Monster",
                                           choices=monster_choices)
        # if cancel is made
        if monster_search is None:
            break
        # for later use if name is changed which helps add back changes
        monster_change = monster_search
        # prints monster stats for user to see

        # prints name
        print(f"{monster_search}")
        # prints ~ line for aesthetics
        print("~" * len(monster_search))
        print("Stats:")
        # prints stats
        for stats, value in monster_cards[monster_search].items():
            print(f"      {stats}: {value}")
            # adds the entire dictionary under the monster name in
            # edited_card
            edited_card[monster_search] = monster_cards[monster_search]
        easygui.msgbox(
            "The monster you have searched has its stats and name "
            "printed "
            "below", "Look below")
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
                # Check if edited_card is not empty
                if edited_card:
                    # Retrieve the only key from edited_card,
                    # which should be the monster's name
                    new_key = list(edited_card.keys())[0]

                    # Update monster_cards dictionary at the
                    # original position
                    monster_cards[new_key] = edited_card[new_key]

                    # Remove the old entry if the name has changed
                    if new_key != monster_change:
                        del monster_cards[monster_change]

                    # Clears edited_card dictionary for next use
                    edited_card.clear()
                return
            elif do_what == "Edit":

                # edit section
                while True:
                    # ask what to change
                    change = easygui.buttonbox(
                        "What would you like to "
                        "change?", "Editing",
                        choices=[
                            "Name", "Stat", "Finish"])
                    # changes name
                    if change == "Name":
                        change_name = easygui.enterbox(
                            f"Please enter the name you would "
                            f"like to "
                            f"change {monster_search} to:", "Name Change")
                        edited_card[change_name] = edited_card.pop(
                            monster_search)
                        # prevents error when user wants to change name
                        # and stats
                        monster_search = change_name
                        # shows changes
                        print("Changes made:\n")
                        print_card(edited_card, monster_search)
                        easygui.msgbox(f"Changes to {monster_search} has "
                                       f"been printed below", "Look down")
                    # changes stat
                    elif change == "Stat":
                        # Ask which stat
                        which_stat = easygui.buttonbox(
                            f"Which stat would "
                            f"you like to "
                            f"change", "Which stat to change?",
                            choices=list(
                                edited_card
                                [monster_search]
                                .keys()))
                        # user inputs new stat
                        new_stat = easygui.integerbox(
                            f"Please enter the new "
                            f"stat for "
                            f"{which_stat}", "Stat Change")
                        # changes stat
                        edited_card[monster_search][
                            which_stat] = new_stat
                        # shows changes
                        print("Changes made:\n")
                        print_card(edited_card, monster_search)
                        easygui.msgbox(f"Changes to {monster_search} has "
                                       f"been printed below", "Look down")
                    else:
                        if edited_card:
                            # checks if user wants to keep edits
                            confirm_edits = (easygui.
                                             choicebox("Would you "
                                                       "like to keep "
                                                       "changes?",
                                                       title="Confirmation",
                                                       choices=["Confirm",
                                                                "Cancel"]))
                            if confirm_edits == "Cancel":
                                edited_card.clear()
                                easygui.msgbox("Changes have been "
                                               "reverted",
                                               "Cancellation")

                        break

            # when user chooses delete card
            elif do_what == "Delete":
                # making sure user wants to delete the card
                confirm = easygui.buttonbox("Are you sure you want to "
                                            "delete this monster?",
                                            "Confirm",
                                            ["Confirm", "Cancel"])
                # When confirmed
                if confirm == "Confirm":
                    # deletes card
                    del monster_cards[monster_change]
                    easygui.msgbox(
                        f"The monster, {monster_search} has been "
                        f"removed for the dungeon.", "Monster removed")
                    return
                # When cancelled
                else:
                    easygui.msgbox("Deletion was Cancelled",
                                   "Cancelled")


# print_card
def print_card(dictionary, identifier):
    # prints name
    print(f"{identifier}")
    # prints ~ line for aesthetics
    print("~" * len(identifier))
    print("Stats:")
    # prints stats
    for stats, value in dictionary[identifier].items():
        print(f"      {stats}: {value}")
    print()


# Main routine

# Welcome message
easygui.msgbox("Welcome to the Monster card "
               "Dungeon\n~~~~~~~~~~~~~~~~~~~~~~~~~~", "Welcome Traveler")
# Menu/options
while True:
    # asks what the user wants to do
    option = easygui.buttonbox("Choose what you want to do, Traveler",
                               "Choose Wisely",
                               ["Instructions", "Add New Monster",
                                "Search "
                                "for a Monster",
                                "Show all Monsters",
                                "Exit"])
    # When User picks Instructions
    if option == "Instructions":
        easygui.msgbox(
            "Instructions:\n"
            "----------------------------------------------------------"
            "----------------------------------------\nThis how you use The "
            "Monster"
            "Dungeon, "
            "Traveler.\nYou have a few options\n\n"
            "1.Add New Monster (Lets you add cards)\nYou first add their name "
            "and\n"
            "their stats for each Strength, Speed, Stealth and Cunning which "
            "each\n"
            "have to be 1-25 including in value. You can edit it before "
            "confirming\n"
            "the addition of this new monster\n\n"
            "2.Search for a Monster (Lets you view, Edit or Delete existing "
            "cards)\nYou can press edit to change their name or stats "
            "remember to\n"
            "enter valid stats and press finish to finish edits and confirm "
            "or\n"
            "cancel if you want to keep changes or not. You can also delete "
            "the\n"
            "card by pressing delete and you can also confirm or cancel. Press"
            "Finish if you just want to view the card\n\n"
            "3.Show all Monsters (Prints all Monsters)\n\n"
            "4.Exit (Exits Program)\n\nHopefully this shall help you in your "
            "Journey"
            "through the Monster Dungeon, Good Luck and Have "
            "fun!\n"
            "-----------------------------------------------------------------"
            "-------"
            "--------------------------",
            "Instructions, For the Monster Dungeon")
    # when user chooses add card
    elif option == "Add New Monster":
        add_card()
    # when user chooses search/edit
    elif option == "Search for a Monster":
        search_edit_delete()
    # when user chooses show all cards
    elif option == "Show all Monsters":
        print("Monsters in the dungeon\n\n")
        # prints out all cards
        for card, stat in monster_cards.items():
            print_card(monster_cards, card)
        easygui.msgbox("All cards in the dungeon have been printed below",
                       "Look down")
    # when user wants to exit program
    else:
        break
