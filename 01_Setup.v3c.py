"""Monster cards -Setup- v3c
This is just a setup which has the welcome screen and a list of the
pre-existing cards
Update: Trialling add card (simple list)"""

import easygui

# list of cards
monster_cards = [["Stoneling", 7, 1, 25, 15],
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


# Add card

# asks and adds new monster name
new_name = easygui.integerbox("Please enter the Monster's name")
monster_cards.append(list(new_name))
# asks and adds new strength stat
new_strength = easygui.integerbox("Please enter the strength stat for this "
                                  "card")
monster_cards[11].append(new_strength)
# asks and adds speed stat
new_speed = easygui.integerbox("Please enter the speed stat for this card")
monster_cards[11].append(new_speed)
# asks and adds stealth stat
new_stealth = easygui.integerbox("Please enter the stealth stat for this card")
monster_cards[11].append(new_stealth)
# asks and adds cunning stat
new_cunning = easygui.integerbox("Please enter the cunning stat for this card")
monster_cards[11].append(new_cunning)

