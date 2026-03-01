import math


def magnitude(a: list) -> int:
    total: float = 0.0
    for n in a:
        total += n**2
    return math.sqrt(total)


def dot_product(a: list, b: list) -> int:
    total: float = 0.0
    for i in range(len(a)):
        total += a[i] * b[i]

    return total


def cosine_similarity(a: list, b: list) -> float:
    aA = dot_product(a, b)
    m1 = magnitude(a)
    m2 = magnitude(b)

    return aA / (m1 * m2)


word_vectors = {
    "king": [0.9, 0.1, 0.5],
    "queen": [0.8, 0.2, 0.6],
    "pizza": [0.1, 0.9, 0.1],
    "food": [0.2, 0.8, 0.2],
}


def AIChatty(word_vectors):
    print("Hello, how can I help you today? You can quit anytime by typing 'quit'")

    similarities = {}
    for word in word_vectors:
        if word == user_input:
            continue
        similarity = cosine_similarity(word_vectors[word], word_vectors[user_input])
        similarities[word] = similarity

    best_match = None
    best_score = 0
    for w, s in similarities.items():
        if s > best_score:
            best_score = s
            best_match = w

    return best_match, best_score


while True:
    while True:
        print("Hello, how can I help you today? You can quit anytime by typing 'quit'")
        user_input = input("Call AiChatty a king: ")
        if user_input == "quit":
            break
        output = AIChatty(word_vectors)
        print("Yes I am a king and you are a ", str(output[0]))
