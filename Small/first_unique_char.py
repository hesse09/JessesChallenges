####################################################
# Program: firstUniqueChar.py
# Purpose: Finds the first non-repeating character
####################################################

def first_unique_char(text):
    counts = {}

    for i in range(len(text)):
        if text[i] not in counts:
            counts[text[i]] = 1
        else:
            counts[text[i]] += 1

    for i in text:
        if counts[i] == 1:
            return i

    return None


word = "swiss"

answer = first_unique_char(word)

print("First unique character:", answer)
