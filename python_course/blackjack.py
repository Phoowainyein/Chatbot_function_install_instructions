#! /usr/bin/python3
import random 
def make_a_new_deck():
    deck_of_cards=[i for i in range(52)]
    for i in range(13):
        for y in range(4):
            if i<10:
                deck_of_cards[i+y*13]=i+1
            elif i >=10:
                deck_of_cards[i+y*13]=10
    random.shuffle(deck_of_cards)
    return deck_of_cards

def draw_card(deck):
    card = deck.pop()
    return card

def print_hands(dealer_hand_local,player_hand_local):
    print("Dealer has",dealer_hand_local)
    print("Player has",player_hand_local)

def ask_if_player_wants_card(player_hand_now):
    question = "you have now "+ str(player_hand_now) + "do you want another card"
    answer_local = input(question)
    return answer_local


deck = make_a_new_deck()
#print(deck)
while True:
    deck = make_a_new_deck()
    dealer_hand= [draw_card(deck)]
    player_hand = [draw_card(deck)]
    while True:
#asking if player wants a card 
        print_hands(dealer_hand,player_hand)
        answer = ask_if_player_wants_card(player_hand)
        if answer == "yes":

            player_hand = player_hand + draw_card(deck)
        if sum(player_hand) >= 21 :
            break
        elif answer == "no":
            break
        else:
            dealer_hand =dealer_hand+ draw_card(deck)

    while True:
        print_hands(dealer_hand,player_hand)
        if player_hand > 21:
            print("you went over,you lose")

        elif dealer_hand < 16:
            dealer_hand =dealer_hand +draw_card(deck)

        elif dealer_hand > 21 :
            print("dealer went over,you win!")
            break
    
        elif dealer_hand >= player_hand:
            print("dealer wins!")

        
        elif dealer_hand < player_hand:
            print("player wins")
   #ask user (do you want a new game ,press enter if you want to end type no)

        while True:
            answer = input("Do you want a new game \n press enter to play a new game \n type no to end game")
    
            if answer == "no":
                break
            else:
                print("so you want to play a new game !")"""



    



""" 
1.make deck
2.draw card for dealer
3.draw card for player
ask if player wants a card 
    until answer is no 
    or hand is over 21

if player is over 21 print(you went over,you lose)
if dealer has less thank 16 deal another card for dealer
if dealer is over 21 print(dealer went over,you win )
if dealer hand is bigger than player print(dealer wins)
if player hand is bigger than dealer print(player wins)"""
