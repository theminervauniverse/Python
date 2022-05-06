students_heights = input("Input a list of students height separated by a comma\n").split(",")
# print(students_heights)
for n in range(0, len(students_heights)):
    students_heights[n] = int(students_heights[n])
print(students_heights)

total_height = 0
for height in students_heights:
    total_height += height
# print(total_height)

total_students = 0
for student in students_heights:
    total_students += 1
# print(total_students)

average = round(total_height / total_students)
print(average)
