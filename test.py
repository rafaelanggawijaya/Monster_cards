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
num_card = 0
for card in monster_cards:
    print(monster_cards[num_card][0])
    num_card += 1
# Welcome message
easygui.msgbox("Welcome to the Monster card "
               "Dungeon\n~~~~~~~~~~~~~~~~~~~~~~~~~~", "Welcome Traveler")

# prints everything out
# for card in monster_cards:
#     # prints name
#     print(f"{card[0]}\nStats:")
#     # prints stat
#     for stat in card:
#         # stops error
#         if stat != card[0]:
#             print(f"    {stat[0]}: {stat[1]}")
#     print()

# search and edit
# searches for monster chosen
monster_search = easygui.enterbox("Please choose a monster:")
# keeps in check which card is which
num_card = 0
for card in monster_cards[num_card][0]:
    if monster_search in monster_cards[num_card][0]:
            # prints name
        print(f"{monster_cards[num_card][0]}\nStats:\n")
        # prints stats
        for stat in monster_cards[num_card]:
            # stops error
            if stat != monster_cards[num_card][0]:
                print(f"    {stat[0]}: {stat[1]}")
    num_card += 1
