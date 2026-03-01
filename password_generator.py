import random
import math
import string


def password_generator(text: str, symbols: bool, caps_allowed: bool) -> str:
    currentlegnth = int(len(text))
    newPasswordLegnth = max(math.floor(currentlegnth * 1.5), 10)
    if symbols:
        allowedSymbols = ["!", "@", "#", "^"]

    if not caps_allowed or caps_allowed:
        newPassword = ""
        for i in range(newPasswordLegnth):
            num = random.randint(0, 10)
            if symbols and num > 9:
                newPassword += random.choice(allowedSymbols)
            elif caps_allowed:
                newPassword += random.choice(string.ascii_letters)
            else:
                newPassword += random.choice(string.ascii_lowercase)

    return newPassword


while True:
    try:
        password = str(input("Enter your passwword (fake): "))
        newPassword = password_generator(password, True, True)
        print("your new password is: " + newPassword)
    except KeyboardInterrupt:
        print("exiting")
        exit()
