# -*- coding: utf-8 -*-
"""
Created on Fri Dec 19 02:06:57 2025

@author: toora
"""
# Understanding the basic class and how it works
class User:
    
    def __init__(self, user_id, username):
        self.id= user_id
        self.username= username
        self.followers= 0            # doesnt need to be declared cuz hard coded
        self.following= 0
        
    def follow(self, user):
        user.followers += 1
        self.following += 1
    
# calling class along with its methods
user_1=User("001", "Toor")   
user_2=User("002", "Bibchen") 

print(user_1.id)
print(user_2.id)

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print("*******************")
print(user_2.followers)
print(user_2.following)

