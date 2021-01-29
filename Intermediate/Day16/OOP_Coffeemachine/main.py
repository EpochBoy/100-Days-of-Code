from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


def machine():
    printMenu()
    while True:
        selector()


def printMenu():
    print("Hi, would you like some coffee?")
    print(f"We have these options: {menu.get_items()}")
    print("You can also get a report or turn off the machine.")


def selector():
    select = input("Please choose your brew: ").lower()
    if select == "report":
        coffee_maker.report()
        money_machine.report()
    elif select == "off" or select == "no" or select == "n":
        exit()
    elif menu.find_drink(select):
        selection = menu.find_drink(select)
        if coffee_maker.is_resource_sufficient(selection):
            if money_machine.make_payment(selection.cost):
                coffee_maker.make_coffee(selection)
                print("Would you like more coffee?")


machine()
