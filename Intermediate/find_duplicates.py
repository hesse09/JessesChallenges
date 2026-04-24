sentence = input("Enter a sentence: ")

words = sentence.split()
print(words)

for word in words:
    has_duplicate = False
    letters = []
    for i in word:
        if i in letters:
            has_duplicate = True
            break
        else:
            letters.append(i)

    if has_duplicate:
        print(word, "has duplicate letters")
    else:
        print(word, "has no duplicate letters")
