# 1. Name:
#      Nathan Yochim
# 2. Assignment Name:
#      Lab 04: Monopoly
# 3. Assignment Description:
#      This program determines if you can build a hotel on Pennsylvania Avenue in Monopoly.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part was determining what order to make the decisions in.
# 5. How long did it take for you to complete the assignment?
#      It took me about 3 hours to complete the assignment.

# Program introduction.
print("This is the Monopoly Program.")
print("Use this program to determine if you can build a hotel on Pennsylvania Avenue.")

# Find if user owns all green properties.
own_green = input("Do you own all the green properties? (y/n): ")
# If user does not own all green properties, they cannot build a hotel.
if own_green.lower() != 'y':
    print("You cannot purchase a hotel until you own all the properties of a given color group.")
else:
    # Find how many houses are on Pennsylvania Avenue.
    pennsylvania_houses = int(input("What is on Pennsylvania Avenue? (0:nothing, 1:one house, ... 5:a hotel): "))
    # If variable is outside of permitted range, print error message.
    if pennsylvania_houses < 0 or pennsylvania_houses > 5:
        print("Error: Invalid number of houses on Pennsylvania Avenue.")
    # If there is already a hotel on Pennsylvania Avenue, user cannot build another one.
    elif pennsylvania_houses == 5:    
        print("You cannot purchase a hotel if the property already has one.")
    else:
        # Find how many houses are on North Carolina Avenue.
        north_carolina_houses = int(input("What is on North Carolina Avenue? (0:nothing, 1:one house, ... 5:a hotel): "))
        # If variable is outside of permitted range, print error message.
        if north_carolina_houses < 0 or north_carolina_houses > 5:
            print("Error: Invalid number of houses on North Carolina Avenue.")
        # If there is a hotel on North Carolina Avenue, user can swap it with Pennsylvania's 4 houses.
        elif north_carolina_houses == 5:
            print("Swap North Carolina's hotel with Pennsylvania's 4 houses.")
        else:
            # Find how many houses are on Pacific Avenue.
            pacific_houses = int(input("What is on Pacific Avenue? (0:nothing, 1:one house, ... 5:a hotel): "))
            # If variable is outside of permitted range, print error message.
            if pacific_houses < 0 or pacific_houses > 5:
                print("Error: Invalid number of houses on Pacific Avenue.")
            # If there is a hotel on Pacific Avenue, user can swap it with Pennsylvania's 4 houses.
            elif pacific_houses == 5:
                print("Swap Pacific's hotel with Pennsylvania's 4 houses.")
            else:
                # Check how many hotels are available to buy.
                available_hotels = int(input("How many hotels are there to purchase?: "))
                # If there are less than 1 hotel available, user cannot build a hotel.
                if available_hotels < 1:
                    print("There are not enough hotels available for purchase at this time.")
                else:
                    # Check how much money the user has.
                    cash = int(input("How much cash do you have to spend?: "))
                    # If user has less than $200, they cannot build a hotel.
                    if cash < 200:
                        print("You do not have sufficient funds to purchase a hotel at this time.")
                    else:
                        # Check how many houses are available to buy.
                        available_houses = int(input("How many houses are there to purchase?: "))
                        # If there are not enough houses to even out the properties, user cannot build a hotel.
                        if available_houses < (4-pennsylvania_houses) + (4-north_carolina_houses) + (4-pacific_houses):
                            print("There are not enough houses available for purchase at this time.")
                        else:
                            # Add up the price of the hotel and the houses needed to even out the properties.
                            price = 200 + (4 - pennsylvania_houses) * 200 + (4 - north_carolina_houses) * 200 + (4 - pacific_houses) * 200
                            # If user does not have enough money to cover the price, they cannot build a hotel.
                            if cash < price:
                                print("You do not have sufficient funds to purchase a hotel at this time.")
                            else:
                                # Print the total price and tell the user how to distribute their hotel and houses.
                                print(f"This will cost ${price}.")
                                print(f"        Purchase 1 hotel and {(4 - pennsylvania_houses) + (4 - north_carolina_houses) + (4 - pacific_houses)} house(s).")
                                print(f"        Put 1 hotel on Pennsylvania and return any houses to the bank.")
                                if north_carolina_houses < 4:
                                    print(f"        Put {4 - north_carolina_houses} house(s) on North Carolina.")
                                if pacific_houses < 4:
                                    print(f"        Put {4 - pacific_houses} house(s) on Pacific.")