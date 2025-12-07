# -*- coding: utf-8 -*-
"""
Created on Sun Dec  7 00:01:13 2025

@author: toora
"""
#importing modules
from Blackjack_module1 import *

blackjack=(r''' 
 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
                       _/ |                
                      |__/                
                      ''')
print(blackjack)
print("***************************************")
print("Welcome to Blackjack")
print("There are the initial cards")
print("This game is based on only one Deck")
print("***************************************\n")

# Player initial hand
player_cards=user_onedeck()
card_remove(player_cards)
print(f"Your cards: {player_cards}")
random.shuffle(cards) 

# Dealer initial hand    
dealer_cards=computer_onedeck()
card_remove(dealer_cards)
print(f"Computer's first card: {dealer_cards}")


# Drawing cards from the same deck  
while True:
    
    #Either y or n
    get_another_card=input("Type y to \"HIT\", type n to \"STAY\": ").strip().lower()
    while get_another_card not in ("y","n"):
        print("Invalid choice")
        get_another_card=input("y or n: ")
        
    print("\n")
    # if deck got emptied, game over
    if cards==[]:
        print("No cards in deck. Thanks and till next time")
        break
    
    
    if get_another_card=="y":
        #Draw card for the player
        a_list=[]
        num=random.choice(cards) 
        a_list.append(num)    
        card_remove(a_list)
        player_cards.extend(a_list) 
        
    
    if sum(dealer_cards)<17:
        #draw card for the dealer if hand is less than 17
        b_list=[]
        num2=random.choice(cards) 
        b_list.append(num2)
        card_remove(b_list)
        dealer_cards.extend(b_list)
    
    # Check if game ends
    player_total = ace_adjustment(sum(player_cards), player_cards)
    dealer_total = ace_adjustment(sum(dealer_cards), dealer_cards)
    
    # shows what is you hand and dealer's hand
    print(f"Your current hand: {player_cards}")    
    print(f"Dealer's current hand: {dealer_cards}")    

    if player_total == dealer_total and player_total>=17 and dealer_total>=17:
        print("Push: Game draws.")
        break    
    elif player_total == 21:
        print("You win: BLACKJACK!")
        break
    elif dealer_total == 21:
        print("Dealer wins: BLACKJACK!")
        break
    elif player_total > 21:
        print("You bust! Dealer wins.")
        break
    elif dealer_total > 21:
        print("Dealer busts! You win.")
        break
    elif dealer_total >= 17 and player_total < 17:
        print("Dealer wins.")
        break
print("\n")    
input("press any key to exit...")


    


    
    
    
    
    
    
    
