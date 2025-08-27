class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def __str__(self):
        avg = sum(self.marks) / len(self.marks)
        return f"Name: {self.name}, Roll No: {self.roll_number}, Marks: {self.marks}, Average: {avg:.2f}"


class StudentPortal:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def find_student_by_roll_number(self, roll_number):
        for student in self.students:
            if student.roll_number == roll_number:
                return student
        return None

    def display_student(self, roll_number):
        student = self.find_student_by_roll_number(roll_number)
        if student:
            print(student)
        else:
            print(f"No student found with roll number {roll_number}")


def menu(portal):
    while True:
        print("\nStudent Portal Menu")
        print("1. Display student by roll number")
        print("2. Exit")
        choice = input("Enter your choice (1-2): ")

        if choice == "1":
            roll_number = input("Enter student roll number: ")
            portal.display_student(roll_number)
        elif choice == "2":
            print("Exiting the portal.")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    portal = StudentPortal()

    # Adding 10 students at compile time
    students_data = [
        ("Alice", "001", [85, 90, 88]),
        ("Bob", "002", [75, 80, 72]),
        ("Charlie", "003", [65, 70, 68]),
        ("David", "004", [95, 92, 98]),
        ("Eve", "005", [55, 60, 58]),
        ("Frank", "006", [80, 85, 78]),
        ("Grace", "007", [70, 75, 72]),
        ("Hank", "008", [60, 65, 68]),
        ("Ivy", "009", [90, 88, 92]),
        ("Jack", "010", [50, 55, 58]),
    ]

    for name, roll_number, marks in students_data:
        portal.add_student(Student(name, roll_number, marks))

    menu(portal)
