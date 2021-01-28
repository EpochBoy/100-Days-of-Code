
from data import resources
from data import MENU

# Function to take input about User's Choice


def take_input():
    coffee_type = input(
        'What would you like? (espresso/latte/cappuccino)').lower()
    return coffee_type


# Print Report of Coffee
def print_report():
    for items in resources:
        print(f"{items} :  {resources[items]}")


# Function to Ask Money and Return Total
def ask_money():
    pennies = int(input('How Many Pennies? '))
    nickles = int(input('How Many Nickles? '))
    dimes = int(input('How Many Dimes? '))
    quarters = int(input('How Many Quarters? '))
    total = int((pennies * 0.01) + (nickles * 0.05) +
                (dimes * 0.10) + (quarters * 0.25))
    return total


# Function to Check Resources and Return Coffee or Error
def check_resources(coffee, amount):
    if resources["water"] > MENU[f"{coffee}"]["ingredients"]["water"] or resources["milk"] > MENU[f"{coffee}"]["ingredients"]["milk"] or resources["coffee"] > MENU[f"{coffee}"]["ingredients"]["coffee"]:
        change = amount - MENU[coffee]["cost"]
        print(f"Here's Your {coffee}")
        print(f"Here is your change: ${change}")
        return
    else:
        print("Machine Don't Have Enough Resources")
        return


# Function to Update Resources
def update_resources(res, coffee_type):
    if coffee_type == "espresso":
        res["water"] = int(res["water"]) - \
            int(MENU[f"{coffee_type}"]["ingredients"]["water"])
        res["coffee"] = int(res["coffee"]) - \
            int(MENU[f"{coffee_type}"]["ingredients"]["coffee"])
        print(res)
    else:
        res["water"] = int(res["water"]) - \
            int(MENU[f"{coffee_type}"]["ingredients"]["water"])
        res["milk"] = int(res["milk"]) - \
            int(MENU[f"{coffee_type}"]["ingredients"]["milk"])
        res["coffee"] = int(res["coffee"]) - \
            int(MENU[f"{coffee_type}"]["ingredients"]["coffee"])
        print(res)


# Function to Make Coffee
def make_coffee():
    coffee_type = take_input()
    amount = ask_money()
    if amount < MENU[coffee_type]["cost"]:
        money_required = MENU[coffee_type]["cost"] - amount
        print(f"You Don't Have Enough Money. You Need ${money_required} More.")
        return
    else:
        check_resources(coffee_type, amount)
        update_resources(resources, coffee_type)
        return


make_coffee()
