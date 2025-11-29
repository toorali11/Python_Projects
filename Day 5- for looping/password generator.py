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
letters = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
    'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
]

numbers = ['0','1','2','3','4','5','6','7','8','9']

symbols = [
    '!','@','#','$','%','^','&','*','(',')',
    '-','_','=','+','[',']','{','}',';',':',
    ',', '.', '<','>','?','/','\\','|','~'
]

print(len(symbols))
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

a=int(input("How many letters would you like in your password?"))
b=int(input("How many numbers would you like in your password?"))
c=int(input("How many symbols would you like in your password?"))

# =============================================================================
# Condition without while loop
# =============================================================================
if  a>(len(letters)):
        a=int(input("The range is 0-52 for letters: "))
        
elif b>(len(numbers)):
    b=int(input("The range is 0-10 for numbers: ")) 

elif c>(len(symbols)):
    b=int(input("The range is 0-29 for symbol: "))        
         
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