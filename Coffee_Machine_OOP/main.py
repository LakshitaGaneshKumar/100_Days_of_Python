from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

QUARTER = 0.25
DIME = 0.10
NICKEL = 0.05
PENNY = 0.01

# Create Objects
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

def start_machine():
    """Starts the Machine"""
    user_choice = input(f"What would you like? ({menu.get_items()}): ").lower()

    if user_choice == "off":
        print("Machine is now off for maintenance.")
    
    elif user_choice == "report":
        coffee_maker.report()
        money_machine.report()
    
    elif user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
        drink = menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
        start_machine()
    
    else:
        start_machine()

start_machine()
