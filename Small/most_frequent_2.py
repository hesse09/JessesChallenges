####################################################
# Program: mostFrequent.py
# Purpose: Finds the most frequent number in a list
####################################################

def most_frequent(numbers):
    freq = {}

    for i in range(len(numbers)):
        if numbers[i] in freq:
            freq[numbers[i]] += 1
        else:
            freq[numbers[i]] = 1

    largest_n = None
    largest_k = 0
    for k in freq:
        if largest_n is None:
            largest_n = freq[k]
            largest_k = k
        elif freq[k] > largest_n:
            largest_n = freq[k]
            largest_k = k

    return largest_k



nums = [4, 2, 4, 7, 4, 2, 9]

answer = most_frequent(nums)

print("Most frequent number:", answer)
