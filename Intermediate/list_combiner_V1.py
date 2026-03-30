# VARS
list1: list[int] = []
list2: list[int] = []
mode: str = "list 1"

EXIT_KEY: str = "Q"
MODE_KEYS: dict[str, list] = {
    "list 1": list1,
    "list 2": list2,
}


# make function to help us do this
def addList(list1: list, list2: list) -> bool | list[int]:
    # making sure list are same length
    return_list: list[int] = []
    legnthOfList: tuple = (len(list1), len(list2))

    # if not, change approach
    if legnthOfList[0] != legnthOfList[1]:
        list_1_len = legnthOfList[0]
        list_2_len = legnthOfList[1]

        if list_1_len > list_2_len:
            for i in range(list_1_len):
                if i < len(list2):
                    return_list.append(list1[i] + list2[i])
                else:
                    return_list.append(list1[i])
        else:
            for i in range(list_2_len):
                if i < len(list1):
                    return_list.append(list1[i] + list2[i])
                else:
                    return_list.append(list2[i])
        return True, return_list

    # unpack and add
    for i in range(legnthOfList[0]):
        return_list.append(list1[i] + list2[i])

    return True, return_list


print("Welcome to List Combiner! Please enter your TWO list below\n[q,Q] to quit!")
while True:
    print("Add a number to %s or [c] to move on:" % mode, end="")
    user_input = input()
    if user_input == EXIT_KEY or user_input == EXIT_KEY.lower():
        print("Closing.....")
        break
    elif user_input == "c" or user_input == "C":
        if len(MODE_KEYS[mode]) == 0:
            verify = input(
                "%s has 0 numbers inserted, are you sure you want to continue [y/n]:"
                % mode
            )
            if verify == "y":
                mode = "list 2"
        elif mode == "list 2":
            success, new_list = addList(MODE_KEYS["list 1"], MODE_KEYS["list 2"])
            if not success:
                print("Error")
            else:
                print("Your new list is %s" % new_list)
                MODE_KEYS["list 1"].clear()
                MODE_KEYS["list 2"].clear()
                mode = "list 1"
        else:
            mode = "list 2"
        continue
    try:
        user_input = int(user_input)
        MODE_KEYS[mode].append(user_input)
    except Exception:
        print("Please enter a valid number")
