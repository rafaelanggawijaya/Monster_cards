"""Monster cards -Setup- v1b
This is just a setup which has the welcome screen and a list of the
pre-existing cards
Update: Trialling search and edit mode"""

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


# search and edit (simplified could change)

# searches for monster chosen
monster_search = easygui.enterbox("Please choose a monster:")
# prints monster stats for user to see
if monster_search in monster_cards:
    # prints name
    print(f"{monster_search}\nStats:\n")
    # prints stats
    for stat, value in monster_cards[monster_search].items():
        print(f"      {stat}: {value}")
    easygui.msgbox("The monster you have searched has its stats and name "
                   "printed"
                   "below")
else:
    # if name not valid
    easygui.msgbox(f"There is no card named {monster_search}\nPlease enter "
                   f"a valid name")
# edit section
while True:
    # ask what to change
    change = easygui.buttonbox("What would you like to change?", choices=[
        "Name", "Stat", "Finish"])
    # changes name
    if change == "Name":
        change_name = easygui.enterbox(f"Please enter the name you would "
                                       f"like to"
                                       f"change {monster_search} to:")
        monster_cards[change_name] = monster_cards.pop(monster_search)
        # prevents error when user wants to change name and stats
        monster_search = change_name
    # changes stat
    elif change == "Stat":
        # Ask which stat
        which_stat = easygui.buttonbox(f"Which stat would you like to "
                                       f"change", choices=list(
                                        monster_cards[monster_search].keys()))
        # user inputs new stat
        new_stat = easygui.integerbox(f"Please enter the new stat for "
                                      f"{which_stat}")
        # changes stat
        monster_cards[monster_search][which_stat] = new_stat
        print(monster_cards[monster_search])
    else:
        break
