# ============================================================
#           STUDENT ATTENDANCE MANAGEMENT SYSTEM
# ============================================================


# ============================================================
# STUDENT CLASS
# ============================================================

class Student:

    def __init__(
        self,
        student_id,
        name,
        roll_no,
        age,
        standard,
        section,
        gender,
        parentsphone
    ):

        self.student_id = student_id
        self.name = name
        self.roll_no = roll_no
        self.age = age
        self.standard = standard
        self.section = section
        self.gender = gender
        self.parentsphone = parentsphone

        # Stores attendance of each class
        # Example:
        # ["Present", "Absent", "Present"]
        self.attendance = []

    # --------------------------------------------------------
    # ADD PRESENT
    # --------------------------------------------------------

    def mark_present(self):

        self.attendance.append("Present")

    # --------------------------------------------------------
    # ADD ABSENT
    # --------------------------------------------------------

    def mark_absent(self):

        self.attendance.append("Absent")

    # --------------------------------------------------------
    # TOTAL CLASSES
    # --------------------------------------------------------

    def total_classes(self):

        return len(self.attendance)

    # --------------------------------------------------------
    # PRESENT CLASSES
    # --------------------------------------------------------

    def present_classes(self):

        return self.attendance.count("Present")

    # --------------------------------------------------------
    # ABSENT CLASSES
    # --------------------------------------------------------

    def absent_classes(self):

        return self.attendance.count("Absent")

    # --------------------------------------------------------
    # ATTENDANCE PERCENTAGE
    # --------------------------------------------------------

    def attendance_percentage(self):

        total = self.total_classes()

        if total == 0:

            return 0.0

        present = self.present_classes()

        return (present / total) * 100

    # --------------------------------------------------------
    # DISPLAY STUDENT DETAILS
    # --------------------------------------------------------

    def display_details(self):

        print("\n")
        print("==================================================")
        print("                 STUDENT DETAILS")
        print("==================================================")

        print("Student ID       :", self.student_id)
        print("Name             :", self.name)
        print("Roll No          :", self.roll_no)
        print("Age              :", self.age)
        print("Standard         :", self.standard)
        print("Section          :", self.section)
        print("Gender           :", self.gender)
        print("Parent Phone     :", self.parentsphone)

        print("\n---------------- ATTENDANCE ----------------")

        if self.total_classes() == 0:

            print("No classes have been added yet.")

        else:

            for i in range(self.total_classes()):

                print(
                    "Class",
                    i + 1,
                    ":",
                    self.attendance[i]
                )

        print("\n--------------------------------------------------")

        print(
            "Total Classes       :",
            self.total_classes()
        )

        print(
            "Present Classes     :",
            self.present_classes()
        )

        print(
            "Absent Classes      :",
            self.absent_classes()
        )

        print(
            "Attendance          :",
            f"{self.attendance_percentage():.2f}%"
        )

        print("==================================================")


# ============================================================
# ATTENDANCE SYSTEM CLASS
# ============================================================

