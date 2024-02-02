
# Guess the value 

import random

# Card constants
SUIT_TUPLE = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
RANK_TUPLE = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9','10', 'Jack', 'Queen', 'King')

ncards = 8

# supply a deck and get a random card from the deck provided
def getCard(deckListIn):
    thisCard = deckListIn.pop() #Pops one off the top of the deck and returns it
    return thisCard

# Supply a deck and get a shuffled copy of the deck
def shuffle(deckListIn):
    deckListOut = deckListIn.copy() # copy the starting deck
    random.shuffle(deckListOut)
    return deckListOut


print('Welcome to Higher or Lower.')
print('In this game you have to guess whether the next card to be shown will be higher or lower than the current card.')
print('Getting it right adds 20 points; get it wrong and you lose 15 points.')
print('You have 50 points to start.')
# print()

startingDeckList = []
for suit in SUIT_TUPLE:
    for thisValue, rank in enumerate(RANK_TUPLE):
        cardDict = {'rank':rank, 'suit':suit, 'value':thisValue + 1}
        startingDeckList.append(cardDict)
        