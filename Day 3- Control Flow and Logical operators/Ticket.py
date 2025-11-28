# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 08:38:50 2025

@author: toora
"""
h=int(input("what's your height? "))

if h>120:
    print("Applicable age. Can ride")
    
    a=int(input("what's your age? "))
    b=0
    
    if a<12:
        b+=5
        print(f"Ticket costs {b}")
        
    elif a<18:
        b+=7
        print(f"Ticket cost {b}")
        
    elif a>=45 and a<=55:    
        b+=16
        print(f"Ticket cost {b}")      
        
    elif a>=18:    
        b+=12
        print(f"Ticket cost {b}")
         
        
    if input("you want photos? y or n: ")=="y":
        b+=3
        print(f"The bill will be {b}")
        
    else:
        print(f"The total bill will be {b}")
else:
    print("Cant ride")
