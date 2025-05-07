# tricksy battle
import os
import random

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen']

value_rank = {
    'Ace': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'Jack': 11,
    'Queen': 12
}

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    def __repr__(self):
        # how a card will look when printed
        return f"{self.value} of {self.suit}"
    def rank(self):
        # returns the numerical value
        return value_rank[self.value]

def build_deck():
    deck = []  # empty list to hold the cards
    for suit in suits:  # 4 each suit
        for value in values:  # 4 each value
            deck.append(Card(value, suit))  # add the lists together
    return deck  # return the deck of cards

def shuffled_deck(deck):
    random.shuffle(deck)

deck = build_deck()
shuffled_deck(deck)


for drawn_card in deck[:8]:
    print(drawn_card)

player_1_hand = deck[:8]
player_2_hand = deck[8:16]

deck = deck[16:]


for card in player_1_hand:
    print(f"Player 1's hand: {card}")

def play_round(player_1_hand, player_2_hand):
    print("New round")
    for i in range(len(player_1_hand)):
        print(str(i+1)) + ": " + str(player_1_hand[i])


chosen_card = int(input("Pick what card you want to play!: ") + str(len(player_1_hand)))