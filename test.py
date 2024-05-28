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
def add_card():
    # add card

    new_card = {}
    while True:
        # asks for name
        name = easygui.enterbox(
            "Enter the name of the Monster you would like to add")
        # if user wants to cancel
        if name is None:
            return
        # makes a dictionary for that cards name
        new_card[name] = {"Strength": 0, "Speed": 0, "Stealth": 0,
                          "Cunning": 0}
        for stat_name, stats in new_card[name].items():
            new_stat = easygui.integerbox(
                f"Please enter the {stat_name} "
                f"for this monster", upperbound=25, lowerbound=1)
        print(name)
        print(new_card[name])

add_card()