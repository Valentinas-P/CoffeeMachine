def make_coffee(water, coffee, milk, money):
    if resources["Water"] < water or resources["Coffee"] < coffee or resources["Milk"] < milk:
        print("Not enough resources to make coffee")
    else:
        print("Please insert coins.")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))
        overall_count = ((quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01))
        if overall_count < money:
            print("Not enough money inserted")
        else:
            overall_to_give_back = overall_count - money
            print(f"Here is ${overall_to_give_back:.2f} in change")
            print("Here is your latte Enjoy!")
            resources["Water"] -= water
            resources["Coffee"] -= coffee
            resources["Milk"] -= milk
            resources["Money"] += money


resources = {
    "Water": 300,
    "Milk": 200,
    "Coffee": 100,
    "Money": 0,
}

game_is_on = True

while game_is_on:
    option = input("What would you like? (espresso/latte/cappuccino: ").lower()
    if option == "report":
        for i, x in resources.items():
            print(f"{i}: {x}")
    elif option == "latte":
        make_coffee(200, 24, 150, 2.50)
    elif option == "espresso":
        make_coffee(50, 18, 0, 1.50)
    elif option == "cappuccino":
        make_coffee(250, 24, 100, 2.80)
    elif option == "off":
        break
