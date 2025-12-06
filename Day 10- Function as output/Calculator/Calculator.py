# -*- coding: utf-8 -*-
"""
Created on Sat Dec  6 16:31:13 2025

@author: toora
"""

print(r''' 
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |          
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|

''')

# =============================================================================
# Import custom module
# =============================================================================
from Calculator_module import *
# import sys

# =============================================================================
# Whole program in while loops to ensure recurring calculations
# =============================================================================
stop_programm= False
while not stop_programm:    #import sys module can be used here with while True:
    
    # =============================================================================
    # while loop to make sure user just type the numbers
    # =============================================================================
    
    while True:
        try:
            first_number=int(input("What's the first number? "))
            break
            
        except ValueError:
            print("Invalid choice")
    
    # =============================================================================
    # Print the symbols vertically        
    # =============================================================================
    
    saved_result=first_number # variable to save the results
    
    while True: 
        
        list=["+", "-", "*", "/"] 
        for i in list:
            print(i)
        
        # =============================================================================
        # while loop to select the given operators
        # =============================================================================
        
        operator=input("Pick an operation? ")
        
        while operator not in list:
            print("Invalid choice")    
            operator=input("Please chose operation again: ")
    
        result=saved_result    # variable to access saved results
        
        # =============================================================================
        # while loop to make sure user just type the numbers
        # =============================================================================   
         
        while True:
            try:
                second_number=int(input("What's the next number? "))
                break
            
            except ValueError:
                print("Invalid choice")
                
        
        # =============================================================================
        #         If conditions for operations
        # =============================================================================
        if operator=="+":
            a=addition(result, second_number)
            print()
            print(f"The result is {result}+{second_number}={a}")
            saved_result=a
            
        elif operator=="-":
            a=subtraction(result, second_number)
            print()
            print(f"The result is {result}-{second_number}={a}")
            saved_result=a
            
        elif operator=="*":
            a=multiplication(result, second_number)
            print()
            print(f"The result is {result}*{second_number}={a}")
            saved_result=a
            
        elif operator=="/":
            a=division(result, second_number)
            print()
            print(f"The result is {result}/{second_number}={a}")
            saved_result=a
            
        
        continue_calculation=input("Type y to continue with current results, type n to start a new calculation or type exit to stop: ").lower()
        while continue_calculation not in ("y","n", "exit"):
            print("Invalid choice")
            continue_calculation=input("y or n: ").lower()
            
        if continue_calculation=="y":
            pass
        
        elif continue_calculation=="n":
            break
        
        elif continue_calculation=="exit":
            stop_programm=True
            break
            # sys.exit()
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    