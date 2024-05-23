"""Monster cards -Setup- v2b
This is just a setup which has the welcome screen and a list of the
pre-existing cards
Update: Trialling the search and edit mode (lists)"""

import easygui

# list of cards
monster_cards = [["Stoneling", ["Strength", 7], ["Speed", 1], ["Stealth", 25],
                  ["Cunning", 15]],
                 ["Vexscream", ["Strength", 1], ["Speed", 6], ["Stealth", 21],
                  ["Cunning", 19]],
                 ["Dawnmirage", ["Strength", 5], ["Speed", 15], ["Stealth",
                                                                 18],
                  ["Cunning", 22]],
                 ["Blazegolem", ["Strength", 15], ["Speed", 20], ["Stealth",
                                                                  23],
                  ["Cunning", 6]],
                 ["Websnake", ["Strength", 7], ["Speed", 15], ["Stealth", 10],
                  ["Cunning", 5]],
                 ["Moldvine", ["Strength", 21], ["Speed", 18], ["Stealth", 14],
                  ["Cunning", 5]],
                 ["Vortexwing", ["Strength", 19], ["Speed", 13], ["Stealth",
                                                                  19],
                  ["Cunning", 2]],
                 ["Rotthing", ["Strength", 16], ["Speed", 7], ["Stealth", 4],
                  ["Cunning", 12]],
                 ["Froststep", ["Strength", 14], ["Speed", 14], ["Stealth",
                                                                 17],
                  ["Cunning", 4]],
                 ["Wispghoul", ["Strength", 17], ["Speed", 19], ["Stealth", 3],
                  ["Cunning", 2]]]

# Main routine

# Welcome message
easygui.msgbox("Welcome to the Monster card "
               "Dungeon\n~~~~~~~~~~~~~~~~~~~~~~~~~~", "Welcome Traveler")


# search and edit
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
        for stat in monster_cards[num_card]:
            # stops error
            if stat != monster_cards[num_card][0]:
                print(f"    {stat[0]}: {stat[1]}")

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
                                       choices=[monster_cards[num_card][1][
                                                    0], monster_cards[
                                                    num_card][2][
                                                    0], monster_cards[
                                                    num_card][3][
                                                    0], monster_cards[
                                                    num_card][4][
                                                    0]])
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
        monster_cards[num_card][1][which_stat] = new_stat
        print(monster_cards[num_card])
    else:
        break
