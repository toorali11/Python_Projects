# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 09:17:50 2025

@author: toora
"""

print("Welcome to python pizza deliveries")
size = input("What size you wanna have? S, M or L: ")
pep = input("do we add pepperoni? y or n: ")
che= input("extra cheese? y or n: ")

price=0
if size=="S":
    price+=15

    if pep =="y":
        price+=2

    
elif size=="M":
    price+=20
    
    if pep=="y":
        price+=3

    
elif size=="L":
    price+=25
    
    if pep=="y":
        price+=3
        
if che =="y":
    price+=1

    print(f"You final bill will be {price} $ ")

