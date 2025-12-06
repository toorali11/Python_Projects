# -*- coding: utf-8 -*-
"""
Created on Wed Dec  3 17:57:07 2025

@author: toora
"""


def calculate_love_score(name1, name2):
    name1=name1.upper()
    name2=name2.upper()
    i=0
    j=0
    for letters in name1+name2:
        for alphabets in "TRUE":
            if alphabets==letters:
                i+=1 
        for alphabets in "LOVE":
            if alphabets==letters:
                j+=1
    i=str(i)
    j=str(j)
    print(f"Your Lovescore is {i+j}")
    
print("Welcome to the TRUE LOVE calculator")            
a=input("Type your name: ")
b=input("Type your partner's name: ")    
calculate_love_score(a, b)  

input("press any key to exit...")