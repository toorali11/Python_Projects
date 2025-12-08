# -*- coding: utf-8 -*-
"""
Created on Sun Dec  7 22:59:37 2025

@author: toora
"""
# Import module
import random

#Intro
print(r'''
      
 _   _                       _                       _____                      
| \ | |                     | |                    / ____|                     
|  \| | ___  _   _ _ __ ___ | |__   ___ _ __ ___  | |  __ _   _  ___  ___ ___  
| . ` |/ _ \| | | | '_ ` _ \| '_ \ / _ \ '__/ _ \ | | |_ | | | |/ _ \/ __/ __| 
| |\  | (_) | |_| | | | | | | |_) |  __/ | |  __/ | |__| | |_| |  __/\__ \__ \ 
|_| \_|\___/ \__,_|_| |_| |_|_.__/ \___|_|  \___|  \_____|\__,_|\___||___/___/ 
                                                                               
                  +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
                  | N U M B E R   G U E S S I N G |
                  +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

                 Guess the secret number (if you dare!)

                        ┌─────────────────────┐
                        │    [   ???   ]      │
                        └─────────────────────┘
                               ^   ^   ^
                               |   |   |
                   The number is hiding in here…
                   
                  GitHub: https://github.com/toorali11         

''')

print("I am thinkng a number from 0 to 100")
# Global variables
number=random.randint(1, 100)
difficulty=input("Choose a difficulty: Type Easy or Hard? ").strip().lower()

# Ensuring the user input
while difficulty not in ("easy","hard"):
    print("Invalid command")
    difficulty=input("please type Easy or Hard: ").strip().lower()

# defining number of atempts
if difficulty=="easy":
    attempts=10
    
elif difficulty=="hard":
    attempts=5   
    
# definig function

def winning_conditions(a,b):
    """a is guessed number, b is random number, c is attempts"""
    
    if a==b:
        return "You win, guessed correctly"
    
    elif a in range (b+1, b+6):
        return"Just a bit high. You are close"
    
    elif a in range (b-6, b): 
        return "Just a bit low. You are close"
        
    elif a in range (b+6, b+12):
        return "Too High"
    
    elif a in range (b-12, b-6):
        return "Too High"
        
    else:
        return("keep guessing") 
    
while True:
    print("\n") 
    
    while True:
        try:
            guess=int(input("Make a guess: "))
            break
        except ValueError:
            print("please write a number")
            
    attempts-=1
    print(f"you have {attempts} attempts left")
    result=winning_conditions(guess, number)
    print(result)
       
    if result=="You win, guessed correctly":
        break
    
    elif attempts==0:
        print("you are out of attempts")
        print(f"The number was {number}")
        break
        

print("\n")    
input("press any key to exit...")
    
    
  