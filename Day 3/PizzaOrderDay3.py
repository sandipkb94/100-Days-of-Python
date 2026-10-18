#order pizza if else condition
size = input("Enter pizza size : S/M/L\n")
bill = 0
if size == "S" or size =="s":
    bill += 200

elif size == "M" or size =="m":
    bill += 300

elif size =="L" or size == "l":
    bill += 400

else : print("Wrong Input")

pepperoni = input("Do you want pepperoni? Y/N\n")

if pepperoni =="Y" or pepperoni =="y":
    if size == "S" or size =="s":
        bill += 50
    else : bill += 80

print("Your final bill is : Rs.", bill)