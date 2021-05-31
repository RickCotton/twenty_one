''' 
This program pits one player against the dealer (AI) 
in a fierce game of blackjack!
'''

import random

CARD_VALUE = {'2H':2,'3H':3,'4H':4,'5H':5,'6H':6,'7H':7,'8H':8,'9H':9,'10H':10,'JH':10,'QH':10,'KH':10,'AH':1,'2D':2,'3D':3,'4D':4,'5D':5,'6D':6,'7D':7,'8D':8,'9D':9,'10D':10,'JD':10,'QD':10,'KD':10,'AD':1,'2S':2,'3S':3,'4S':4,'5S':5,'6S':6,'7S':7,'8S':8,'9S':9,'10S':10,'JS':10,'QS':10,'KS':10,'AS':1,'2C':2,'3C':3,'4C':4,'5C':5,'6C':6,'7C':7,'8C':8,'9C':9,'10C':10,'JC':10,'QC':10,'KC':10,'AC':1}
DECK = ['2H','3H','4H','5H','6H','7H','8H','9H','10H','JH','QH','KH','AH','2D','3D','4D','5D','6D','7D','8D','9D','10D','JD','QD','KD','AD','2C','3C','4C','5C','6C','7C','8C','9C','10C','JC','QC','KC','AC','2S','3S','4S','5S','6S','7S','8S','9S','10S','JS','QS','KS','AS']

def deal_cards():
    deck = DECK

#Shuffle deck
    random.shuffle(deck)
    cards_dealt = 0

# Deal Player Cards & Remove From Deck. 
    p1_hand = []    # Stores the cards in the hand.
    p1_card1 = deck.pop(cards_dealt)  # Removes a cards from the deck. Stores it as P1C1.
    cards_dealt += 1  # Counts the number of cards dealth.
    p1_hand.append(p1_card1) # Stores the actual cards (not the values) of Player 1's hand.
    # Card 2.
    p1_card2 = deck.pop(cards_dealt)
    cards_dealt += 1
    p1_hand.append(p1_card2)
    print("Your have been dealt the " + p1_card1 + " " + p1_card2)

# Deal Dealer Cards & Remove From Deck.
    dealer_hand = []
    dealer_card1 = deck.pop(cards_dealt)
    cards_dealt += 1
    dealer_hand.append(dealer_card1)
    dealer_card2 = deck.pop(cards_dealt)
    cards_dealt += 1
    dealer_hand.append(dealer_card2)
    print("The dealer is showing the " + dealer_card2)
    print("Player 1: " + ", ".join(p1_hand) + "     Dealer: " + (dealer_card2))

# Check Player Aces.
    p1_ace_count = 0
    for aces in p1_hand:
        for char in aces:
            if char == 'A':
                p1_ace_count += 1

# Check Dealer Aces.
    dealer_ace_count = 0
    for aces in dealer_hand:
        for char in aces:
            if char == 'A':
                dealer_ace_count += 1

# Value of Player Hand.
    p1_hand_value = []
    p1_card1_value = CARD_VALUE[(p1_card1)]
    p1_card2_value = CARD_VALUE[(p1_card2)]
    p1_hand_value.append(p1_card1_value)
    p1_hand_value.append(p1_card2_value)

# Check Player Blackjack.
    p1_bj_value = 0
    if p1_ace_count == 1:
        p1_bj_value = sum(p1_hand_value) + 10 #Aces assigned as 1. Add 10 to determine if P1 has blackjack with an ace.
    if p1_bj_value == 21:
        print("")
        print("B-L-A-C-K-J-A-C-K! CONGRATULATIONS!")
        play_again()

# Value of Dealer Hand.
    dealer_hand_value = []
    d_card1_value = CARD_VALUE[(dealer_card1)]
    d_card2_value = CARD_VALUE[(dealer_card2)]
    dealer_hand_value.append(d_card1_value)
    dealer_hand_value.append(d_card2_value)

# Check Dealer Blackjack.
    dealer_bj_value = 0
    if dealer_ace_count == 1:
        dealer_bj_value = sum(dealer_hand_value) + 10
    if dealer_bj_value == 21:
        print("")
        print("OH NO! DEALER B-L-A-C-K-J-A-C-K!")
        print("Player 1: " + ", ".join(p1_hand) + "     Dealer: " + ", ".join(dealer_hand))
        play_again()

# Player 1 Plays.
    print("")
    p1_total = sum(p1_hand_value)
    decision = input("What do you want to do? [H]it to add a card. [S]tand to stay with your current hand. (H/S): ")
    while (decision != "H") and (decision != "S"):
        print("")
        print("Please try again: ")
        decision = input("What do you want to do? [H]it to add a card. [S]tand to stay with your current hand. (H/S): ")
    while decision != "S":
        # Take a Card
        p1_card = deck.pop(cards_dealt)  # Removes a cards from the deck and stores it.
        cards_dealt += 1  # Counts the number of cards dealth.
        p1_hand.append(p1_card) # Stores the actual cards (not the values) of Player 1's hand.
        # Determine the Card Value
        p1_card_value = CARD_VALUE[(p1_card)] # Looks up the card value.
        p1_hand_value.append(p1_card_value) # Adds card value to the running total.
        # Check for Aces
        p1_ace_count = 0
        for aces in p1_hand:
            for char in aces:
                if char == 'A':
                    p1_ace_count += 1
        # Determine Optimal Value of Player Hand.
        p1_total_aces = 0
        p1_total = sum(p1_hand_value) # Converts list to a integer value.
        if p1_ace_count >= 1:   # Factors in that Aces can be 11 or 1.
            p1_total_aces = p1_total + 10 # Determines the value as 11. Even with multiple aces, only 1 ace can be worth 11 or hand will bust.
        if (p1_total_aces > p1_total) and (p1_total_aces <= 21): # Compares value with ace as 11 versus 1.
            p1_total = p1_total_aces # Selects the best hand.
        # Announce the card.
        print("You added the " + (p1_card))
        print("Player 1: " + ", ".join(p1_hand) + "     Dealer: " + (dealer_card2))
        print("")
        # Check to see if the hand has busted
        if p1_total > 21:
            print("Sorry! You busted!")
            print("Player 1: " + ", ".join(p1_hand) + "     Dealer: " + ", ".join(dealer_hand))
            play_again()
        else:
            decision = input("What do you want to do? [H]it to add a card. [S]tand to stay with your current hand. (H/S): ")

