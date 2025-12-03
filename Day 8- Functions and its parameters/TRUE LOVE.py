# -*- coding: utf-8 -*-
"""
Created on Wed Dec  3 17:57:07 2025

@author: toora
"""


def calculate_love_score(name1, name2):
    print("Welcome to the TRUE LOVE calculator")
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
    print(i+j)
            
    
calculate_love_score("Kanye West", "Kim Kardashian")  