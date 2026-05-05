def readOrders(filename):
    with open(filename, "r") as file:
        contents = file.read()
    return contents


def displayOrders(orders) -> str:
    orders = orders.splitlines()
    finalString = ""
    for o in orders:
        line = o = o.split(",")
        payload = "Customer: %s | Item: %s | Price: %s" % (line[0], line[1], line[2])
        finalString = finalString + payload + "\n"
    return finalString


def countItems(orders) -> dict[str, int]:
    orders = orders.splitlines()
    items = {}
    for o in orders:
        line = o.split(",")
        if line[1] not in items:
            items[line[1]] = 1
        else:
            items[line[1]] += 1
    return items


def calculateTotalSales(orders) -> float:
    orders = orders.splitlines()
    total: float = 0
    for o in orders:
        line = o.split(",")
        total += float(line[2])
    return total


def findMostCommonItem(itemCounts) -> tuple[int, str]:
    high = None
    highI = ""
    for k, v in itemCounts.items():
        if high is None:
            high = v
            highI = k
        elif v > high:
            high = v
            highI = k
    return (high, highI)


def selectionSort(orders) -> str:
    # make a list thats easy to use
    orders = orders.splitlines()
    orders = [o.split(",") for o in orders]
    # swap
    for i in range(len(orders) - 1):
        temp = i
        minV = i
        for j in range(i + 1, len(orders)):
            if float(orders[j][2]) < float(orders[minV][2]):
                minV = j
        orders[temp], orders[minV] = orders[minV], orders[temp]

    return orders


def binarySearch(sortedItems, key):
    left = 0
    right = len(sortedItems) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if sortedItems[mid].lower() == key:
            return mid
        elif key < sortedItems[mid].lower():
            right = mid - 1
        elif key > sortedItems[mid].lower():
            left = mid + 1

    return None


def saveReport(filename, orders, itemCounts, totalSales, mostCommonIP, mostCommonItem):
    originalC = readOrders(filename)
    payload = ""
    payload = payload + "All Orders:\n%s" % orders
    payload = payload + "\nItem Counts:"
    for k, v in itemCounts.items():
        payload = payload + "\n%s: %d" % (k, v)
    payload = payload + "\nTotal Sales: $%.2f" % totalSales
    payload = payload + "\n\nMost Common Item: %s" % mostCommonItem
    payload = payload + "\nTimes Ordered: %d" % mostCommonIP

    with open(filename, "w") as file:
        file.write(originalC + "\n" + payload)
    return payload


def main():
    user_mode: str = ""
    while user_mode != "Quit":
        print(
            "===== OzMart Order Analyzer =====\n1. Display all orders\n2. Display item counts\n3. Display total sales\n4. Display most common item\n"
            "5. Sort orders by price\n6. Search for an item\n7. Save report\n8. Quit\nEnter your choice:",
            end="",
        )
        try:
            user_mode = input()
            if user_mode == "Quit":
                print("Quitting....")
            else:
                user_mode = int(user_mode)
        except ValueError:
            print("Please enter a valid interger!")

        orders = readOrders("orders2025.txt")

        if user_mode == 1:
            orders_to_display = displayOrders(orders)
            print("-------ALL ORDERS---------")
            print(orders_to_display)
        elif user_mode == 2:
            item_counts = countItems(orders)
            print("-------ITEM COUNTS---------")
            for k, v in item_counts.items():
                print("%s: %d" % (k, v))
        elif user_mode == 3:
            order_total = calculateTotalSales(orders)
            print("-------ORDER TOTAL---------")
            print("Total Sales: $%.2f" % order_total)
        elif user_mode == 4:
            iC = countItems(orders)
            high_price, high_item = findMostCommonItem(iC)
            print("-------MOST COMMON---------")
            print("Most Common Item: %s\nTimes Ordered: %d" % (high_item, high_price))
        elif user_mode == 5:
            sorted_items = selectionSort(orders)
            print("-------SORTED ITEMS---------")
            finalString = ""
            for line in sorted_items:
                payload = "Customer: %s | Item: %s | Price: %s" % (
                    line[0],
                    line[1],
                    line[2],
                )
                finalString = finalString + payload + "\n"
            print(finalString)
        elif user_mode == 6:
            items = ["Coffee", "Keyboard", "Monitor", "Mouse", "Notebook"]
            print("------Items-----")
            for i in items:
                print(i)
            key = input("Enter a item to search for:").strip().lower()
            found_item = binarySearch(items, key)
            print("-------FOUND ITEM---------")
            print(f"Found at index: {found_item}")
        elif user_mode == 7:
            orders_display = displayOrders(orders)
            item_count_display = countItems(orders)
            total_sales_display = calculateTotalSales(orders)
            iC = countItems(orders)
            high_price_d, high_item_d = findMostCommonItem(iC)
            report = saveReport(
                "orders2025.txt",
                orders_display,
                item_count_display,
                total_sales_display,
                high_price_d,
                high_item_d,
            )
            print(report)
    else:
        print("Goodbye!")


main()