# Dealer Takes Card If Dealer Has Soft 17 (Includes Ace) or Total < 17 (No Aces)
    dealer_total = sum(dealer_hand_value)
    while (dealer_total <= 17 and dealer_ace_count >= 1) or (dealer_total < 17 and dealer_ace_count ==0):   # Factors in that Aces can be 11 or 1.
        # Take a Card
        dealer_card = deck.pop(cards_dealt)  # Removes a cards from the deck. Stores it as a card.
        cards_dealt += 1  # Counts the number of cards dealt.
        dealer_hand.append(dealer_card) # Stores the actual cards (not the values) in the dealer's hand.
        # Determine the Card Value
        dealer_card_value = CARD_VALUE[(dealer_card)] # Looks up the value of the dealer card.
        dealer_hand_value.append(dealer_card_value) # Adds card value to the running total.
        dealer_total = sum(dealer_hand_value) # Converts list to a integer value.
        #Check for Aces
        for aces in dealer_hand:
            for char in aces:
                if char == 'A':
                    dealer_ace_count += 1
        # Determine Optimal Value of Dealer Hand
        dealer_total_aces = 0 # Sum of the hand factoring in aces as 11 or 1.
        dealer_total = sum(dealer_hand_value) # Converts list to a integer value.
        if dealer_ace_count >= 1:   # Factors in that Aces can be 11 or 1.
            dealer_total_aces = dealer_total + 10 # Determines the value as 11. Even with multiple aces, only 1 ace can be worth 11 or hand will bust.
        if (dealer_total_aces > dealer_total) and (dealer_total_aces <= 21): # Compares value with ace as 11 versus 1.
            dealer_total = dealer_total_aces # Selects the best hand.
        print("")
        print("Dealer takes a " + (dealer_card))
        print("Player 1: " + ", ".join(p1_hand) + "     Dealer: " + ", ".join(dealer_hand))

# Deliver Outcome. Who Won?
    if int(dealer_total) > 21:
        print("")
        print("DEALER BUSTED! CONGRATULATIONS! YOU WIN!")
        play_again()
    elif int(p1_total) > int(dealer_total):
        print("")
        print("Congratulaitons! YOU BEAT THE DEALER!")
        print("Player 1: " + ", ".join(p1_hand) + "     Dealer: " + ", ".join(dealer_hand))
        play_again()
    elif int(p1_total) == int(dealer_total):
        print("")
        print("It's a push! Nobody wins!")
        print("Player 1: " + ", ".join(p1_hand) + "     Dealer: " + ", ".join(dealer_hand))
        play_again()
    else:
        print("")
        print("Sorry! Dealer wins with a better hand!")
        print("Player 1: " + ", ".join(p1_hand) + "     Dealer: " + ", ".join(dealer_hand))
        play_again()

# Play Again?
def play_again():
    print("")
    play_one_more = input("Do you want to play again (Y/N)? ")
    print("")
    while (play_one_more != "N") and (play_one_more != "Y"):
        print("")
        print("Please try again: ")
        play_one_more = input("Do you want to play again (Y/N)? ")
    if (play_one_more == "N"):
        print("Thanks for playing Code In Place Blackjack!")
        exit()
    else:
        deal_cards()

# Blackjack Introduction
def introduction():
    print("")
    print("Welcome to Code In Place Blackjack!")
    know_how_to_play = input("Do you know how to play blackjack (Y/N)? ")
    print("")
    while (know_how_to_play != "N") and (know_how_to_play != "Y"):
        print("")
        print("Please try again: ")
        know_how_to_play = input("Do you know know how to play blackjack (Y/N)? ")
    if (know_how_to_play == "N"):
        instructions()

# Blackjack Instructions
def instructions():
    print("")
    print("No problem, its easy to get started! A quick overview:")
    print("- The goal of blackjack is to beat the dealer without going over 21.")
    print("- Numbered cards are worth the value indicated.")
    print("- Face cards are worth 10.")
    print("- Aces are worth 1 or 11, whichever makes a better hand.")
    print("- Each player starts with two cards.")
    print("- One dealer card is always hidden until the end.")
    print("- To ask for another card, say 'hit'.")
    print("- To hold your total and end your turn, say 'stand'.")
    print("- If you go over 21, you bust and the dealer wins.")
    print("- If you are dealt 21 (Ace & 10) to start, you got a blackjack!")
    print("- Dealer will hit until their cards total 17 or higher.")

def main():
    player_name = introduction()
    deal_cards()
