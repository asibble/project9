import random

SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
assert(len(SUITS) == 4)
assert(len(RANKS) == 13)
assert(4 * 13 == 52)

class Card:
    def __init__(self, index):
        assert(index >= 0)
        assert(index < 52)
        self.index = index
    def suit(self):
        return SUITS[self.index // 13]
    def rank(self):
        return RANKS[self.index % 13]
    def __str__(self):
        return '{}/{}'.format(self.rank(), self.suit())
    def __repr__(self):
        return str(self)
    
def make_card(rank: str, suit: str) -> Card:
    rank_i = RANKS.index(rank)
    if rank_i < 0:
        raise ValueError(rank)
    suit_i = SUITS.index(suit)
    if suit_i < 0:
        raise ValueError(suit)
    return Card(rank_i + (13 * suit_i))

c = make_card('J', 'Hearts')
assert(c.rank() == 'J')
assert(c.suit() == 'Hearts')

def make_deck():
    """ Generate all 52 cards and shuffle them. """
    keep = []
    for i in range(52):
        keep.append(Card(i))
    random.shuffle(keep)
    return keep
def make_hand(hand_size=5):
    deck=make_deck()
    hand=[]
    for i in range(hand_size):
        cur_card=deck[random.randint(0, len(deck)-1)]
        hand.append(cur_card)
        deck.remove(cur_card)
    return hand
def has_a_pair(cards: list):
    seen=[]
    for i in cards:
        if i.rank() in seen:
            return True
        seen.append(i.rank())
    return False

def all_the_same_suit(cards: list):
    seen=[]
    for i in cards:
        if i.suit() not in seen:
            seen.append(i.suit())
    if len(seen)==1:
        return True
    return False

#High Low Game
def high_low():
    user_card=make_hand(1)[0]
    opp_card=make_hand(1)[0]
    print("Your card is",user_card)
    while True:
        guess=input("Do you think the next card will be lower or higher? \n 1. Lower \n 2. Higher\n ")
        if guess=="1":
            if user_card.rank() > opp_card.rank():
                print("You win! It was",opp_card)
                return
            elif user_card.rank() < opp_card.rank():
                print("You lose. It was",opp_card)
                return
        elif guess=="2":
            if user_card.rank() < opp_card.rank():
                print("You win! It was",opp_card)
                return
            elif user_card.rank() > opp_card.rank():
                print("You lose. It was",opp_card)
                return
            
high_low()
x=input("The following loop checks randomly-drawn 5-card hands until it finds a flush. \nEnter anyhting to proceed")
while True:
    hand=make_hand()
    print(hand)
    print("Is there a pair?", has_a_pair(hand))
    print("Are they all the same suit?", all_the_same_suit(hand))
    if all_the_same_suit(hand):
        break
