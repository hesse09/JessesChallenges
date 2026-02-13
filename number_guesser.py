# Desc: Guesses a user given number until correct
# Date: 2/3/2026
# Author: Jesse France


def validate(userNum: int, low: int, high: int) -> str:
    guessedNum = guess((low, high))
    print(f"Guessed {guessedNum}")
    if guessedNum == userNum:
        return f"Found your number {userNum}"
    if guessedNum > userNum:
        guessRange = (guessedNum - 1, userNum)
    elif guessedNum < userNum:
        guessRange = (userNum, guessedNum + 1)
    return validate(userNum, guessRange[0], guessRange[1])


def guess(range: tuple) -> int:
    guessedNum = (range[0] + range[1]) // 2
    return guessedNum


try:
    inputValue = int(input("Enter a number:"))
except Exception as e:
    raise ValueError(f"Enter a valid number. Traceback: {e}")

result = validate(inputValue, 1, inputValue)
print(result)
