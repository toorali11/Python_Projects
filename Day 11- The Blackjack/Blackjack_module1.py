# -*- coding: utf-8 -*-
"""
Created on Sun Dec  7 01:48:29 2025

@author: toora
"""
import random
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10] #deck of cards
random.shuffle(cards)

def user_onedeck():
    a=random.choice(cards)
    b=random.choice(cards)
    while a==b:
        b=random.choice(cards)
    return [a,b]

def computer_onedeck():
    a=random.choice(cards)
    return [a]

def card_remove(a):
    for card in a:
        if card in cards:
            cards.remove(card)    
            
def ace_adjustment(hand_total, hand):
    # Adjusts Ace from 11 to 1 if the total exceeds 21
    while hand_total > 21 and 11 in hand:
        hand_total -= 10
        hand[hand.index(11)] = 1  # Change Ace from 11 to 1
    return hand_total

    