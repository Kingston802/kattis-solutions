n, dominantSuit = input().split()

cards = {
    'A':11,
    'K':4,
    'Q':3,
    'J':2,
    'T':10,
    '9':0,
    '8':0,
    '7':0,
}

dcards = {
    'A':11,
    'K':4,
    'Q':3,
    'J':20,
    'T':10,
    '9':14,
    '8':0,
    '7':0,
}
pointTotal = 0
for i in range(4*int(n)):
    card = input()
    if card[1] == dominantSuit:
        pointTotal += dcards[card[0]]
    else:
        pointTotal += cards[card[0]]

print(pointTotal)


    
