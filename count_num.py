# Desc: Counts an inputed number for the user
# Date: 2/3/2026
# Author: Jesse France


def count(num: int) -> str:
    interval = 1
    while interval <= num:
        print(interval)
        interval += 1

    return f"Successfully counted to {num}"


try:
    number = int(input("Enter a number: "))
except Exception as e:
    raise ValueError(f"Enter a valid number. Traceback: {e}")


result = count(number)
print(result)
