# -*- coding: utf-8 -*-
"""
Created on Sun Nov 30 12:14:32 2025

@author: toora
"""
# =============================================================================
# module import
# =============================================================================

import random

# =============================================================================
# defining wordlist
# =============================================================================

words = [
    "apple", "banana", "orange", "grape", "melon",
    "python", "java",
    "guitar", "piano", "drums", "violin", "trumpet",
    "river", "forest", "desert", "ocean",
    "castle", "village", "bridge", "harbor", "caravan",
    "battery", "charger", "monitor", "laptop",
    "dragon", "wizard", "potion", "castle", "dagger",
    "shadow", "crystal", "ember", "harvest", "whisper",
    "quantum", "gravity", "neutron", "photon",
    "victory", "mystery", "fortune",
    "circle", "diamond", "polygon", "horizon",
    "anchor", "compass", "harpoon", "lantern",
    "galaxy", "nebula", "comet"
]


random_words=random.choice(words)

# =============================================================================
# ASCII Hangingman
# =============================================================================

stages = [
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========""",
    """
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========""",
    """
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========""",
    """
      +---+
      |   |
          |
          |
          |
          |
    ========="""
]

# =============================================================================
# defining placeholder
# =============================================================================

placeholder=""
for letters in random_words:
    placeholder+=" _ "
print(placeholder)    

# =============================================================================
# for loop with condition
# =============================================================================

correct_word=[]
lives=6
while True:
    
    display=""  
    guess=input("Please type a letter: ").lower()

    for letters in random_words:
        if letters==guess:
            display+=guess
            correct_word.append(guess)
    
            
        elif letters in correct_word:
            display+=letters
            
        else:
            display+=" _ "
    
    print()
    print("\n")      # also adds one empty line     
    print(display)    
        
    if " _ " not in display:
        print("You win! Game over...")
        break

    if guess in random_words:
        print("Correct guess!")
        print(stages[lives])
    else:
        lives -= 1
        print("Wrong guess!")
        print("Lives left:", lives)
        print(stages[lives])

        if lives == 0:
            print("Game over! The word was:", random_words)
            break
        
input("Press Enter to exit...")            
    
    