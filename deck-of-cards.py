import random

myList: list = [3,43,2,1,6,9,7]

ranks = ["Ace", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
cardSuites: list = ["Spade", "Heart", "Diamond", "Club"]
deck: list = []
aCard:int = -1

def cardInfo(cardNum: int) -> list:
    return(ranks[cardNum % 13] + " of " + cardSuites[cardNum//13])

for number in range(0, 52):
    deck.append(number)
    
random.shuffle(deck)

for i in range(0,4):
    aCard = deck.pop()
    print("Card dealt is: %s" % cardInfo(aCard))



