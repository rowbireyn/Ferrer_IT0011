students = []

def show_all_records():
    if not students:
        print("No student records found.")
    else:
        for student in students:
            print(f"ID: {student[0]}, Name: {student[1][0]} {student[1][1]}, Class Standing: {student[2]}, Exam: {student[3]}")

def add_record():
    student_id = input("Enter Student ID (6 digits): ")
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    class_standing = float(input("Enter Class Standing Grade: "))
    major_exam = float(input("Enter Major Exam Grade: "))
    students.append((student_id, (first_name, last_name), class_standing, major_exam))
    print("Record added successfully.")

def show_student_record():
    student_id = input("Enter Student ID to search: ")
    for student in students:
        if student[0] == student_id:
            print(f"ID: {student[0]}, Name: {student[1][0]} {student[1][1]}, Class Standing: {student[2]}, Exam: {student[3]}")
            return
    print("Student not found.")

def edit_record():
    student_id = input("Enter Student ID to edit: ")
    for i in range(len(students)):
        if students[i][0] == student_id:
            first_name = input("Enter New First Name: ")
            last_name = input("Enter New Last Name: ")
            class_standing = float(input("Enter New Class Standing Grade: "))
            major_exam = float(input("Enter New Major Exam Grade: "))
            students[i] = (student_id, (first_name, last_name), class_standing, major_exam)
            print("Record updated.")
            return
    print("Student not found.")

def delete_record():
    student_id = input("Enter Student ID to delete: ")
    for student in students:
        if student[0] == student_id:
            students.remove(student)
            print("Record deleted.")
            return
    print("Student not found.")

while True:
    print("\nMenu:")
    print("1. Show All Records")
    print("2. Add Record")
    print("3. Show Student Record")
    print("4. Edit Record")
    print("5. Delete Record")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        show_all_records()
    elif choice == "2":
        add_record()
    elif choice == "3":
        show_student_record()
    elif choice == "4":
        edit_record()
    elif choice == "5":
        delete_record()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")