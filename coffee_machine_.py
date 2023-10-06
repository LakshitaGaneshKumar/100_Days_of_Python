from coffee_machine_data import MENU, resources

QUARTER = 0.25
DIME = 0.10
NICKEL = 0.05
PENNY = 0.01

def print_report():
    """Prints the report of what resources are left in the coffee machine"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")
    coffee_machine()


def update_resources(coffee_type):
    """Takes in a coffee type as input and updates the machine's available resources"""
    resources['water'] -= MENU[coffee_type]['ingredients']['water']
    resources['milk'] -= MENU[coffee_type]['ingredients']['milk']
    resources['coffee'] -= MENU[coffee_type]['ingredients']['coffee']
    resources['money'] += MENU[coffee_type]['cost']
    coffee_machine()


def run_machine(coffee_type):
    """Takes in a coffee type as input and runs the coffee machine"""
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))

    total_inserted = (quarters * QUARTER) + (dimes * DIME) + (nickels * NICKEL) + (pennies * PENNY)
    total_needed = MENU[coffee_type]['cost']
    remainder = round((total_inserted - total_needed), 2)

    if remainder > 0:
        print(f"Here is ${remainder} in change.")
        print(f"Here is your {coffee_type}. Enjoy!")
        update_resources(coffee_type)
    else:
        print("Sorry, that is not enough money. Money refunded.")
        coffee_machine()


def check_resources(coffee_type):
    """Takes in a coffee type as input and checks if the machine has enough resources to run"""
    water_left = resources['water']
    coffee_left = resources['coffee']
    milk_left = resources['milk']

    water_needed = MENU[coffee_type]['ingredients']['water']
    coffee_needed = MENU[coffee_type]['ingredients']['coffee'] 
    milk_needed = MENU[coffee_type]['ingredients']['milk']

    enough_resources = False

    if water_left >= water_needed:
        if coffee_left >= coffee_needed:
            if milk_left >= milk_needed:
                enough_resources = True
            else:
                print("Sorry, there is not enough milk left.")
        else:
            print("Sorry, there is not enough coffee left.")
    else:
        print("Sorry, there is not enough water left.")

    if enough_resources:
        run_machine(coffee_type)
    else:
        coffee_machine()


def coffee_machine():
    """Starts the coffee machine"""
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_choice == "off":
        print("Machine is now off for maintenance.")
        return
    elif user_choice == "report":
        print_report()
    elif user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
        check_resources(user_choice)
    else:
        coffee_machine()
    

coffee_machine()
