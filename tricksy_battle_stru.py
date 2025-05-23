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

def build_deck(): # creating a deck using the lists just made
    """
    builds/returns 48 card deck with no kings
    """
    deck = []  # empty list to hold the cards
    for suit in suits:  # 4 each suit
        for value in values:  # 4 each value
            deck.append((value, suit))  # add the lists together
    return deck  # return the deck of cards

deck = build_deck()
random.shuffle(deck) # shuffles list

# test # print("test for proper deck length of 48: ", len(build_deck))

print("Shuffling the deck..")
time.sleep(2)


print("Dealing cards..")
time.sleep(2)

player_1_hand = deck[:8]
player_2_hand = deck[8:16]
deck = deck[16:]

def printed_card(card):
    """
    card tuple given (value, suit), returns string
    """
    return card[0] + " of " + card[1]

def play_round(player_1_hand, player_2_hand): # all operations of one round
    """
    plays one round of the game where player 1 chooses a card from their hand to play
    
    returns the card chosen by player 1 and what time they chose it
    """
    print("New round")
    print("Player 1's hand: ")
    for card in player_1_hand:
        print(printed_card(card))
              
    print("Player 1 is thinking..")
    time.sleep(3)

    relevant_cards = [printed_card(card) for card in player_1_hand]

    chosen_card = input(f"Pick what card you want to play: {', '.join(relevant_cards)}\n") # joins all cards in hand 
# Currently, the player's input must exactly match the card string, including capitalization and spaces.
# This strict matching might lead to user frustration if they make minor mistakes in typing.
# Making the input check case-insensitive and trimming extra spaces could improve usability and the overall user experience.    
    while chosen_card not in relevant_cards: # checking for existence of input in the hand
            print("Chosen card not in your hand, please choose another: ")
            chosen_card = input("Pick what card you want to play!: ")


    for card in player_1_hand: # break input loop if chosen card is found in hand
            if str(printed_card(card)) == chosen_card:
                chosen_card = card
                break
            
    time_at_play = time.strftime("%I:%M:%S %p") # time stamp for hour, minute, and second
    print(f"Player 1 played {printed_card(chosen_card)} at {time_at_play}.")
    return chosen_card, time_at_play


play_round(player_1_hand, player_2_hand)
