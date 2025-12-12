# -*- coding: utf-8 -*-
"""
Created on Thu Dec 11 22:18:36 2025

@author: toora
"""


# =============================================================================
# custom functions
# =============================================================================
def ask_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.\n")

def ask_coins():
    """ These numbers goes in ask_numbers, cuz we dont want that
    user inputs anything other than numbers"""
    
    q = ask_number("How many quarters?: ")
    d = ask_number("How many dimes?: ")
    n = ask_number("How many nickels?: ")
    p = ask_number("How many pennies?: ")

    total = q * 0.25 + d * 0.10 + n * 0.05 + p * 0.01
    return total

def rest_money(a,b):
    """ a would be aed amount while b is the b
    of the drink"""
    
    if a<b:
        return("Sorry that's not enough money. Money refunded\n")
    elif a==b:
        return("Here is your drink")
    elif a>b:
        rest=a-b
        return(f"Here is your change:{rest: .2f}\n")
    
# =============================================================================
# import modules
# =============================================================================
from Menu_resources import MENU, resources
from pictures import logo, capi, espr, lat 

print(logo)
# =============================================================================
# The whole program in loop till turn off command
# =============================================================================
while True:
    
    # components from resources
    w_r=resources["water"]
    m_r=resources["milk"]
    c_r=resources["coffee"]
    
    # choice in loop
    choice=input("What would you like? (Espresso/Latte/Cappuccino): ").strip().lower()
    while choice not in ("espresso", "latte", "cappuccino", "report"):
        print("Invalid choice")
        choice=input("Please write correctly. (Espresso/Latte/Cappuccino): ").strip().lower()
     
    # check for resources as report    
    if choice=="report":
        for key in resources:
            a=resources[key]
            print(f"{key}: {a}ml")
    
    # conditional code if espresso got selected
    elif choice=="espresso":
        
        ing=MENU[choice]["ingredients"]
        w_i=ing["water"]
        m_i=ing["milk"]
        c_i=ing["coffee"]
        
        #updating and checkinf if resources available
        if w_r>w_i and c_r>c_i:
            resources["water"]=w_r-w_i
            resources["coffee"]=c_r-c_i
            
        else:
            turnoff=input("Please fill up the machine for further use")
            while turnoff!="turn off":
                turnoff=input("Worker is there?")
            break
        
        # Asking for money
        print("\n")
        cost=MENU[choice]["cost"]
        print(f"The price for a drink is: {cost}$")
        print("Please insert the coins")  
        insert=ask_coins()
        print(rest_money(insert, cost))
        print(espr)
        
   
    elif choice=="latte":
        
        ing=MENU[choice]["ingredients"]      
        w_i=ing["water"]
        m_i=ing["milk"]
        c_i=ing["coffee"]
        
        if w_r>w_i and m_r>m_i and c_r>c_i:
            resources["water"]=w_r-w_i
            resources["milk"]=m_r-m_i
            resources["coffee"]=c_r-c_i
            
        else:
            turnoff=input("Please fill up the machine for further use")
            while turnoff!="turn off":
                turnoff=input("Worker is there?")
            break
        
        print("\n")
        cost=MENU[choice]["cost"]
        print(f"The price for a drink is: {cost}$")
        print("Please insert the coins")  
        insert=ask_coins()
        print(rest_money(insert, cost))
        print(lat)
  
            
    elif choice=="cappuccino":
        
        ing=MENU[choice]["ingredients"]      
        w_i=ing["water"]
        m_i=ing["milk"]
        c_i=ing["coffee"]
        
        if w_r>w_i and m_r>m_i and c_r>c_i:
            resources["water"]=w_r-w_i
            resources["milk"]=m_r-m_i
            resources["coffee"]=c_r-c_i
        
        else:
            turnoff=input("Please fill up the machine for further use")
            while turnoff!="turn off":
                turnoff=input("Worker is there?")
            break
        
        print("\n")
        cost=MENU[choice]["cost"]
        print(f"The price for a drink is: {cost}$")
        print("Please insert the coins")  
        insert=ask_coins()     
        print(rest_money(insert, cost))
        print(capi)
            
input("press any key to exit...")
            
            

            
        
   
            
            
        

     
     





       

    
