# -*- coding: utf-8 -*-
"""
Created on Fri Dec 19 03:10:44 2025

@author: toora
"""

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

print(r"""
      
__        __   _                            _       
\ \      / /__| | ___ ___  _ __ ___   ___  | |_ ___ 
 \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \
  \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) |
   \_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/
                                                    
       W E L C O M E   T O   T H E   Q U I Z   S H O W
   ☠  K N O W L E D G E   I S   A   W E A P O N  ☠️
           😈 M O S T   W I L L   F A I L .  (So do) Y O U ?  😈
       
""")

# defining list to append library of question and answers
question_bank=[]

# extracting text and answers from library in data file
for i in range (len(question_data)):
    text=question_data[i]["question"]
    ans=question_data[i]["correct_answer"]
    a=Question(text, ans)
    question_bank.append(a)
    i+=1
  
# sending data to quiz_brain file for durther processing    
quiz= QuizBrain(question_bank)

# looping till all the questions are asked
while quiz.still_has_question():
    quiz.next_question()

# quiz ended
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
print()
input("press any key to exit...")
