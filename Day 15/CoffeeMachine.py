MENU = {
    "espressoo" : {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "cost" : 150
    },
    "latte":{
        "ingredients":{
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 250
    },
    "cappuccino": {
        "ingredients" : {
            "water" : 250,
            "milk" : 100,
            "coffee": 24
        },
        "cost": 300
    }
}
profit = 0
resources = {
    "water" : 300,
    "milk" : 200,
    "coffee" : 100
}
def report() :
    """reports available ingredients remaining"""
    print(f"water : {resources['water']} ml")
    print(f"milk : {resources['milk']} ml")
    print(f"coffee : {resources['coffee']} g")
    print(f"Money: ₹{profit}")
    
def checkInventory(order):
    """false if ordered ingredients are greater than available ingredients"""
   # print(f"ORDERED: {order}")      # ORDERED: {'water': 200, 'milk': 150, 'coffee': 24}
   # print(f"AVAILABLE: {resources}")    # AVAILABLE: {'water': 300, 'milk': 200, 'coffee': 100}
    for items in order :
        if order[items] >= resources[items]:
            print(f"Sorry, there is not enough {items}")
            return False
           # resources[items] -= order[items]
        return True   
def processMoney():
    """calculated how much many the customer has entered"""
    print("Enter Rupees")
    total = int(input("How many Rs. 1: "))*1
    total += int(input("How many Rs. 2: "))*2
    total += int(input("How many Rs. 5: "))*5
    total += int(input("How many Rs. 10: "))*10
    total += int(input("How many Rs. 20: "))*20
    total += int(input("How many Rs. 50: "))*50
    total += int(input("How many Rs. 100: "))*100
    total += int(input("How many Rs. 200: "))*200
    total += int(input("How many Rs. 500: "))*500
    return total
def ProcessTransaction(moneyReceived, cost ):
    """check the item price, whether sufficient money is provided by the customer or not. returnm money if enough"""
    if moneyReceived >= cost :
        change = (moneyReceived-cost)
        print(f"Here is ₹{change} Rs. in change")
        global profit
        profit = profit + cost
        return True
    else :
        print("Sorry that's not enough money. Money refunded.")
        return False
def makeCoffee(drinkName, order):
    """makes the coffe when money is received and there is enough ingredients. after making, deduct ingredients"""
    for item in order:
        resources[item] -= order[item]
    print(f"Here is your {drinkName}. Enjoy!")

is_on = True
while is_on :
    try :
        choice = input("What would you like to have?[espresso|latte|cappuccino]: ").lower()
        if choice == "off":
            is_on = False
        elif choice == "report" :
            report()
        else :
            drink = (MENU[choice])
            if checkInventory(drink["ingredients"]) :
                moneyReceived = processMoney()
                if ProcessTransaction(moneyReceived, drink["cost"]) :
                    makeCoffee(choice, drink["ingredients"])
    except KeyError:
        print("Error: You didnot enter any coffee. Please enter between espresso|latte|cappuccino!")
        

