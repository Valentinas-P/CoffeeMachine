MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

IS_GAME_OVER = False
MONEY = 0.0

def get_total_amount():
    """A function to get the total amount of money entered"""
    # Ask's the user to insert coins
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    quarters *= 0.25
    dimes *= 0.10
    nickles *= 0.05
    pennies *= 0.01

    return quarters + dimes + nickles + pennies


def make_espresso(resources):
    """A function to make a espresso coffee"""
    # Define the required ingredients and the cost
    espresso_water = MENU['espresso']['ingredients']['water']
    espresso_grounds = MENU['espresso']['ingredients']['coffee']
    espresso_cost = MENU['espresso']['cost']
    required_amount = 2.20

    # Check if there are enough resources to make a espresso
    if (espresso_water <= resources["water"]
        and espresso_grounds <= resources["coffee"]):
        
        # Calculate the total money the user enter it
        total = get_total_amount()
        print(f"{total:.02f}")

        # Check if user didn't insert too much money for the coffee
        if total > required_amount:
            print("You inserted too much money. Money refunded.")
            print(f"Your change is: £{total:.02f}")
        else:
            # Check if there are enough money the user entered for the coffee
            if total >= espresso_cost:

                # If there are enough resources to make a espresso
                print("I'm making for you espresso coffee")
                resources["water"] -= espresso_water
                resources["coffee"] -= espresso_grounds
                print(f"Your change is: £{total - espresso_cost:.02f}")

                # Add the cost of the espresso to the machine's money
                global MONEY
                MONEY += 1.50
            else:
                print("Sorry that's not enough money. Money refunded.")
    else:
        print("Sorry, there are not enough ingredients to make a espresso.")


def make_latte(resources):
    """A function to make a latte coffee"""
    # Define the required ingredients
    latte_water = MENU['latte']['ingredients']['water']
    latte_grounds = MENU['latte']['ingredients']['coffee']
    latte_milk = MENU['latte']['ingredients']['milk']
    latte_cost = MENU['latte']['cost']
    required_amount = 3.20

    # Check if there are enough resources to make a latte
    if (latte_water <= resources["water"]
        and latte_grounds <= resources["coffee"]
        and latte_milk <= resources["milk"]):

        total = get_total_amount()
        print(f"{total:.02f}")

        if total > required_amount:
            print("You inserted too much money. Money refunded.")
            print(f"Your change is: £{total:.02f}")
        else:
            if total >= latte_cost:
                # If there are enough resources, make the latte
                print("I'm making for you latte coffee")
                resources["water"] -= latte_water
                resources["coffee"] -= latte_grounds
                resources["milk"] -= latte_milk
                print(f"Your change is: £{total - latte_cost:.02f}")

                # Add the cost of the latte to the machine's money
                global MONEY
                MONEY += 2.50
            else:
                print("Sorry that's not enough money. Money refunded.")
    else:
        print("Sorry, there are not enough ingredients to make a latte.")


def make_cappucino(resources):
    """A function to make a cappucino coffee"""
    # Define the required ingredients
    cappucino_water = MENU['cappuccino']['ingredients']['water']
    cappucino_grounds = MENU['cappuccino']['ingredients']['coffee']
    cappucino_milk = MENU['cappuccino']['ingredients']['milk']
    cappucino_cost = MENU['cappuccino']['cost']
    required_amount = 4.00

    # Check if there are enough resources to make a cappucino
    if (cappucino_water <= resources["water"]
        and cappucino_grounds <= resources["coffee"]
        and cappucino_milk <= resources["milk"]):

        # Calculate the total money the user enter it
        total = get_total_amount()
        print(f"{total:.02f}")

        # Check if user didn't insert too much money for the coffee
        if total > required_amount:
            print("You inserted too much money. Money refunded.")
            print(f"Your change is: £{total:.02f}")
        else:
             # Check if there are enough money the user entered for the coffee
            if total >= cappucino_cost:
                # If there are enough resources, make the cappucino
                print("I'm making for you cappucino coffee")
                resources["water"] -= cappucino_water
                resources["coffee"] -= cappucino_grounds
                resources["milk"] -= cappucino_milk
                print(f"Your change is: £{total - cappucino_cost:.02f}")

                # Add the cost of the cappucino to the machine's money
                global MONEY
                MONEY += 3.00
            else:
                print("Sorry that's not enough money. Money refunded.")
    else:
        print("Sorry, there are not enough ingredients to make a cappucino.")

while not IS_GAME_OVER:
    user_requirements = input("What would you like? (espresso/latte/cappucino): ").lower()
    if user_requirements == "espresso":
        make_espresso(resources)
    elif user_requirements == "latte":
        make_latte(resources)
    elif user_requirements == "cappucino":
        make_cappucino(resources)
    elif user_requirements == "report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g\nMoney: £{MONEY:.02f}")
    elif user_requirements == "off":
        print("Shutting down...")
        break
    else:
        print("Please enter your coffee again.")
