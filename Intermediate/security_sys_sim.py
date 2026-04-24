users = [
    {"username": "alex", "password": "coffee123", "role": "admin"},
    {"username": "riley", "password": "Riley2026!", "role": "manager"},
    {"username": "casey", "password": "abc", "role": "staff"},
    {"username": "morgan", "password": "MetroCity!", "role": "owner"},
    {"username": "jordan", "password": "StrongPass99!", "role": "engineer"},
    {"username": "guest", "password": "password", "role": "guest"},
]

symbols = "!@#$%&*"


def score_password(password):
    not_allowed = ["abc", "12345678", "coffee123", "password"]
    score: int = 0

    if len(password) >= 8:
        score += 1

    has_number = False
    for char in password:
        if char.isdigit():
            has_number = True
            break

    if has_number:
        score += 1

    has_uppercase = False
    for char in password:
        if char.isupper():
            has_uppercase = True
            break

    if has_uppercase:
        score += 1

    has_symbol = False
    for char in password:
        if char in symbols:
            has_symbol = True
            break

    if has_symbol:
        score += 1

    if password not in not_allowed:
        score += 1

    if score >= 4:
        risk = "Low"
    elif score == 3:
        risk = "Medium"
    elif score == 2:
        risk = "High"
    else:
        risk = "Critical"

    return score, risk


def build_security_report(users):
    security_report: dict = {}
    for i in users:
        user = i["username"]
        role = i["role"]
        password = i["password"]
        security_report[user] = {"Role": role, "Password": password}
    
    return security_report


def print_security_report(users):
    print("SECUIRTY REPORT\n---------------")
    security_report = build_security_report(users)
    names_score_list: list = []
    for k, v in security_report.items():
        score, risk = score_password(v["Password"])
        print("%s | %s | Score: %d | Risk: %s"
              % (k, v["Role"], score, risk))
        names_score_list.append((k, score, risk))

    lowest: int = None
    current: int
    lowest_name: str = ""
    for i in names_score_list:
        current = i[1]
        if lowest ==  None:
            lowest = current
            lowest_name = i[0]
        else:
            if current < lowest:
                lowest = current
                lowest_name = i[0]
    print("\nWeakest Account: %s" % lowest_name)
    length = len(names_score_list)
    total = 0
    for i in names_score_list:
        total += i[1]
    total = total / length
    print("Avaerage Score: %.2f" % total)

    reset_string = "Needs Reset:"
    for i in names_score_list:
        if i[2] == "Critical" or i[2] == "High":
            reset_string += " %s," % i[0]
    print(reset_string)

    

print_security_report(users)
