# -*- coding: utf-8 -*-
"""
Created on Thu Dec  4 22:54:01 2025

@author: toora
"""
# =============================================================================
# importing module
# =============================================================================
from os import system
from blind_bid_module import highest_bidder

gavel=(r'''
               .__
              /~=\X~=\,
              Y)=_,~\=J7\,
              .+  `~=\_`~D
            .W'       :*+!
            @ ~\=_,   |,
           |!     `~=\_K
           @           P
          :!          |'
          Z           #W~\=_,
          5\=_,      |#P    `~=\_
          \,  `~=\_  @ ~\=_,     ~\=_,
        ._/!       ~8!     `~=\_     `~=\_
        | ~\=_,   //'           ~\=_,     ~\=_, _
        YG=\_ `~=\W,                `~=\_     `V ~\=_,
         `~=_~~==_,P                     ~\=_, |     `~=\_
             ~~\==/'                         `V_          ~\=,
  |XXXXXXXXXXXXXXXXXXXX8                        ~\=_,       |W
 P~~~~~~~~~~~~~~~~~~~~~~~V                          `~\=_, .*W
 ~V********************M~~                               `~+~M
r=+*********************==q
|                         |
K~T~T~T~T~T~T~T~T~T~T~T~T~T
---------------------------

''')

print(gavel)
print("Welcome to the blind bid")

# =============================================================================
# while looping with constant updating the library
# =============================================================================
main_dictionary={}
while True:
    
    a=str(input("Please enter the Bidders name: "))  
    
    while True: #to ensure user just type the integer
        try:
            b = int(input("Please enter the price? $ "))
            break
        except ValueError:
            print("Invalid. Please write the dollar amount.")
# =============================================================================
# print gavel again
# =============================================================================
    main_dictionary[a]=b
    system("cls")
    prompt=input("Are there more bidders? y or n: ").lower()
    print(gavel)
    while prompt not in ("y" ,"n"): # to ensure user dont break the program
        print("invalid choice")
        prompt=input("Please type y or n: ").lower()
        
    if prompt=="n":
        break

# =============================================================================
# calling the function
# =============================================================================
highest_bidder(main_dictionary) #import the custom made module





            
