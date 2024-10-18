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

value = {
    'quarters': 0.25,
    'dimes': 0.10,
    'nickles': 0.05,
    'pennies': 0.01
}

machine_is_on = True
money = 0


def check_coins():
    print(f"\nThat will cost: {MENU[choice]['cost']}\n")
    inserted_amount = 0
    for cent in value:
        inserted_amount += int(input(f"How many {cent}: ")) * value[cent]
        inserted_amount = round(inserted_amount, 3)
    if inserted_amount < MENU[choice]['cost']:
        print(f"\n{inserted_amount}. Sorry that's not enough money. Money refunded.\n")
        return 0
    else:
        if inserted_amount > MENU[choice]['cost']:
            change = inserted_amount - MENU[choice]['cost']
            print(f"\nHere is ${round(change, 3)} dollars in change.\n")
        return MENU[choice]['cost']


def check_ingredients(make_coffee):
    drink_ingredients = MENU[choice]['ingredients']
    refill_message = ""
    for ingredient in drink_ingredients.keys():
        if ingredient in resources:
            if make_coffee:
                resources[ingredient] -= drink_ingredients[ingredient]
            else:
                if resources[ingredient] - drink_ingredients[ingredient] < 0:
                    refill_message += f"Sorry there is not enough {ingredient}\n"

    if not len(refill_message) == 0:
        print(f"\n{refill_message}")
        return False
    else:
        return True


while machine_is_on:
    choice = input(f"What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        machine_is_on = False
    elif choice == "report":
        print(
         f"\nWater: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney: {money}\n")
    else:
        if check_ingredients(0):
            profit = check_coins()
            money += profit
            if profit > 0:
                check_ingredients(1)
