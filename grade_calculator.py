# insert grades
student_grades = {
    "Alice": [85, 90, 78],
    "Bob": [92, 88, 95],
    "Charlie": [75, 80, 82]
}

# initate the empty dictionary to store  averages
student_averages = {}

# iterate through the student_grades dictionary to calculate the average for each student and store it in  student_averages 
for student, gradelist in student_grades.items():
    average = sum(gradelist) / len(gradelist)
    student_averages[student] = average

# initiate the dictionary to store letter grades
student_grade_letters = {}

# iterate through the student_averages dictionary and assign letter grades based on the averages
for student, average in student_averages.items():
    if average >= 90:
        student_grade_letters[student] = 'A'
    elif average >= 80:
        student_grade_letters[student] = 'B'
    elif average >= 70:
        student_grade_letters[student] = 'C'
    elif average >= 60:
        student_grade_letters[student] = 'D'
    else:
        student_grade_letters[student] = 'F'

# initiate both top_student and top_average variables 
top_student = ""
top_average = 0

# iterate through student_averages dictionary to find student with the highest average
for student, average in student_averages.items():
    if average > top_average:
        top_average = average
        top_student = student

# initate the total average variable
total_average = 0

# iterate through the averages to calculate the total average of the class
for average in student_averages.values():
    total_average += average

# calculate the class average by dividing the total average by number of students
total_average /= len(student_averages)

# initiate the passing_students variable to count number of passing students
passing_students = 0

# iterate through student_grade_letters to count number of students that are passing
for letter_grade in student_grade_letters.values():
    if letter_grade == 'A' or letter_grade == 'B' or letter_grade == 'C':
        passing_students += 1

# print the results for every student
for student in student_grades:
    print(f"{student}:")
    print(f"Average: {student_averages[student]:.2f}")
    print(f"Grade: {student_grade_letters[student]}")

# print final results and create a new line to seperate final results from individual results
print("\nResults:")
print(f"Top Student: {top_student} with average: {top_average:.2f}")
print(f"Top Average: {top_average:.2f}")
print(f"Class Average: {total_average:.2f}")
print(f"Passing Students: {passing_students}")
