####################################################
# Program: reverseWord.py
# Purpose: Reverses a word
####################################################

def reverse_word(word):
    reversed_word = ""

    for i in range(len(word)):

        r = len(word) - i - 1

        reversed_word += word[r]

    return reversed_word


text = "python"


answer = reverse_word(text)

print("The reversed word is:", answer)
