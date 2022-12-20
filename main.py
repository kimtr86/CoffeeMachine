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
    "money": 0,

}

quarters = 0.25
dimes = 0.10
nickel = 0.05
pennies = 0.01


def check_espresso():
    if resources["water"] < MENU["espresso"]["ingredients"]["water"]:
        return f"Sorry there is not enough water."
    elif resources["coffee"] < MENU["espresso"]["ingredients"]["coffee"]:
        return f"Sorry there is not enough coffee."
    else:
        return f"yes espresso"


def check_latte():
    if resources["water"] < MENU["latte"]["ingredients"]["water"]:
        return f"Sorry there is not enough water."
    elif resources["milk"] < MENU["latte"]["ingredients"]["milk"]:
        return f"Sorry there is not enough milk."
    elif resources["coffee"] < MENU["latte"]["ingredients"]["coffee"]:
        return f"Sorry there is not enough coffee."
    else:
        return f"yes latte"


def check_cappuccino():
    if resources["water"] < MENU["cappuccino"]["ingredients"]["water"]:
        return f"Sorry there is not enough water."
    elif resources["milk"] < MENU["cappuccino"]["ingredients"]["milk"]:
        return f"Sorry there is not enough milk."
    elif resources["coffee"] < MENU["cappuccino"]["ingredients"]["coffee"]:
        return f"Sorry there is not enough coffee."
    else:
        return f"yes cappuccino"


def check_coins_espresso():
    print("Please insert coins")
    quarters_question = int(input(f"how many quarters?: "))
    dimes_question = int(input(f"how many dimes?: "))
    nickles_question = int(input(f"how many nickles?: "))
    pennies_question = int(input(f"how many pennies? "))
    coin_calculation = quarters * quarters_question + dimes * dimes_question + nickel * nickles_question + pennies * pennies_question

    if coin_calculation >= MENU["espresso"]["cost"]:

        espresso_calc = coin_calculation - MENU["espresso"]["cost"]
        print(f"Here is ${round(espresso_calc, 2)} in change.")
        print(f"Here is your espresso ☕️. Enjoy!")

    else:
        print(f"Sorry that's not enough money. Money refunded.")


def check_coins_latte():
    print("Please insert coins")
    quarters_question = int(input(f"how many quarters?: "))
    dimes_question = int(input(f"how many dimes?: "))
    nickles_question = int(input(f"how many nickles?: "))
    pennies_question = int(input(f"how many pennies? "))
    coin_calculation = quarters * quarters_question + dimes * dimes_question + nickel * nickles_question + pennies * pennies_question

    if coin_calculation >= MENU["latte"]["cost"]:

        latte_calc = coin_calculation - MENU["latte"]["cost"]
        print(f"Here is ${round(latte_calc, 2)} in change.")
        print(f"Here is your latte ☕️. Enjoy!")

    else:
        print(f"Sorry that's not enough money. Money refunded.")


def check_coins_cappuccino():
    print("Please insert coins")
    quarters_question = int(input(f"how many quarters?: "))
    dimes_question = int(input(f"how many dimes?: "))
    nickles_question = int(input(f"how many nickles?: "))
    pennies_question = int(input(f"how many pennies? "))
    coin_calculation = quarters * quarters_question + dimes * dimes_question + nickel * nickles_question + pennies * pennies_question

    if coin_calculation >= MENU["cappuccino"]["cost"]:

        cappuccino_calc = coin_calculation - MENU["cappuccino"]["cost"]
        print(f"Here is ${round(cappuccino_calc, 2)} in change.")
        print(f"Here is your cappuccino ☕️. Enjoy!")

    else:
        print(f"Sorry that's not enough money. Money refunded.")


def report(resources_information):
    water = resources_information["water"]
    milk = resources_information["milk"]
    coffee = resources_information["coffee"]
    money = resources_information["money"]
    return f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}"


def machine():
    # TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):

    coffee_machine_continue = True

    while coffee_machine_continue:

        question = input("What would you like? (espresso/latte/cappuccino): ").lower()

        # TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.

        if question == "off":
            coffee_machine_continue = False

        # TODO: 3. Print report.

        elif question == "report":
            print(report(resources))

        # TODO: 4. Check resources sufficient?

        elif question == "espresso":
            if check_espresso() == "yes espresso":
                check_coins_espresso()
                new_water_espresso = resources["water"] - MENU["espresso"]["ingredients"]["water"]
                new_coffee_espresso = resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"]
                resources["water"] = new_water_espresso
                resources["coffee"] = new_coffee_espresso
            else:
                print(check_espresso())

        elif question == "latte":
            if check_latte() == "yes latte":
                check_coins_latte()
                new_water_latte = resources["water"] - MENU["latte"]["ingredients"]["water"]
                new_milk_latte = resources["milk"] - MENU["latte"]["ingredients"]["milk"]
                new_coffee_latte = resources["coffee"] - MENU["latte"]["ingredients"]["coffee"]
                resources["water"] = new_water_latte
                resources["milk"] = new_coffee_latte
                resources["coffee"] = new_coffee_latte
            else:
                print(check_latte())

        elif question == "cappuccino":
            if check_cappuccino() == "yes cappuccino":
                check_coins_cappuccino()
                new_water_cappuccino = resources["water"] - MENU["cappuccino"]["ingredients"]["water"]
                new_milk_cappuccino = resources["milk"] - MENU["cappuccino"]["ingredients"]["milk"]
                new_coffee_cappuccino = resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"]
                resources["water"] = new_water_cappuccino
                resources["milk"] = new_coffee_cappuccino
                resources["coffee"] = new_coffee_cappuccino
            else:
                print(check_cappuccino())


machine()
