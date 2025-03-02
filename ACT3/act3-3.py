last_name = input("Enter last name: ")
first_name = input("Enter first name: ")
age = input("Enter age: ")
contact_number = input("Enter contact number: ")
course = input("Enter course: ")

student_info = f"""
Last Name: {last_name}
First Name: {first_name}
Age: {age}
Contact Number: {contact_number}
Course: {course}
"""

with open("students.txt", "a") as file:
    file.write(student_info + "\n")

print("Student information has been saved to 'students.txt'.")