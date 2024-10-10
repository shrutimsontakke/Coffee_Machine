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

profit = 0

def is_resource_sufficient(order_ingredients):
    """Returns True when the order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources.get(item, 0):
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

def refill_resources():
    """Refills the resources."""
    resources["water"] += int(input("Enter the amount of water to add (ml): "))
    resources["milk"] += int(input("Enter the amount of milk to add (ml): "))
    resources["coffee"] += int(input("Enter the amount of coffee to add (g): "))
    print("Resources have been refilled!")

is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino/refill/report): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    elif choice == "refill":
        refill_resources()
    else:
        drink = MENU.get(choice)
        if drink:
            if is_resource_sufficient(drink["ingredients"]):
                payment = process_coins()
                if payment >= drink["cost"]:
                    change = round(payment - drink["cost"], 2)
                    if change > 0:
                        print(f"Here is ${change} in change.")
                    profit += drink["cost"]
                    make_coffee(choice, drink["ingredients"])
                else:
                    print("Sorry, that's not enough money. Money refunded.")
        else:
            print("Invalid choice. Please choose espresso, latte, cappuccino, refill, or report.")
