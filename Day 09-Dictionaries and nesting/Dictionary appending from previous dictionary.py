# -*- coding: utf-8 -*-
"""
Created on Thu Dec  4 22:33:52 2025

@author: toora
"""

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades={}
for key in student_scores:
    if student_scores[key] >=91 and student_scores[key]<=100:
        a="Outstanding"
        student_grades[key]=a

    elif student_scores[key] >=81 and student_scores[key]<=90:
        a="Exceeds Expectations"
        student_grades[key]=a
        
    elif student_scores[key] >=71 and student_scores[key]<=80:
        a="Acceptable"
        student_grades[key]=a
    
    else:
        a="Fail"
        student_grades[key]=a
            
print(student_grades)
    
