import random
def getSum(vars: list[float]) -> float:
    vSum: float = 0
    for v in vars:
        vSum += v
    return vSum
def validateInput(token: str) -> list:
    weights = []
    token = token.split(" ")
    for t in token:
        tImp = random.random()
        weight = tImp * 0.9
        weights.append(weight)
    return weights
while True:
    try:
        try:
            inputValue = str(input("What can I help you with today? "))
        except Exception as e:
            print("Invalid input", e)
            continue

        if inputValue.strip() == "":
            continue
        weights = validateInput(inputValue)
        print(weights)
        finalWeight = getSum(weights)
        print(finalWeight)
        if finalWeight < 0.1:
            print("Wow you typed something short!")
        elif finalWeight > 0.9:
            print("Wow you typed something long!")

    except KeyboardInterrupt:
        print("Goodbye")
        break