class AttendanceSystem:

    def __init__(self, students):

        self.students = students

    # --------------------------------------------------------
    # SEARCH STUDENT
    # --------------------------------------------------------

    def search_student(self, student_id):

        for student in self.students:

            if student.student_id.upper() == student_id.upper():

                return student

        return None

    # --------------------------------------------------------
    # VIEW STUDENT DETAILS
    # --------------------------------------------------------

    def view_student(self):

        print("\n")
        print("==================================================")
        print("               VIEW STUDENT DETAILS")
        print("==================================================")

        student_id = input(
            "Enter Student ID: "
        ).strip()

        student = self.search_student(student_id)

        if student is None:

            print("\nStudent not found!")

            return

        # Display student information
        student.display_details()

    # --------------------------------------------------------
    # ADD ATTENDANCE
    # --------------------------------------------------------

    def add_attendance(self):

        print("\n")
        print("==================================================")
        print("                  ADD ATTENDANCE")
        print("==================================================")

        student_id = input(
            "Enter Student ID: "
        ).strip()

        student = self.search_student(student_id)

        if student is None:

            print("\nStudent not found!")

            return

        print("\nStudent Name:", student.name)

        print(
            "Current Attendance:",
            f"{student.attendance_percentage():.2f}%"
        )

        print(
            "Classes Already Added:",
            student.total_classes()
        )

        try:

            number_of_classes = int(
                input(
                    "\nHow many classes do you want to add? "
                )
            )

        except ValueError:

            print("\nPlease enter a valid number.")

            return

        if number_of_classes <= 0:

            print("\nNumber of classes must be greater than 0.")

            return

        # Add each class
        for i in range(number_of_classes):

            class_number = student.total_classes() + 1

            print(
                f"\nClass {class_number}"
            )

            while True:

                choice = input(
                    "Enter P for Present or A for Absent: "
                ).strip().upper()

                if choice == "P":

                    student.mark_present()

                    print("Present marked.")

                    break

                elif choice == "A":

                    student.mark_absent()

                    print("Absent marked.")

                    break

                else:

                    print(
                        "Invalid choice!"
                    )

                    print(
                        "Please enter P or A."
                    )

        # Show updated percentage
        print("\n")
        print("Attendance added successfully!")

        print(
            "Total Classes:",
            student.total_classes()
        )

        print(
            "Present Classes:",
            student.present_classes()
        )

        print(
            "Absent Classes:",
            student.absent_classes()
        )

        print(
            "Attendance Percentage:",
            f"{student.attendance_percentage():.2f}%"
        )

    # --------------------------------------------------------
    # ADD NEW STUDENT
    # --------------------------------------------------------

    def add_student(self):

        print("\n")
        print("==================================================")
        print("                  ADD NEW STUDENT")
        print("==================================================")

        student_id = input(
            "Enter Student ID: "
        ).strip()

        # Check duplicate student ID
        if self.search_student(student_id) is not None:

            print(
                "\nThis Student ID already exists!"
            )

            return

        name = input(
            "Enter Name: "
        ).strip()

        roll_no = input(
            "Enter Roll No: "
        ).strip()

        try:

            age = int(
                input("Enter Age: ")
            )

        except ValueError:

            print(
                "\nAge must be a number."
            )

            return

        standard = input(
            "Enter Standard: "
        ).strip()

        section = input(
            "Enter Section: "
        ).strip()

        gender = input(
            "Enter Gender: "
        ).strip()

        parentsphone = input(
            "Enter Parent Phone: "
        ).strip()

        new_student = Student(
            student_id,
            name,
            roll_no,
            age,
            standard,
            section,
            gender,
            parentsphone
        )

        self.students.append(new_student)

        print("\nStudent added successfully!")

        print(
            "Student ID:",
            new_student.student_id
        )

        print(
            "Name:",
            new_student.name
        )

    # --------------------------------------------------------
    # SHOW ALL STUDENTS
    # --------------------------------------------------------

    def show_all_students(self):

        print("\n")
        print("==================================================")
        print("                  ALL STUDENTS")
        print("==================================================")

        print(
            "ID       Name            Roll No      Attendance"
        )

        print(
            "--------------------------------------------------"
        )

        for student in self.students:

            print(
                f"{student.student_id:<8}"
                f"{student.name:<16}"
                f"{student.roll_no:<13}"
                f"{student.attendance_percentage():.2f}%"
            )

        print(
            "=================================================="
        )


# ============================================================
# CREATE 40 STUDENTS
# ============================================================

student1 = Student(
    "S001", "Rahul", "R001", 15,
    "10th", "A", "Male", "9876543201"
)

student2 = Student(
    "S002", "Priya", "R002", 15,
    "10th", "A", "Female", "9876543202"
)

student3 = Student(
    "S003", "Arjun", "R003", 16,
    "10th", "A", "Male", "9876543203"
)

student4 = Student(
    "S004", "Sneha", "R004", 15,
    "10th", "A", "Female", "9876543204"
)

student5 = Student(
    "S005", "Kiran", "R005", 16,
    "10th", "A", "Male", "9876543205"
)

student6 = Student(
    "S006", "Anjali", "R006", 15,
    "10th", "A", "Female", "9876543206"
)

student7 = Student(
    "S007", "Vikram", "R007", 16,
    "10th", "A", "Male", "9876543207"
)

student8 = Student(
    "S008", "Pooja", "R008", 15,
    "10th", "A", "Female", "9876543208"
)

student9 = Student(
    "S009", "Ravi", "R009", 16,
    "10th", "A", "Male", "9876543209"
)

student10 = Student(
    "S010", "Divya", "R010", 15,
    "10th", "A", "Female", "9876543210"
)

student11 = Student(
    "S011", "Manoj", "R011", 16,
    "10th", "B", "Male", "9876543211"
)

student12 = Student(
    "S012", "Kavya", "R012", 15,
    "10th", "B", "Female", "9876543212"
)

student13 = Student(
    "S013", "Rohit", "R013", 16,
    "10th", "B", "Male", "9876543213"
)

student14 = Student(
    "S014", "Sowmya", "R014", 15,
    "10th", "B", "Female", "9876543214"
)

student15 = Student(
    "S015", "Ajay", "R015", 16,
    "10th", "B", "Male", "9876543215"
)

student16 = Student(
    "S016", "Lakshmi", "R016", 15,
    "10th", "B", "Female", "9876543216"
)

student17 = Student(
    "S017", "Sandeep", "R017", 16,
    "10th", "B", "Male", "9876543217"
)

student18 = Student(
    "S018", "Keerthi", "R018", 15,
    "10th", "B", "Female", "9876543218"
)

