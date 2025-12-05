# -*- coding: utf-8 -*-
"""
Created on Fri Dec  5 18:24:11 2025

@author: toora
"""
def highest_bidder(bid_dictionary):
        
    number=0
    for key in bid_dictionary:
        winner=""
        s=bid_dictionary[key]
        if s>number:
            number=s
            winner=key
    print(f"The winner is {winner} with bid of {number}")