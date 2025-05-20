def add_student_grades():
    student_name = input("Enter student name: ")
    total_num_of_subjects = int(input("Enter total number of subjects: "))
    
    grades = {}
    for _ in range(total_num_of_subjects):
        subject = input("Enter subject name: ")
        grade = float(input(f"Enter grade for {subject}: "))
        grades[subject] = grade
    
    students[student_name] = grades
    print(f"\nGrades recorded for {student_name}.\n")


def calculate_average(grades):
    return sum(grades.values()) / len(grades) if grades else 0


def display_student_grades():
    for student, grades in students.items():
        print(f"\nStudent: {student}")
        if not grades:
            print("No grades available.")
            continue

        print("Grades:")
        for subject, grade in grades.items():
            print(f"{subject}: {grade}")

        avg = calculate_average(grades)
        print(f"\nAverage Grade: {avg:.2f}")


def main():
    while True:
        print("\n=== Student Grade Tracker ===")
        print("1. Add Student Grades")
        print("2. Display All Grades")
        print("3. Exit")
        
        choice = input("Select an option: ")
        
        if choice == "1":
            add_student_grades()
        elif choice == "2":
            display_student_grades()
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

# Global dictionary to store student data
students = {}

main()
