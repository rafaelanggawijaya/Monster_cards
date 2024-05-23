"""Monster cards -Setup- v3b
This is just a setup which has the welcome screen and a list of the
pre-existing cards
Update: Trialling search and edit (simple list)"""

import easygui

# list of cards
monster_cards = [["Stoneling", 7, 1, 25, 15, ],
                 ["Vexscream", 1, 6, 21, 19],
                 ["Dawnmirage", 5, 15, 18, 22],
                 ["Blazegolem", 15,  20, 23, 6],
                 ["Websnake", 7, 15, 10, 5],
                 ["Moldvine", 21, 18, 14, 5],
                 ["Vortexwing", 19, 13, 19, 2],
                 ["Rotthing", 16, 7, 4, 12],
                 ["Froststep", 14, 14, 17, 4],
                 ["Wispghoul", 17, 19, 3, 2]]

# Main routine

# Welcome message
easygui.msgbox("Welcome to the Monster card "
               "Dungeon\n~~~~~~~~~~~~~~~~~~~~~~~~~~", "Welcome Traveler")


# edit/search

# asks for user for monster they want to search
monster_search = easygui.enterbox("Please choose a monster:")
# for if the card asked for is not in list
found = 0
# keeps in check which card is which
num_card = 0
# searches for monster chosen
for card in monster_cards:
    if monster_search in monster_cards[num_card][0]:
        # prints name
        print(f"{monster_cards[num_card][0]}\nStats:\n")
        # prints stats
        print(f"    Strength: {monster_cards[num_card][1]}\n    Speed: "
              f"{monster_cards[num_card][2]}\n    Stealth: "
              f"{monster_cards[num_card][3]}\n    Cunning: "
              f"{monster_cards[num_card][4]}\n")

        found = 1
        break
    num_card += 1
if found == 0:
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
                                       f"like to "
                                       f"change {monster_search} to:")
        # changes name
        monster_cards[num_card][0] = change_name
        print(monster_cards[num_card])
    # changes stat
    elif change == "Stat":
        # Ask which stat
        which_stat = easygui.buttonbox(f"Which stat would you like to "
                                       f"change",
                                       choices=["Strength", "Speed",
                                                "Stealth", "Speed"])
        # user inputs new stat
        new_stat = easygui.integerbox(f"Please enter the new stat for "
                                      f"{which_stat}")
        # tells list what stat to change
        if which_stat == "Strength":
            which_stat = 1
        elif which_stat == "Speed":
            which_stat = 2
        elif which_stat == "Stealth":
            which_stat = 3
        elif which_stat == "Speed":
            which_stat = 4
        # changes stat
        monster_cards[num_card][which_stat] = new_stat
        print(monster_cards[num_card])
    else:
        # ends loop
        break
