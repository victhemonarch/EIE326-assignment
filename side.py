total_units = 0
total_points = 0

for i in range(6):
    course_name = input("Enter course name: ")
    grade = input("Enter grade (A-F): ").upper()
    unit = int(input("Enter course unit: "))

    if grade == 'A':
        point = 5
    elif grade == 'B':
        point = 4
    elif grade == 'C':
        point = 3
    elif grade == 'D':
        point = 2
    elif grade == 'F':
        point = 0
    else:
        point = 0

    total_units += unit
    total_points += point * unit

gpa = total_points / total_units
print("Your GPA is:", round(gpa, 2))