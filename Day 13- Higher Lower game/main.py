# -*- coding: utf-8 -*-
"""
Created on Thu Dec 11 01:37:21 2025

@author: toora
"""
# =============================================================================
# Asscii characters
# =============================================================================
logo = r"""
  _   _ _       _               
 | | | (_) __ _| |__   ___ _ __ 
 | |_| | |/ _` | '_ \ / _ \ '__|
 |  _  | | (_| | | | |  __/ |   
 |_| |_|_|\__, |_| |_|\___|_|   
 | |    __|___/    _____ _ __   
 | |   / _ \ \ /\ / / _ \ '__|  
 | |__| (_) \ V  V /  __/ |     
 |_____\___/ \_/\_/ \___|_|     
"""

vs = r"""
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

# =============================================================================
# import modules
# =============================================================================

from data import followers, youtube_subscribed
# from functions import random_index
import random
# =============================================================================
# Global variables
# =============================================================================
f=followers
y=youtube_subscribed
points=0

# The whole program in loop till it get broken
while True:
    
    # randomly select the data
    data_list=["fff", "yyy"]
    selected=random.choice(data_list)
    
    if selected=="fff":    
        # random index of first variable
        follower_index1=random.randint(0, len(f)-1)   
        follower_index2=random.randint(0, len(f)-1)   
        
        # ensuring both indicies were different
        while follower_index1==follower_index2:
            follower_index1=random.randint(0, len(f)-1)   
            
        # print statements
        print(logo)   
        print("Compare A:",f[follower_index1]["name"],"is", f[follower_index1]["description"],"from", f[follower_index1]["country"])
        print(vs)
        print("Against B:",f[follower_index2]["name"],"is", f[follower_index2]["description"],"from", f[follower_index2]["country"])
        
        # determining who got more followers
        a=f[follower_index1]["followers"]
        b=f[follower_index2]["followers"]
        print()
        print("Who got more followers?\n")
        
        # conditions for checking if person gets the point
        choice=input("Type A or B: ").upper()
        while choice not in ("A","B"):
            print("Invalid Choice")
            choice=input("Please type either A or B: ").upper()
            print("\n")
            
        if choice=="A" and a>b:
            print("right option")
            points+=1
            
        elif choice=="B" and b>a:
            print ("You got one point for your right answer")
            points+=1

        else:
            print("\n")
            print("Wrong answer. Game over")
            break

    else:
        # # random index of second variable
        youtube_index1=random.randint(0, len(y)-1)   
        youtube_index2=random.randint(0, len(y)-1)   
        
        while youtube_index1==youtube_index2:
            youtube_index1=random.randint(0, len(y)-1)    
        
        # print of the ui    
        print(logo)   
        print("Compare A:",y[youtube_index1]["name"],"is", y[youtube_index1]["category"],"from", y[youtube_index1]["country"])
        print(vs)
        print("Against B:",y[youtube_index2]["name"],"is", y[youtube_index2]["category"],"from", y[youtube_index2]["country"])
    
        # extracting numbers to ger compared
        a=y[youtube_index1]["subscribers_millions"]
        b=y[youtube_index2]["subscribers_millions"]
        print()
        print("Who got more subscribers?\n")
        
        # conditions for checking if person gets the point
        choice=input("Type A or B: ").upper()
        while choice not in ("A","B"):
            print("Invalid Choice")
            choice=input("Please type either A or B: ").upper()
            print("\n")
            
        if choice=="A" and a>b:
            print("right option")
            points+=1
        elif choice=="B" and b>a:
            print ("You got one point for your right answer")
            points+=1

        else:
            print("\n")
            print("Wrong answer. Game over")
            break

print("*****************************************")
# condition for correct grammer in the game.
if points<=1:
    print(f"Your final point is {points}")
else:
    print(f"Your final points are {points}")        
print("*****************************************") 
print("\n")    
input("press any key to exit...")
