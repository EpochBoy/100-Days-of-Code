from art import logo
import random

#infinite deck
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
game_state = True
player_hand = []
dealer_hand = []
player_state = True
dealer_state = True
new_game = True
start_game = ""


#card picking function
def pick_card():
    card_amount = len(cards)
    card = cards[random.randint(0,card_amount-1)]
    return card

def play_game(new_game):
    game_on = input("Do you want to play a new game 'y' 'n'? ")
    if game_on == "n":
        new_game = False
        return new_game
    return new_game

#player hand logic
def check_player(player_hand, player_state):
    player_continue = input("Do you want another card 'y' 'n'? ")
    while player_continue == "y":
        player_hand.append(pick_card())
        if sum(player_hand) > 21:
            if 11 in player_hand:
                for i in range(len(player_hand)):
                    if player_hand[i] == 11:
                        player_hand[i] = 1
            elif 11 not in player_hand and sum(player_hand) > 21:
                print("Sorry you lost, house takes it all")
                player_continue = "n"
                player_state = False
                return player_state
        print(f"Your current hand is {player_hand} Sum: {sum(player_hand)}")
    return player_state

def check_dealer(dealer_hand, dealer_state):
    while sum(dealer_hand) < 17:
        dealer_hand.append(pick_card())
        if sum(dealer_hand) > 21:
            if 11 in dealer_hand:
                for i in range(len(dealer_hand)):
                    if dealer_hand[i] == 11:
                        dealer_hand[i] = 1
            elif 11 not in dealer_hand:
                dealer_state = False
                print("Dealer is Bust, you WIN!")
                return dealer_state
    return dealer_state

def check_winner(player_hand, dealer_hand, player_state, dealer_state, new_game):
    if dealer_state == True and player_state == True:
        if sum(dealer_hand) >= sum(player_hand):
            print("The house won, please try again")
            play_game(new_game)
        elif sum(player_hand) > sum(dealer_hand):
            print("Congratulations you won!")
            play_game(new_game)

def blackjack(player_hand, dealer_hand, player_state, dealer_state, start_game):
    print(logo)
    if start_game == "" and game_state == True:
        start_game = input("Do you want to play a game of Blackjack 'y' or 'n': ")
    if start_game == "y" and game_state == True:
        player_hand = [pick_card(), pick_card()]
        print(f"Your hand is: {player_hand}")
        dealer_hand = [pick_card(), pick_card()]
        print(f"Dealers hand is: [Hidden, {dealer_hand[0]}]")
        check_player(player_hand, player_state)
        print(f"Your final hand was {player_hand} SUM: {sum(player_hand)}")
        if player_state == True:
            print(f"Dealers hand is: {dealer_hand}")
            dealer_state = check_dealer(dealer_hand, dealer_state)
            if dealer_state == True:
                print(f"Dealers final hand was {dealer_hand} Sum: {sum(dealer_hand)}")
                check_winner(player_hand, dealer_hand, player_state, dealer_state, new_game)
            else:
                play_game(new_game)
        elif player_state == False:
            print(f"Dealers hand was: {dealer_hand}")
            game = play_game(new_game)
            if game == True:
                blackjack(player_hand, dealer_hand, player_state, dealer_state, start_game)
            else:
                game_state == False
    else:
        game_state == False




# pick_card()
blackjack(player_hand=player_hand, dealer_hand=dealer_hand, player_state=player_state, dealer_state=dealer_state, start_game=start_game)



#comp stays at 17

#compare function
