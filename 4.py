"""Student's average mark
Shows the average mark and highest mark
Sun Woo Yi
07/02/22
"""
name = []
student_name = ""
total = 0
number = 0
student_name = input("What is the name of the student "
                     "(press x if you want to quit): ").upper()
student_mark = int(input("What is the mark of the student (0-100): "))
highest_mark = student_mark
name.append(student_name)
total += student_mark
number += 1
while student_name != "X":
    student_name = input("What is the name of the student "
                         "(press x if you want to quit): ").upper()
    if student_name == "X":
        break
    student_mark = int(input("What is the mark of the student (0-100): "))
    if student_mark > highest_mark:
        highest_mark = student_mark
        name.clear()
        name.append(student_name)
    elif student_mark == highest_mark:
        name.append(student_name)
    total += student_mark
    number += 1
average = total / number
for i in name:
    print("Highest mark: ", i, ": ", highest_mark)
print("Average mark: " f"{average:.1f}")
