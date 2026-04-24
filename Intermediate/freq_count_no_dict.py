words = ["Cats", "Cats", "Cow", "Piggy", "Cow", "Apple"]

unique_words = []
frequencies = []

# Your nested loop logic here
for i in range(len(words)):
    if words[i] not in unique_words:
        unique_words.insert(i, words[i])
        frequencies.insert(i, 1)
    else:
        frequencies[unique_words.index(words[i])] += 1

for i in range(len(unique_words)):
    print(unique_words[i] + ":", frequencies[i])
