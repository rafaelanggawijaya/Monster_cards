"""Monster cards -Setup-
This is just a setup which has the welcome screen and a list of the
pre-existing cards
Update: Wanted to trial also a different way to use a list"""

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
# # prints everything out
# for card in monster_cards:
#     # prints name
#     print(f"{card[0]}\nStats:")
#     # prints stats
#     print(f"    Strength: {card[1]}\n    Speed: {card[2]}\n    Stealth: "
#           f"{card[3]}\n    Cunning: {card[4]}")


# edit
