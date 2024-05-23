"""Monster cards -Setup- v2c
This is just a setup which has the welcome screen and a list of the
pre-existing cards
Update: Trialling the add new card (lists)"""

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


# Add card

# hold new card name and stats
new_card = []
new_strength_store = ["Strength"]
new_speed_store = ["Speed"]
new_stealth_store = ["Stealth"]
new_cunning_store = ["Cunning"]

# asks and adds new monster name
new_name = easygui.enterbox("Please enter the Monster's name")
new_card.append(new_name)
# asks and adds new strength stat
new_strength = easygui.integerbox("Please enter the strength stat for this "
                                  "card")
new_strength_store.append(new_strength)
# asks and adds speed stat
new_speed = easygui.integerbox("Please enter the speed stat for this card")
new_speed_store.append(new_speed)
# asks and adds stealth stat
new_stealth = easygui.integerbox("Please enter the stealth stat for this card")
new_stealth_store.append(new_stealth)
# asks and adds cunning stat
new_cunning = easygui.integerbox("Please enter the cunning stat for this card")
new_cunning_store.append(new_cunning)

# adds stats to the new_cards list (which will be added together in
# monster_cards
new_card.append(new_strength_store)
new_card.append(new_speed_store)
new_card.append(new_stealth_store)
new_card.append(new_cunning_store)
# adds new card to list of cards
monster_cards.append(new_card)

# testing
print(new_card)
print(monster_cards[10])
