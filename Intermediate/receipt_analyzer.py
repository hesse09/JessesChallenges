purchases = [
    {"item": "Notebook", "category": "School", "price": 2.50},
    {"item": "Pens", "category": "School", "price": 4.25},
    {"item": "Steak", "category": "Food", "price": 12.99},
    {"item": "Rice", "category": "Food", "price": 3.49},
    {"item": "Chicken", "category": "Food", "price": 9.75},
    {"item": "Shampoo", "category": "Household", "price": 6.99},
]

def get_total(purchases):
    total: float = 0
    for items in purchases:
        total += items["price"]
    return total
        
        

def get_category_totals(purchases)-> dict:
    temp: list = []
    categorys: dict = {}
    for i in purchases:
        if i["category"] in categorys:
            categorys[i["category"]] += i["price"]
        else:
            categorys[i["category"]] = i["price"]
    
    for i, p in categorys.items():
        temp.append((i, p))
    
    for u in range(len(temp) - 1):
        for j in range(len(temp) - u - 1):
            if temp[j][1] < temp[j + 1][1]:
                temp[j], temp[j + 1] = temp[j + 1], temp[j]
    return temp
        

def get_most_expensive_item(purchases)-> tuple:
    temp: list = []
    for i in purchases:
        temp.append((i["price"], i["item"]))
    
    highest: float = 0
    hI: str = ""
    for j in temp:
        if j[0] > highest:
            highest = j[0]
            hI = j[1]
    return highest, hI

def apply_tax(total, tax_rate)-> tuple:
    taxed = tax_rate * total
    return taxed, total + taxed

def print_receipt_summary(purchases, tax_rate):
    item_totals: int = get_total(purchases)
    most_expensive, most_ex_item = get_most_expensive_item(purchases)
    category_total = get_category_totals(purchases)
    taxed, taxed_price = apply_tax(item_totals, tax_rate)

    print("----------\nRECEIPT DATA\n----------")
    print("Subtotal: $%.2f" % item_totals)
    print("Tax: $%.2f" % taxed)
    print("Total: $%.2f" % taxed_price)
    print("\nCategory Totals:")
    for i in category_total:
        print("%s: $%.2f" % (i[0], i[1]))
    print("\nMost Expensive Item: %s" % most_ex_item)
    print("Price of Most Expensive: %.2f" %most_expensive)


taxRate = 0.08
print_receipt_summary(purchases, taxRate)
   
