"""
######## Problem  1 ###############
# Get and print the 2 marks each for 3 students. Also, get each student name
# output should be
# Mark 1 for Student 1 is 55
# Mark 2 for Student 1 is 67
# Mark 1 for Student 2 is 56
#etc

for student in range (#FillinMissingCode):
    #FillinMissingCode  to get student name
    for mark in range (#FillinMissingCode):
        inputMark = float (input(f"#FillinMissingCode")) #use formatted string
        print (#FillinMissingCode)
"""
# Loop over each student in the range 1 to 3
for student in range(1, 4):
    # Get the name of the current student from the user
    student_name = input(f"Enter student {student} name: ")

    # Loop over each mark in the range 1 to 2
    for mark in range(1, 3):
        # Get the mark for the current student and mark from the user
        inputMark = float(input(f"enter your mark {mark}:"))
        # Print the mark for the current student and mark
        print(f'Mark {mark} for Student {student} is {inputMark}')
