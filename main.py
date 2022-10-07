print("Menu ")
print("green - ₹30")
print("Chai - ₹25")
print("lemon - ₹60")

MENU = {
    "green": {
        "ingredients": {
            "water": 50,
            "Tea": 18,
        },
        "cost": 30,
    },
    "Chai": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "Tea": 24,
        },
        "cost": 25,
    },
    "lemon": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "Tea": 24,
        },
        "cost": 60,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "Tea": 100,
}


def make_Tea(Tea_type):
    resources["water"] -= MENU[Tea_type]["ingredients"]["water"]
    resources["Tea"] -= MENU[Tea_type]["ingredients"]["Tea"]
    if "milk" in MENU[Tea_type]["ingredients"]:
        resources["milk"] -= MENU[Tea_type]["ingredients"]["milk"]
    print(f'Here is your {Tea_type}. Enjoy!')


def check_transaction_successful(user_money, Tea_cost):
    if user_money < Tea_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        resources["money"] += Tea_cost
        change = user_money - Tea_cost
        print(f'Here is ₹{round(change, 2)} rupees in change.')
        return True


def insert_coins():
    print("Please insert coins.")
    rupees = int(input("how many rupees?: "))
    paise = int(input("how many paise?: "))
    
    monetary_value = (rupees * 1) + (paise * 0.1) 
    return monetary_value


def Tea_machine():
    Tea_machine_is_on = True

    while Tea_machine_is_on:
        machine_water = resources["water"]
        machine_milk = resources["milk"]
        machine_Tea = resources["Tea"]
        machine_money = resources["money"]

        green_water = MENU["green"]["ingredients"]["water"]
        green_Tea = MENU["green"]["ingredients"]["Tea"]
        green_cost = MENU["green"]["cost"]

        Chai_water = MENU["Chai"]["ingredients"]["water"]
        Chai_milk = MENU["Chai"]["ingredients"]["milk"]
        Chai_Tea = MENU["Chai"]["ingredients"]["Tea"]
        Chai_cost = MENU["Chai"]["cost"]

        lemon_water = MENU["lemon"]["ingredients"]["water"]
        lemon_milk = MENU["lemon"]["ingredients"]["milk"]
        lemon_Tea = MENU["lemon"]["ingredients"]["Tea"]
        lemon_cost = MENU["lemon"]["cost"]

        user_input = input(" What would you like? (green/Chai/lemon): ").lower()
        if user_input == "off":
            Tea_machine_is_on = False

        elif user_input == "report":
            print(f'Water: {machine_water}ml\nMilk: {machine_milk}ml\nTea: {machine_Tea}g\n'
                  f'Money: ₹{machine_money}')

        elif user_input == "green":
            if machine_water >= green_water:
                if machine_Tea >= green_Tea:
                    user_money = insert_coins()
                    if check_transaction_successful(user_money, green_cost):
                        make_Tea(user_input)
                else:
                    print("Sorry there is not enough Tea.")
            else:
                print("Sorry there is not enough water.")

        elif user_input == "Chai":
            if machine_water >= Chai_water:
                if machine_milk >= Chai_milk:
                    if machine_Tea >= Chai_Tea:
                        user_money = insert_coins()
                        if check_transaction_successful(user_money, Chai_cost):
                            make_Tea(user_input)
                    else:
                        print("Sorry there is not enough Tea.")
                else:
                    print("Sorry there is not enough milk.")
            else:
                print("Sorry there is not enough water.")

        elif user_input == "lemon":
            if machine_water >= lemon_water:
                if machine_milk >= lemon_milk:
                    if machine_Tea >= lemon_Tea:
                        user_money = insert_coins()
                        if check_transaction_successful(user_money, lemon_cost):
                            make_Tea(user_input)
                    else:
                        print("Sorry there is not enough Tea.")
                else:
                    print("Sorry there is not enough milk.")
            else:
                print("Sorry there is not enough water.")


resources["money"] = 0
Tea_machine()