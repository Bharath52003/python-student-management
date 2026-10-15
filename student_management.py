
students = []

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        age = input("Enter student age: ")

        students.append({
            "id": student_id,
            "name": name,
            "age": age
        })

        print("Student added successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No students found.")
        else:
            for student in students:
                print(student)

    elif choice == "3":
        student_id = input("Enter student ID to search: ")

        for student in students:
            if student["id"] == student_id:
                print("Student found:", student)
                break
        else:
            print("Student not found.")

    elif choice == "4":
        student_id = input("Enter student ID to delete: ")

        for student in students:
            if student["id"] == student_id:
                students.remove(student)
                print("Student deleted successfully!")
                break
        else:
            print("Student not found.")

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Try again.")
