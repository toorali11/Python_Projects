# -*- coding: utf-8 -*-
"""
Created on Fri Dec  5 22:07:01 2025

@author: toora
"""

def is_leap_year(year):
    if year % 400 == 0:
        print(f"The {year} is a leap year")
        return True
    
    elif year % 100 == 0:
        print(f"The {year} is a leap year")
        return False
    elif year % 4 == 0:
        print(f"The {year} is a leap year")
        return True
    else:
        print(f"The {year} is a not leap year")
        return False

    print(f"The {year} is a leap year")

   
is_leap_year(1700)   