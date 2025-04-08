"""
Grades
Ella Chakravarty

Store students' exam grades and attendence. 

"""

#Creating sets for attendance
attendance_d1 = {'William', 'Daphne', 'Erika', 'Adam', 'Percy', 'Brock', 'Jessica', 'Trent', 'Mahmoud'}
attendance_d2 = {'Daphne', 'Alex', 'Percy', 'Mahmoud', 'Jessica', 'Adam', 'Trent', 'Caleb', 'Zayne', 'Erika'}

#How many students attended the class
students_attended = set.union(attendance_d1, attendance_d2)
num_students = len(students_attended)
#Who attended both days of class
students_attended_both = set.intersection(attendance_d1, attendance_d2)
#Who attended only one day of class
students_attended_one = attendance_d1.symmetric_difference(attendance_d2)

#Creating a list of grades
grades = [88,96,96,76,89,74,100,85,75,77,100,98]

#How many students took the exam
num_exam_students = len(grades)
#The highest grade
highest_grade = max(grades)
#The lowest grade
lowest_grade = min(grades)
#The average grade for the exam
average_grade = sum(grades) / num_exam_students

print(num_students, 'students attended the class.')
print(students_attended_both, 'attended both class days.')
print(students_attended_one, 'attended one class day.')

print(num_exam_students, 'students took the exam.')
print('The highest grade was a', highest_grade)
print('The lowest grade was a', lowest_grade)
print('The average grade for the exam was a', f'{average_grade:.1f}')
