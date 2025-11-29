# -*- coding: utf-8 -*-
"""
Created on Sat Nov 29 14:18:02 2025

@author: toora
"""

# =============================================================================
# module import
# =============================================================================
import random

# =============================================================================
# Defining the lists
# =============================================================================
letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers = list("0123456789")
symbols = list("!@#$%^&*()-_=+[]{};:,.<>?/|\\~")

# =============================================================================
# Shuffling the list
# =============================================================================
random.shuffle(letters)
random.shuffle(numbers)
random.shuffle(symbols)

# =============================================================================
# implementing password generator
# =============================================================================
print("Welcome to the Password Generator")

while True:
    a = int(input(f"Please enter range for letter from 0 to {len(letters)}: "))
    if 0 <= a <= len(letters):
        break  
    
while True:
    b = int(input(f"Please enter range for numbers from 0 to {len(numbers)}: "))
    if 0 <= b <= len(numbers):
        break     

while True:
    c = int(input(f"Please enter range for symbols from 0 to {len(symbols)}: "))
    if 0 <= c <= len(symbols):
        break    
         
# =============================================================================
# for loop and list appending    
# =============================================================================
list=[]

for i in range(0,a):
    pas=letters[i]
    list.append(pas)
    
for x in range(0,b):
    passs=numbers[x]
    list.append(passs)
    
for y in range(0,c):
    passss=symbols[y]
    list.append(passss) 

password=""
for char in list:
    password+=char
  
print(f"This is your generated password: {password}")
input("Press Enter to exit...")
