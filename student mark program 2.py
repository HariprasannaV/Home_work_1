"""
######### Problem 1.1
#same problem as above, but output should have the student name and all the marks in the same line.
# Eg - Input - Student Name - Chitra, Mark1 1 55, Mark 2 67
#output -  Chitra's marks 55, 67
"""
# Loop over each student in the range 1 to 3
for student in range(1, 4):
    # Get the name of the current student from the user
    student_name = input(f"Enter name of student {student}: ")
    # Create an empty list to store the marks for the current student
    marks = []
    # Loop over each mark in the range 1 to 2
    for mark in range(1, 3):
        # Get the mark for the current student and mark from the user
        input_mark = float(input(f"Enter mark {mark} for {student_name}: "))
        # Add the mark to the list of marks for the current student
        marks.append(input_mark)
    # Print the marks for the current student
    print(f"{student_name}'s marks {marks[0]}, {marks[1]}")