student19 = Student(
    "S019", "Naveen", "R019", 16,
    "10th", "B", "Male", "9876543219"
)

student20 = Student(
    "S020", "Harika", "R020", 15,
    "10th", "B", "Female", "9876543220"
)

student21 = Student(
    "S021", "Varun", "R021", 16,
    "10th", "C", "Male", "9876543221"
)

student22 = Student(
    "S022", "Swathi", "R022", 15,
    "10th", "C", "Female", "9876543222"
)

student23 = Student(
    "S023", "Karthik", "R023", 16,
    "10th", "C", "Male", "9876543223"
)

student24 = Student(
    "S024", "Deepa", "R024", 15,
    "10th", "C", "Female", "9876543224"
)

student25 = Student(
    "S025", "Praveen", "R025", 16,
    "10th", "C", "Male", "9876543225"
)

student26 = Student(
    "S026", "Neha", "R026", 15,
    "10th", "C", "Female", "9876543226"
)

student27 = Student(
    "S027", "Tarun", "R027", 16,
    "10th", "C", "Male", "9876543227"
)

student28 = Student(
    "S028", "Meena", "R028", 15,
    "10th", "C", "Female", "9876543228"
)

student29 = Student(
    "S029", "Surya", "R029", 16,
    "10th", "C", "Male", "9876543229"
)

student30 = Student(
    "S030", "Bhavya", "R030", 15,
    "10th", "C", "Female", "9876543230"
)

student31 = Student(
    "S031", "Vamsi", "R031", 16,
    "10th", "D", "Male", "9876543231"
)

student32 = Student(
    "S032", "Anusha", "R032", 15,
    "10th", "D", "Female", "9876543232"
)

student33 = Student(
    "S033", "Rakesh", "R033", 16,
    "10th", "D", "Male", "9876543233"
)

student34 = Student(
    "S034", "Aishwarya", "R034", 15,
    "10th", "D", "Female", "9876543234"
)

student35 = Student(
    "S035", "Chandan", "R035", 16,
    "10th", "D", "Male", "9876543235"
)

student36 = Student(
    "S036", "Bhargavi", "R036", 15,
    "10th", "D", "Female", "9876543236"
)

student37 = Student(
    "S037", "Sai", "R037", 16,
    "10th", "D", "Male", "9876543237"
)

student38 = Student(
    "S038", "Tejaswini", "R038", 15,
    "10th", "D", "Female", "9876543238"
)

student39 = Student(
    "S039", "Abhishek", "R039", 16,
    "10th", "D", "Male", "9876543239"
)

student40 = Student(
    "S040", "Deepika", "R040", 15,
    "10th", "D", "Female", "9876543240"
)


# ============================================================
# STORE ALL 40 STUDENTS
# ============================================================

students = [

    student1,
    student2,
    student3,
    student4,
    student5,
    student6,
    student7,
    student8,
    student9,
    student10,

    student11,
    student12,
    student13,
    student14,
    student15,
    student16,
    student17,
    student18,
    student19,
    student20,

    student21,
    student22,
    student23,
    student24,
    student25,
    student26,
    student27,
    student28,
    student29,
    student30,

    student31,
    student32,
    student33,
    student34,
    student35,
    student36,
    student37,
    student38,
    student39,
    student40

]


# ============================================================
# CREATE ATTENDANCE SYSTEM
# ============================================================

system = AttendanceSystem(students)


# ============================================================
# MAIN MENU
# ============================================================

while True:

    print("\n\n")
    print("==================================================")
    print("          STUDENT ATTENDANCE SYSTEM")
    print("==================================================")

    print("1. View Student Details")
    print("2. Add Attendance")
    print("3. Add New Student")
    print("4. Show All Students")
    print("5. Exit")

    print("==================================================")

    choice = input(
        "Enter your choice: "
    ).strip()

    # --------------------------------------------------------
    # CHOICE 1
    # --------------------------------------------------------

    if choice == "1":

        system.view_student()

    # --------------------------------------------------------
    # CHOICE 2
    # --------------------------------------------------------

    elif choice == "2":

        system.add_attendance()

    # --------------------------------------------------------
    # CHOICE 3
    # --------------------------------------------------------

    elif choice == "3":

        system.add_student()

    # --------------------------------------------------------
    # CHOICE 4
    # --------------------------------------------------------

    elif choice == "4":

        system.show_all_students()

    # --------------------------------------------------------
    # CHOICE 5
    # --------------------------------------------------------

    elif choice == "5":

        print("\nThank you for using the system!")

        break

    # --------------------------------------------------------
    # INVALID CHOICE
    # --------------------------------------------------------

    else:

        print(
            "\nInvalid choice!"
        )

        print(
            "Please enter a number from 1 to 5."
        )
