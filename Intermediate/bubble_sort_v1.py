def reverse_bubble_sort(numbers: list) -> list:
    for i in range(len(numbers)- 1):
        for j in range(len(numbers) - 1):
            if numbers[j] < numbers[j + 1]:
                numbers[j + 1], numbers[j]  =  numbers[j], numbers[j + 1]
    return numbers

def bubble_sort(numbers: list)-> list:
    for i in range(len(numbers)-1):
        for j in range(len(numbers) - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    return numbers

print("Welcome to number sorter! This uses a bubble sort method!")
numList: list = []
QUIT_KEY = "Q"
COMPLIE_KEY = "C"
COMPILE_MODE = False
while True:
    print("Enter a number to add to your list (q to quit)(c to compile):", end="")
    value = input()
    if value == QUIT_KEY or value == QUIT_KEY.lower():
        break
    elif value == COMPLIE_KEY or value == COMPLIE_KEY.lower():
        COMPILE_MODE = True
        while COMPILE_MODE:
            print("ew to exit and wipe list | e to exit and keep list")
            mode = input("LS for longest > smallest, SL for smallest to largest:")
            if mode == "ew" or mode == "EW":
                COMPILE_MODE = False
                numList = []
                break
            elif mode == "e" or mode == "E":
                COMPILE_MODE = False
                break
            elif mode == "LS" or mode == "ls":
                COMPILE_MODE = False
                success = reverse_bubble_sort(numList)
                numList = []
                print(success)
            elif mode == "SL" or mode == "sl":
                COMPILE_MODE = False
                success = bubble_sort(numList)
                numList = []
                print(success)
            else:
                print("Enter a valid input")
                continue
    else:
        try:
            value = int(value)
        except ValueError:
            print("Seems you did not enter a int")
            continue
        numList.append(value)
        print("Current list: %s" % numList)



