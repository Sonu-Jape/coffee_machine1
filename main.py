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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        return True


QUARTERS =  0.25
DIMES = 0.10
NICKLES = 0.05
PENNIES = 0.01

LATTE = 2.5
EXPRESSO = 1.5
CAPPUCINO = 3.00



def processes_coins():
    print("Please insert coins.")
    total = int(input("How many quarters?")) * QUARTERS
    total += int(input("How many dimes?")) * DIMES
    total += int(input("How many nickles?")) * NICKLES
    total += int(input("How many pennies?")) * PENNIES
    return total


def if_transaction_successful(money_received , drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost,2)
        print(F"Here is $ {change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True


while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = processes_coins()
            if if_transaction_successful(payment, drink["cost"]):
                make_coffee(choice,drink["ingredients"])












