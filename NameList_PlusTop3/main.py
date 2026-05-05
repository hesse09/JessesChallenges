def readNames(filename):
    with open(filename, "r") as file:
        contents = file.read()

    return contents


def countNames(names):
    counts = {}
    for i in names:
        if i not in counts:
            counts[i] = 1
        else:
            counts[i] += 1
    return counts


def displayTopThree(nameCounts):
    highest = {}
    for i in range(3):
        high_v = None
        high_k = ""
        for k, v in nameCounts.items():
            if k in highest:
                continue
            if high_v is None or v > high_v:
                high_v = v
                high_k = k
        highest[high_k] = high_v
    return highest


def main():
    names = readNames("names2025.txt")
    names_list = names.splitlines()

    names_counts = countNames(names_list)

    top_three = displayTopThree(names_counts)
    print("All Name Counts:")
    for k, v in names_counts.items():
        print("%s: %d" % (k, v))

    print("\nTop 3 Names:")
    it = 1
    for k, v in top_three.items():
        print("%d. %s - %d" % (it, k, v))
        it += 1


main()
