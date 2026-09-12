# Student Performance Tracker - first ever project road to AI Engineering IA

# ===============================
# 1. Student Data 
# ===============================
students = [
    {
        "name": "Mohammed",
        "age": 20,
        "subjects": "Math",
        "marks": 90
    },
    {
        "name": "Ali",
        "age": 22,
        "subjects": "Science",
        "marks": 85
    },
    {
        "name": "Sakina",
        "age": 21,
        "subjects": "English",
        "marks": 95
    }



]

def calculate_average_marks(students):
    total_marks = 0
    for student in students:
        total_marks += student['marks']
    average_marks = total_marks / len(students)
    return average_marks

 




def find_top_student(students):
    top_student = students[0]
    for student in students:
        if student['marks'] > top_student['marks']:
            top_student = student
    return top_student

 


def get_grade(mark):
    if mark >= 85:
        return "A"
    elif mark >= 70:
        return "B"
    elif mark >= 60:
        return "C"
    elif mark >= 50:
        return "D"
    else:
        return "F"
 


def add_student(students, name, age, subjects, marks):
    new_student = {
        "name": name,
        "age": age,
        "subjects": subjects,
        "marks": marks
    }
    students.append(new_student)

  

# =========================
# Menu / User Interface 
# =========================

while True: 
    print(" ============ Student Performance Tracker ============")

    print("1. Display all students")
    print("2. Add student")
    print("3. Calculate average")
    print("4. Find top student")
    print("5. Search student")
    print("6. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        for student in students:
            print(f"Name: {student['name']}, Age: {student['age']}, Subjects: {student['subjects']}, Marks: {student['marks']}")

    elif choice == "2":
        name = input("Enter student name: ")
        age = input("Enter student age: ")
        try:
            age = int(age)
        except ValueError:
            print("Invalid age. Please enter a valid integer.")
            continue
        if age < 0:
            print("Age cannot be negative. Please enter a valid age.")
            continue
        subjects = input("Enter student subjects: ")
        if not subjects.strip():
            print("Subjects cannot be empty. Please enter valid subjects.")
            continue
        if not subjects.replace(" ", "").isalpha():
            print("Subjects should only contain letters and spaces. Please enter valid subjects.")
            continue
        marks = input("Enter student marks: ")
        try:
            marks = int(marks)
        except ValueError:
            print("Invalid marks. Please enter a valid integer.")
            continue
        if marks < 0 or marks > 100:
            print("Marks should be between 0 and 100. Please enter valid marks.")
            continue
        add_student(students, name, age, subjects, marks)
        print(f"Student {name} added successfully.")
    elif choice == "3":
        average = calculate_average_marks(students)
        print(f"Average Marks: {average}")
    elif choice == "4":
        top_student = find_top_student(students)
        print(f"Top Student: {top_student['name']}, Marks: {top_student['marks']}")
    elif choice == "5":
        name = input("Enter student name to search: ")
        print(f"You entered: '{name}'")
        for student in students:
            if student['name'] == name:
                print(f"Name: {student['name']}, Age: {student['age']}, Subjects: {student['subjects']}, Marks: {student['marks']}")
                break
        else:
            print("Student not found.")
    elif choice == "6":
        print("Feature coming soon. Exiting the program.")
        break

