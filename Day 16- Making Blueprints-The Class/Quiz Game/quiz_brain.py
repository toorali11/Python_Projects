# -*- coding: utf-8 -*-
"""
Created on Fri Dec 19 04:20:37 2025

@author: toora
"""

class QuizBrain:
    
    def __init__(self, q_list):
        self.question_number=0
        self.question_list = q_list
        self.score=0
        
    
    def next_question(self):
        current_question=self.question_list[self.question_number]
        self.question_number+=1
        
        a= input(f"Q.{self.question_number}: {current_question.text} (True/False)? ").lower().strip()
        while a not in ("true", "false"):
            print()
            print("Invalid option")
            a=input("Please write True or False: ").strip().lower()
        
        self.check_answer(a, current_question.answer)
    
    def check_answer(self, a , current_answer):
        if a == current_answer.lower().strip():
            print("That's right answer")
            self.score+=1
            print(f"Your score is {self.score}/{self.question_number}")
            print("\n")
            
        else:
            print("Wrong answer")
            print(f"Your score is {self.score}/{self.question_number}")
            print("\n")
            
    def still_has_question(self):
        return  self.question_number < len(self.question_list)   # this works like code given below
                                                                 # becasue 5>3 is True (try in console) 
        
        # if self.question_number < len(self.question_list):
        #     return True
        # else:
        #     False
            
        