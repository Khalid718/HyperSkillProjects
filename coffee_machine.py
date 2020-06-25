water_supply = 400
milk_supply = 540
beans_supply = 120
cups_supply = 9
money_supply = 550


def buy():
    coffee_type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
    global water_supply, milk_supply, beans_supply, cups_supply, money_supply
    if coffee_type == "1":
        if min(water_supply // 250, beans_supply // 16) >= 1:
            print("I have enough resources, making you a coffee!")
            water_supply -= 250
            beans_supply -= 16
            money_supply += 4
            cups_supply -= 1
        elif water_supply // 250 < 1:
            print("Sorry, not enough water!")
        elif beans_supply // 16 < 1:
            print("Sorry, not enough coffee beans!")
    elif coffee_type == "2":
        if min(water_supply // 350, milk_supply // 75, beans_supply // 20) >= 1:
            print("I have enough resources, making you a coffee!")
            water_supply -= 350
            milk_supply -= 75
            beans_supply -= 20
            money_supply += 7
            cups_supply -= 1
        elif water_supply // 350 < 1:
            print("Sorry, not enough water!")
        elif milk_supply // 75 < 1:
            print("Sorry, not enough milk!")
        elif beans_supply // 20 < 1:
            print("Sorry, not enough coffee beans!")
    elif coffee_type == "3":
        if min(water_supply // 200, milk_supply // 100, beans_supply // 12) >= 1:
            print("I have enough resources, making you a coffee!")
            water_supply -= 200
            milk_supply -= 100
            beans_supply -= 12
            money_supply += 6
            cups_supply -= 1
        elif water_supply // 200 < 1:
            print("Sorry, not enough water!")
        elif milk_supply // 100 < 1:
            print("Sorry, not enough milk!")
        elif beans_supply // 12 < 1:
            print("Sorry, not enough coffee beans!")
    else:
        return

def fill():
    global water_supply, milk_supply, beans_supply, cups_supply
    water_add = int(input("Write how many ml of water do you want to add:"))
    milk_add = int(input("Write how many ml of milk do you want to add:"))
    beans_add = int(input("Write how many grams of coffee beans do you want to add:"))
    cups_add = int(input("Write how many disposable cups of coffee do you want to add:"))
    water_supply += water_add
    milk_supply += milk_add
    beans_supply += beans_add
    cups_supply += cups_add

def take():
    global money_supply
    print(f"I gave you ${money_supply}")
    money_supply = 0

def remaining():
    print(f"""The coffee machine has:
    {water_supply} of water
    {milk_supply} of milk
    {beans_supply} of coffee beans
    {cups_supply} of disposable cups
    {money_supply} of money""")

action = input("Write action (buy, fill, take, remaining, exit):")
while action != "exit":
    if action == "buy":
        buy()
    elif action == "fill":
        fill()
    elif action == "take":
        take()
    elif action == "remaining":
        remaining()
    action = input("Write action (buy, fill, take, remaining, exit):")

