#!/bin/python3

import os
import sys

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):

    new_grade = list(range(len(grades)))
    print(len(grades))
    for x in range(len(grades)):
        i = 0
        temp_grade = 0
        if (grades[x] < 38):
            new_grade[x] = grades[x]
        else:    
            while (grades[x]+i) % 5 != 0:
                i += 1
            temp_grade = grades[x]+i    
            if (temp_grade - grades[x] < 3):
                new_grade[x] = temp_grade
            elif (temp_grade - grades[x] == 3):
                new_grade[x] = grades[x]
            else:
                new_grade[x] = grades[x]
    return new_grade

n = int(input())

grades = []

for _ in range(n):
    grades_item = int(input())
    grades.append(grades_item)

result = gradingStudents(grades)
print(result)
