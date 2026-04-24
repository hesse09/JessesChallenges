logs = [
    "INFO user=alex action=login",
    "WARN user=riley action=password_attempt",
    "ERROR user=casey action=payment_failed",
    "INFO user=alex action=checkout",
    "ERROR user=guest action=login_failed",
    "WARN user=casey action=password_attempt",
    "INFO user=morgan action=logout",
]

def parse_log(line):
    line = line.split()
    log_type = line[0]
    user_part = line[1].split("=")
    action_part = line[2].split("=")

    payload = {"User": user_part[1], "Log": log_type, "Action": action_part[1]}
    return payload
    


def build_log_report(logs):
    report = []
    for log in logs:
        payload = parse_log(log)
        report.append(payload)
    return report

def print_log_report(logs):
    parsed = build_log_report(logs)
    user_count = {}
    log_counts = {}
    error_counts = []
    for k in parsed:
        if not k["User"] in user_count:
            user_count[k["User"]] = 1
        else:
            user_count[k["User"]] += 1

        if not k["Log"] in log_counts:
            log_counts[k["Log"]] = 1
        else:
            log_counts[k["Log"]] += 1
        
        if k["Log"] == "ERROR":
            error_counts.append((k["User"], k["Action"]))
    
    largest: int = None
    lN: str = ""
    current: int
    for k, v in user_count.items():
        current = v
        if largest == None:
            largest = current
            lN = k
        else:
            if current > largest:
                largest = current
                lN = k
    print("LOG REPORT\n----------")
    print("Levels:")
    for k, v in log_counts.items():
        print("%s: %d" % (k, v))
    print("\nMost Active User: %s" % lN)
    print("\nErrors:")
    for e in error_counts:
        print("%s - %s" % (e[0], e[1]))

print_log_report(logs)

# LOG REPORT
# ----------
# Levels:
# INFO: 3
# WARN: 2
# ERROR: 2
#
# Most Active User: alex
#
# Errors:
# casey - payment_failed
# guest - login_failed
