from data import MENU
from data import resources

#  added logic for lack of money to customer_choice(),
#  so it doesn't say enjoy something you didn't get


def customer_choice(on):
    while on:
        choice = input("What would you like? (espresso/latte/cappuccino)")
        if choice == "espresso":
            if res_check(choice):
                print(f"Enjoy your {choice}")
                return True
            else:
                return True
        elif choice == "latte":
            if res_check(choice):
                print(f"Enjoy your {choice}")
                return True
            else:
                return True
        elif choice == "cappuccino":
            if res_check(choice):
                print(f"Enjoy your {choice}")
                return True
            else:
                return True
        elif choice == "report":
            fun_res()
            return True
        elif choice == "off":
            print("Goodbye")
            exit()


def res_check(choice):
    get_choice = MENU.get(choice)
    choice_ingredient = get_choice.get("ingredients")
    choice_price = get_choice.get("cost")
    choice_milk = 0
    choice_water = 0
    choice_coffee = 0
    if "milk" in choice_ingredient:
        choice_milk = choice_ingredient.get("milk")
        if resources.get("milk") < choice_milk:
            print("Sorry there is not enough milk")
            return False
    if "water" in choice_ingredient:
        choice_water = choice_ingredient.get("water")
        if resources.get("water") < choice_water:
            print("Sorry there is not enough water")
            return False
    if "coffee" in choice_ingredient:
        choice_coffee = choice_ingredient.get("coffee")
        if resources.get("coffee") < choice_coffee:
            print("Sorry there is not enough coffee")
            return False
    if check_money(choice_price):
        res_cost(choice_milk, choice_water, choice_coffee)


def res_cost(milk, water, coffee):
    resources["milk"] -= milk
    resources["water"] -= water
    resources["coffee"] -= coffee


def fun_res():
    for i in resources:
        print(f"{i}: {resources[i]}")


def check_money(choice_price):
    quarters, dimes, nickles, pennies = ask_for_money()
    given = (quarters * 0.25)+(dimes*0.1)+(nickles*0.05)+(pennies*0.01)

    if given < choice_price:
        print("Sorry that's not enough money, money refunded.")
        return False
    if given > choice_price:
        change = round((given-choice_price), 2)
        print(f"Here is ${change} in change")
        return True
    if given == choice_price:
        print("Noice")
        return True

#  fixing no input by adding concatenating '0' with user input


def ask_for_money():
    print("Please insert coins")
    quarters = int('0'+input("How many quarters?: "))
    dimes = int('0'+input("How many dimes?: "))
    nickles = int('0'+input("How many nickles?: "))
    pennies = int('0'+input("How many pennies?: "))
    return quarters, dimes, nickles, pennies


def machine_status(machine):
    while machine:
        if customer_choice(True):
            print("Maybe get some coffee for you coworker?")


machine_status(True)
