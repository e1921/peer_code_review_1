# tricksy battle
import os
import random
import time

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
    """
    represents a card with a value and suit
    """
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    def __repr__(self):
        # how a card will look when printed
        return f"{self.value} of {self.suit}"
    def rank(self):
        "returns the numerical rank of the card"
        return value_rank[self.value]

def build_deck():
    """
    builds/returns 48 card deck with no kings
    """
    deck = []  # empty list to hold the cards
    for suit in suits:  # 4 each suit
        for value in values:  # 4 each value
            deck.append(Card(value, suit))  # add the lists together
    return deck  # return the deck of cards

def shuffled_deck(deck):
    random.shuffle(deck)

deck = build_deck()
shuffled_deck(deck)

print("Shuffling the deck..")
time.sleep(1)

print("Dealing cards..")
time.sleep(1)


player_1_hand = deck[:8]
player_2_hand = deck[8:16]
deck = deck[16:]


for card in deck[:8]:
    print(card)

def play_round(player_1_hand, player_2_hand):
    print("New round")
    print("Player 1's hand: ")
    for card in player_1_hand:
        print(card)

    print("Player 1 is thinkning..")
    time.sleep(2)

    relevant_cards = [str(card) for card in player_1_hand]

    chosen_card = input(f"Pick what card you want to play: {', '.join(relevant_cards)}\n")


    while chosen_card not in relevant_cards:
        print("Chosen card not in your hand, please choose another: ")
        chosen_card = input("Pick what card you want to play!: ")


    chosen_card_object = None
    for card in player_1_hand:
        if str(card) == chosen_card:
            chosen_card_object = card
            # print("Player 1 played this card:", chosen_card_object)
            break




    if chosen_card_object:
        time_at_play = time.strftime("%I:%M:%S %p")
        time.sleep(1)
        print(f"Player 1 {chosen_card_object} at {time_at_play}.")


play_round(player_1_hand, player_2_hand)
