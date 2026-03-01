def calculate_password_strength(weight: int) -> str:
    if weight < 2:
        return "Bad"
    elif weight >= 2 and weight < 5:
        return "Very Weak"
    elif weight >= 5 and weight < 8:
        return "Weak"
    elif weight >= 8 and weight < 12:
        return "Moderate"
    elif weight >= 12 and weight < 18:
        return "Strong"
    else:
        return "Very Strong"


def get_weights(password: str) -> int:
    weight: int = 0
    bias: dict = {
        "lenght": 0.5,
        "special": 0.3,
        "upper": 1,
        "patterns": 1,
    }
    letters = list(password)
    # CACL LEGNTH BIAS
    lenOfPass = int(len(password))
    weight += lenOfPass * bias["lenght"]
    print(weight)
    # CHECK SPEC PASS
    specail_chars: int = 0
    upper_chars: int = 0
    pattern: int = 0
    lastchar: str = ""
    for l in letters:
        if not l.isalnum():
            specail_chars += 1
        elif l.isupper():
            upper_chars += 1
        if lastchar == "":
            lastchar = str(l)
        elif lastchar != l:
            lastchar = str(l)
            pattern += 1

    if specail_chars != 0:
        weight += specail_chars * bias["special"]
    if upper_chars != 0:
        weight += upper_chars * bias["upper"]
    if pattern != 0:
        weight += pattern * bias["patterns"]

    return weight


while True:
    try:
        password = str(input("Enter your passwword (fake): "))
        weight = get_weights(password)
        output = calculate_password_strength(weight)
        print("Your password is:", output)
    except KeyboardInterrupt:
        print("exiting")
        exit()
