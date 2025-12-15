# -*- coding: utf-8 -*-
"""
Created on Mon Dec 15 21:10:40 2025

@author: toora
"""
# =============================================================================
# Creating coffe vending machine by using documentation only
# =============================================================================
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Asking for ingridients 
ingridients= Menu()
payment= MoneyMachine()
order= CoffeeMaker()

options= ingridients.get_items()


# This coffee machine works till turn off is written

while True:
    choice=input(f"What you would like to have? {options} ").strip().lower()
    
    if choice=="turn off":
        break
    
    elif choice=="report":
        print(order.report())
        print(payment.report())     
        
    else:
        drink= ingridients.find_drink(choice)
        if order.is_resource_sufficient(drink) and payment.make_payment(drink.cost):
            order.make_coffee(drink)
            
input("press any key to exit...")


