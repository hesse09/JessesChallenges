items = input("Please enter the items you want to purchase!\n"
              "Milk, Bread, Eggs are avaiable \n"
              "Seperate each item with a comma (,): ").split(",")

itemsTotals = {"Milk": 2.00, "Bread": 4.50, "Eggs": 3.28}


am:int = 0
for i in items:
    am += itemsTotals[i]

print("Your total is", am, "please enter your payment amount.")
billAm = int(input("What size bill are using? 100, 50, 20, 10, 5, 1: "))

if billAm < am:
    print("Insufficent funds")
    raise

billAm = billAm - am

while billAm != 0:
    print(billAm)
    if billAm >= 100:
        billAm -= 100
        print("Spat out a 100")
    elif billAm >= 50:
        billAm -= 50
        print("Spat out a 50")
    elif billAm >= 20:
        billAm -= 20
        print("Spat out a 20")
    elif billAm >= 10:
        billAm -= 10
        print("Spat out a 10")
    elif billAm >= 5:
        billAm -= 5
        print("Spat out a 5")
    elif billAm >= 1:
        billAm -= 1
        print("Spat out a 1")
    elif billAm >= 0.25:
        billAm -= 0.25
        print("Spat out a Quarter")
    elif billAm >= 0.10:
        billAm -= 0.10
        print("Spat out a Dime")
    elif billAm >= 0.05:
        billAm -= 0.05
        print("Spat out a Nickel")
    elif billAm >= 0.01:
        billAm -= 0.01
        print("Spat out a Penny")
    else:
        billAm = 0



