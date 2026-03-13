listToSort:list = []
print("Opening file...")
with open("file_1.txt", "r", encoding="UTF-8") as contents:
    print("Reading file...")
    print("Getting file contents into list...")
    numbers = contents.readlines()
    print("Cleaning list...")
    for n in numbers:
        listToSort.append(int(n.strip()))

print("Before sorting file: %s" % listToSort)
print("Sorting...")
for i in range(len(listToSort) - 1):
    for j in range(len(listToSort) - 1):
        if listToSort[j] > listToSort[j + 1]:
            listToSort[j], listToSort[j + 1] =  listToSort[j + 1], listToSort[j]

print("After sorting file: %s" % listToSort)

