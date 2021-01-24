import random
import os
from art import logo

#infinite deck
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#card picker
def pick_card():
    card_amount = len(cards)
    card = cards[random.randint(0,card_amount-1)]
    return card

#Clear screen / OS agnostic
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def start_game():
    start_game = input("Do you want to play a game of Blackjack 'y' or 'n': ")
    cls()
    if start_game == "y":
        return True
    else:
        return False

def more_cards(a):
    print(f"Your current hand is {a} Sum: {sum(a)}")
    user_choice = input("Do you want another card 'y' or 'n': ")
    if user_choice == "y":
        return True
    elif user_choice == "n":
        return False

def player(player_hand, player_state):
    player_continue = more_cards(player_hand)
    while player_continue:
        player_hand.append(pick_card())
        if sum(player_hand) > 21:
            if 11 in player_hand:
                for i in range(len(player_hand)):
                    if player_hand[i] == 11:
                        player_hand[i] = 1
            elif 11 not in player_hand and sum(player_hand) > 21:
                player_continue = False
                player_state = False
                break;
        player_continue = more_cards(player_hand)
    return player_hand, player_state

def dealer(dhand, dstate):
    while sum(dhand) < 17:
        dhand.append(pick_card())
        if sum(dhand) > 21:
            if 11 in dhand:
                for i in range(len(dhand)):
                    if dhand[i] == 11:
                        dhand[i] = 1
            elif 11 not in dhand and sum(dhand) > 21:
                # print(f"Dealers final hand {dhand} and sum: {sum(dhand)}")
                dstate == False
                return dhand, dstate
    return dhand, dstate

def check_winner(player_hand, dealer_hand, game_state):
    if sum(dealer_hand) > 21:
        print("Congratulations you win, house went over 21")
    elif sum(dealer_hand) == sum(player_hand):
        print("It's a draw! All bets are returned")
    elif sum(dealer_hand) > sum(player_hand):
        print("The house won!")
    elif sum(player_hand) > sum(dealer_hand):
        print("Congratulations you won!")    
    game_state = start_game()
    return game_state

def blackjack():
    print(logo)
    game_state = start_game()
    while game_state == True:
        print(logo)
        pstate = True
        dstate = True

        phand = [pick_card(), pick_card()]
        dhand = [pick_card(), pick_card()]
        print(f"Your hand is: {phand}")
        print(f"Dealers hand is: [Hidden, {dhand[0]}]")

        phand, pstate = player(phand, pstate)

        if pstate == True:
            #check for winner
            dhand, dstate = dealer(dhand, dstate)
            print(f"Player hand: {phand} Sum: {sum(phand)} and Dealer hand: {dhand} Sum: {sum(dhand)}")
            if dstate == True:
                check_winner(player_hand=phand, dealer_hand=dhand, game_state=game_state)
            elif dstate == False:
                print(f"You win, dealers final hand was {dhand}")
        elif pstate == False:
            print(f"You lost, your final hand was {phand} and Dealers was {dhand}")
            game_state = start_game()
    else:
        game_state = False
        print("I am stopping")

blackjack()
