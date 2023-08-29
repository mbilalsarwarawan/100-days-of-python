students_scores = {"Harry": 81,
                   "Rom": 78,
                   "Herimone": 99,
                   "Draco": 64, }

students_grades = {}

for student in students_scores:

    score = students_scores[student]
    if score >= 90:
        students_grades[student] = "outstanding"
    elif score >= 80:
        students_grades[student] = "Exceeds expectation"
    elif score >= 70:
        students_grades[student] = "Aceeptable"
    else:
        students_grades[student] = "fail"

print(students_grades)
