# -*- coding: utf-8 -*-
"""
Created on Thu Dec 11 02:35:09 2025

@author: toora
"""

# =============================================================================
# this function can be used if you dont wanna use random.randint directly as
# shown in the main.py
# =============================================================================
import random

def random_index(a):
    """Append the length of libraries to list and 
    shuffle that list to return a single digit number"""
    
    list_numbers=[]
    
    for i in range (len(a)):
        list_numbers.append(i)
    return random.choice(list_numbers)
