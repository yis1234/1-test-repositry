"""Student's average mark
Shows the average mark, highest mark and grades
Sun Woo Yi
07/02/22
"""
highest_name = []
info = []
student_name = ""
total = 0
number = 0
grade = ""


def grade_evaluator(mark):
    if mark >= 90:
        grade = "A+"
    elif 85 <= mark <= 89:
        grade = "A"
    elif 80 <= mark <= 84:
        grade = "A-"
    elif 75 <= mark <= 79:
        grade = "B+"
    elif 70 <= mark <= 74:
        grade = "B"
    elif 65 <= mark <= 69:
        grade = "B-"
    elif 60 <= mark <= 64:
        grade = "C+"
    elif 55 <= mark <= 59:
        grade = "C"
    elif 50 <= mark <= 54:
        grade = "C-"
    elif 40 <= mark <= 49:
        grade = "D"
    elif 0 <= mark <= 39:
        grade = "E"
    return grade


student_name = input("What is the name of the student "
                     "(press x if you want to quit): ").upper()
student_mark = int(input("What is the mark of the student (0-100): "))
student_grade = grade_evaluator(student_mark)
info.append([student_name, student_mark, student_grade])
highest_mark = student_mark
highest_name.append(student_name)
total += student_mark
number += 1
while student_name != "X":
    student_name = input("What is the name of the student "
                         "(press x if you want to quit): ").upper()
    if student_name == "X":
        break
    student_mark = int(input("What is the mark of the student (0-100): "))
    student_grade = grade_evaluator(student_mark)
    info.append([student_name, student_mark, student_grade])
    if student_mark > highest_mark:
        highest_mark = student_mark
        highest_name.clear()
        highest_name.append(student_name)
    elif student_mark == highest_mark:
        highest_name.append(student_name)
    total += student_mark
    number += 1
average = total / number
for i in highest_name:
    print("Highest mark: ", i, ": ", highest_mark)
print("Average mark: " f"{average:.1f}")
for i in info:
    print(i)
