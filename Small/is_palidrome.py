####################################################
# Program: palindromeCheck.py
# Purpose: Checks if a word is a palindrome
####################################################

def is_palindrome(word):
    left = 0
    right = len(word) - 1

    while left <= right:
        if word[left] != word[right]:
            return False
        print(word[left], word[right])
        left += 1
        right -= 1

    return True


text = "racecar"

answer = is_palindrome(text)

print("Is palindrome:", answer)
