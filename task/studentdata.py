# create a program that get a dictory for student data from user & add 5 student data to list & check whater a student record is exist or not.

student_records = []
found = False

for i in range(5):
    student = {}
    student['name'] = input("Enter student name: ")
    student['roll_number'] = input("Enter student roll number: ")
    student['age'] = int(input("Enter student age: "))
    student_records.append(student)
    print(student)
    
# Check if a student record exists
search_roll_number = input("Enter roll number to search: ")


for student in student_records:
    if student['roll_number'] == search_roll_number:
        found = True
        print("Student found:")
        print("Name:", student['name'])
        print("Roll Number:", student['roll_number'])
        print("Age:", student['age'])
        break

if not found:
    print("Student with roll number", search_roll_number, "not found.")
