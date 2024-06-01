"""Monster Card -Print_card function
This function prints all card names and stats and used to shorten code """


# print_card
def print_card(dictionary, identifier):
    # prints name
    print(f"{identifier}")
    # prints ~ line for aesthetics
    print("~" * len(identifier))
    print("Stats:")
    # prints stats
    for stat, value in dictionary[identifier].items():
        print(f"      {stat}: {value}")
