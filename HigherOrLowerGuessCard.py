
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

