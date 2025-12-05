# -*- coding: utf-8 -*-
"""
Created on Sun Nov 30 12:14:32 2025

@author: toora
"""
# =============================================================================
# module import
# =============================================================================

import random

print(r'''
__        __   _                            _                
\ \      / /__| | ___ ___  _ __ ___   ___  | |_ ___          
 \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \         
  \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) |        
 _ \_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/         
| | | | __ _ _ __   __ _(_)_ __   __ _ _ __ ___   __ _ _ __  
| |_| |/ _` | '_ \ / _` | | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
|  _  | (_| | | | | (_| | | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                   |___/         |___/                       ''')
print("Let´s see if you can stay alive...")
print()

# =============================================================================
# defining wordlist
# =============================================================================
easy_words = [
    "cat", "dog", "sun", "hat", "book",
    "fish", "tree", "milk", "shoe", "bird",
    "cake", "ball", "star", "rain", "frog",
    "road", "lamp", "fire", "king", "queen",
    "cup", "boat", "leaf", "wind", "moon",
    "goat", "bear", "snow", "rice", "corn",
    "blue", "duck", "chip", "bone", "ring",
    "sock", "coat", "desk", "rope", "frog",
    "farm", "gift", "rose", "wave", "door"
]

medium_words = [
    "planet", "garden", "puzzle", "castle", "bridge",
    "dragon", "forest", "wizard", "thunder", "silver",
    "monkey", "pirate", "danger", "rocket", "shadow",
    "freedom", "journey", "battery", "holiday", "victory",
    "captain", "station", "market", "teacher", "library",
    "harvest", "fiction", "machine", "lantern", "orchard",
    "weather", "pattern", "village", "picture", "plastic",
    "citizen", "message", "railway", "mission", "gravity"
]

hard_words = [
    "astronomy", "phenomenon", "labyrinth", "quarantine", "bioluminescent",
    "xylophone", "pneumonia", "cryptography", "paradoxical", "transcendent",
    "photosynthesis", "consciousness", "metamorphosis", "revolutionary",
    "uncharacteristic", "miscellaneous", "hypothesis", "architecture",
    "hallucination", "telekinesis",
    "neuroplasticity", "counterintuitive", "subterranean", "psychological",
    "cosmopolitan", "microsystem", "supranational", "chronological",
    "biotechnology", "electromagnetic", "infrastructure",
    "catastrophic", "extraordinary", "hyperactive",
    "irreversible", "philosophical", "microbiology", "institutionalize",
    "disproportionate"
]


einfach = [
    "katze", "hund", "sonne", "hut", "buch",
    "fisch", "baum", "milch", "schuh", "vogel",
    "kuchen", "ball", "stern", "regen", "frosch",
    "lampe", "feuer", "könig", "königin", "straße",
    "tasse", "boot", "blatt", "wind", "mond",
    "ziege", "bär", "schnee", "mais", "brot",
    "ente", "tisch", "stuhl", "haus", "glas",
    "seil", "rose", "welle", "tür", "wolke"
]

mittel = [
    "planet", "garten", "rätsel", "schloss", "brücke",
    "drache", "wald", "zauberer", "donner", "silber",
    "affe", "pirat", "gefahr", "rakete", "schatten",
    "freiheit", "reise", "batterie", "ferien", "sieg",
    "kapitän", "bahnhof", "markt", "lehrer", "bibliothek",
    "ernte", "geschichte", "maschine", "laterne", "obstgarten",
    "wetter", "muster", "dorf", "bild", "plastik",
    "bürger", "nachricht", "eisenbahn", "auftrag", "schwerkraft"
]

schwer = [
    "astronomie", "phänomen", "labyrinth", "quarantäne", "biolumineszenz",
    "xylophon", "pneumonie", "kryptographie", "paradox", "transzendenz",
    "fotosynthese", "bewusstsein", "metamorphose", "revolutionär",
    "uncharakteristisch", "verschiedenartig", "hypothese", "architektur",
    "halluzination", "telekinese",
    "neuroplastizität", "kontraintuitiv", "unterirdisch", "psychologie",
    "kosmopolitisch", "mikrosystem", "supranational", "chronologisch",
    "biotechnologie", "elektromagnetisch", "infrastruktur",
    "katastrophal", "außergewöhnlich", "hyperaktiv",
    "irreversibel", "philosophisch", "mikrobiologie", "institutionalisieren",
    "unverhältnismäßig"
]

english={"easy": easy_words,"medium": medium_words,"hard": hard_words}
german={"einfach": einfach,"mittel": mittel,"schwer": schwer}
language={"english": english, "german": german}

while True:  # whole menu loop

    # --- LANGUAGE CHOICE ---
    choice_language = input("Which language you wanna choose? English or German: ").lower()

    while choice_language not in ("english", "german"):
        print("Invalid language, try again.")
        choice_language = input("English or German: ").lower()

    # --- ENGLISH MODE ---
    if choice_language == "english":
        choice_difficulty = input("Which difficulty? Easy, Medium, Hard: ").lower()

        while choice_difficulty not in english:
            print("Invalid difficulty, try again.")
            choice_difficulty = input("Easy, Medium, Hard: ").lower()

        random_words = random.choice(english[choice_difficulty])

    # --- GERMAN MODE ---
    elif choice_language == "german":
        choice_difficulty = input("Bitte wählen: Einfach, Mittel oder Schwer: ").lower()

        while choice_difficulty not in german:
            print("Ungültig, bitte erneut versuchen.")
            choice_difficulty = input("Einfach, Mittel, Schwer: ").lower()

        random_words = random.choice(german[choice_difficulty])
    break


print()

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
# looping with condition
# =============================================================================

correct_word = []
wrong_guesses = []
lives = 6

while True:
    guess_word = ""
    display = ""  
    print()
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    guess = input("Please type a letter: ").lower()
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    # Track all wrong guesses
    if guess not in random_words:
        if guess not in wrong_guesses:
            wrong_guesses.append(guess)

    # Build the display word
    for letters in random_words:
        if letters == guess:
            display += " " + guess + " "
            if guess not in correct_word:
                correct_word.append(guess)

        elif letters in correct_word:
            display += " " + letters + " "

        else:
            display += " _ "

    # Show output
    print()
    print(display)    
    print()
    print("Wrong guessed letters:", " ".join(wrong_guesses))
    print()

        
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
    
    