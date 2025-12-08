# -*- coding: utf-8 -*-
"""
Created on Mon Dec  8 14:38:19 2025

@author: toora
"""

def prime_number(a):
    """ Prime bumber checker"""
    if a==1:
        return False
    elif a==2:
        return True
    
    for i in range(2, a):
        if a%i==0:
            return False
        

    return True

while True:
    try:
        number=int(input("Type a number: "))
        break
    except ValueError:
        print("Please type the number only")
        
print(prime_number(number))      
input("Pess any key to exit...")