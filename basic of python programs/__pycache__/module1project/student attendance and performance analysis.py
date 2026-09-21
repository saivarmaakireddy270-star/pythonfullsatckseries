class Student:

    def __init__(self, student_id, name, course):
        self.student_id = student_id
        self.name = name
        self.course = course

        self.total_classes = 0
        self.present_classes = 0
        self.marks = {}

    def mark_attendance(self, present):
        self.total_classes += 1

        if present:
            self.present_classes += 1

    def attendance_percentage(self):
        if self.total_classes == 0:
            return 0

        return (self.present_classes / self.total_classes) * 100

    def add_marks(self, subject, marks):
        self.marks[subject] = marks

    def average_marks(self):
        if len(self.marks) == 0:
            return 0

        return sum(self.marks.values()) / len(self.marks)

    def performance(self):
        average = self.average_marks()

        if average >= 80:
            return "Excellent"
        elif average >= 60:
            return "Good"
        elif average >= 40:
            return "Average"
        else:
            return "Poor"

    def display(self):

        print("\n---------- STUDENT DETAILS ----------")

        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Course:", self.course)

        print("\nAttendance")
        print("Total Classes:", self.total_classes)
        print("Present Classes:", self.present_classes)

        print(
            "Attendance Percentage:",
            round(self.attendance_percentage(), 2),
            "%"
        )

        print("\nMarks")

        if len(self.marks) == 0:
            print("No marks entered")
        else:
            for subject, marks in self.marks.items():
                print(subject, ":", marks)

        print("Average Marks:", round(self.average_marks(), 2))
        print("Performance:", self.performance())


# -----------------------------------
# MAIN PROGRAM
# -----------------------------------

students = []


def add_student():

    print("\n========== ADD STUDENT ==========")

    try:

        student_id = int(input("Enter Student ID: "))

        # Check duplicate ID
        for student in students:
            if student.student_id == student_id:
                print("Student ID already exists.")
                return

        name = input("Enter Student Name: ")
        course = input("Enter Course: ")

        student = Student(student_id, name, course)

        students.append(student)

        print("Student added successfully!")

    except ValueError:

        print("Please enter a valid Student ID.")


def find_student():

    try:
        student_id = int(input("Enter Student ID: "))

        for student in students:

            if student.student_id == student_id:
                return student

        print("Student not found.")

    except ValueError:

        print("Invalid Student ID.")

    return None


def mark_attendance():

    print("\n========== MARK ATTENDANCE ==========")

    student = find_student()

    if student is None:
        return

    choice = input("Was the student present? (Y/N): ").upper()

    if choice == "Y":

        student.mark_attendance(True)
        print("Attendance marked as PRESENT.")

    elif choice == "N":

        student.mark_attendance(False)
        print("Attendance marked as ABSENT.")

    else:

        print("Invalid choice. Enter Y or N.")


def enter_marks():

    print("\n========== ENTER MARKS ==========")

    student = find_student()

    if student is None:
        return

    subject = input("Enter Subject: ")

    try:

        marks = float(input("Enter Marks: "))

        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100.")
            return

        student.add_marks(subject, marks)

        print("Marks added successfully!")

    except ValueError:

        print("Please enter a valid number.")


def view_student():

    print("\n========== VIEW STUDENT ==========")

    student = find_student()

    if student is not None:
        student.display()


def attendance_report():

    print("\n========== ATTENDANCE REPORT ==========")

    if len(students) == 0:

        print("No students available.")
        return

    for student in students:

        print(
            "ID:", student.student_id,
            "| Name:", student.name,
            "| Attendance:",
            round(student.attendance_percentage(), 2),
            "%"
        )


def performance_report():

    print("\n========== PERFORMANCE REPORT ==========")

    if len(students) == 0:

        print("No students available.")
        return

    for student in students:

        print(
            "ID:", student.student_id,
            "| Name:", student.name,
            "| Average:",
            round(student.average_marks(), 2),
            "| Performance:",
            student.performance()
        )


# -----------------------------------
# MENU
# -----------------------------------

while True:

    print("\n========================================")
    print(" STUDENT ATTENDANCE & PERFORMANCE")
    print("========================================")

    print("1. Add Student")
    print("2. Mark Attendance")
    print("3. Enter Marks")
    print("4. View Student Details")
    print("5. Attendance Report")
    print("6. Performance Report")
    print("7. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        mark_attendance()

    elif choice == "3":
        enter_marks()

    elif choice == "4":
        view_student()

    elif choice == "5":
        attendance_report()

    elif choice == "6":
        performance_report()

    elif choice == "7":

        print("Thank you!")
        break

    else:

        print("Invalid choice. Please try again.")