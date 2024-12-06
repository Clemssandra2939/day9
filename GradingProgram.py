# Instructions
# The keys in student_scores are the names of the students and value are their exam scores.
# Write a program that convert their score to grades,By the end of the program,
# you should have a new dictionary called student_grades tht should contain students  names for keys
# and their rades for values,the final version of the studrnt_grades dictionary will be checked.

# Scoring Citeria :
# 91-100:Grade = "Outstanding"
# 81 -90 :Grade =  "Exceeds Expectation"
# 71-80 :Grade = "Acceptable"
# 70 or lower:Grade = "Fail"

student_scores = {
"Harry":81,
"Ron": 78,
"Hermione":99,
"Draco":74,
"Neville":62,
}

# TODO-1- Create an empty dictionary called student_grades
student_grades = {}

# TODO-2- Write your code below to add the grades 

for student in student_scores:
    score = student_scores[student]
    if score > 90 :
        student_grades[student] ="Outstanding"
    elif score > 80 and  score < 90:
        student_grades[student] = "Exceeds Expectation"
    elif score > 70 and  score < 80:
        student_grades[student] =  "Acceptable"
    else:
        student_grades[student] =  "Fail"
     

print(student_grades)