
import json
import os
from datetime import datetime


# ==========================================
# FILE NAMES
# ==========================================

USERS_FILE = "users.json"
JOBS_FILE = "jobs.json"
APPLICATIONS_FILE = "applications.json"


# ==========================================
# FILE HANDLING FUNCTIONS
# ==========================================

def load_data(filename):
    """Load data from a JSON file."""

    if not os.path.exists(filename):
        return []

    try:
        with open(filename, "r") as file:
            return json.load(file)

    except (json.JSONDecodeError, OSError):
        return []


def save_data(filename, data):
    """Save data to a JSON file."""

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


# ==========================================
# JOB PORTAL CLASS
# ==========================================

class JobPortal:

    def __init__(self):

        self.users = load_data(USERS_FILE)
        self.jobs = load_data(JOBS_FILE)
        self.applications = load_data(APPLICATIONS_FILE)

        self.initialize_admin()
        self.initialize_jobs()

    # ======================================
    # INITIAL DATA
    # ======================================

    def initialize_admin(self):

        admin_exists = any(
            user["role"] == "admin"
            for user in self.users
        )

        if not admin_exists:

            admin = {
                "user_id": "U001",
                "name": "Admin",
                "email": "admin@gmail.com",
                "password": "admin123",
                "role": "admin"
            }

            self.users.append(admin)
            save_data(USERS_FILE, self.users)

    def initialize_jobs(self):

        if not self.jobs:

            sample_jobs = [

                {
                    "job_id": "J001",
                    "title": "Python Developer",
                    "company": "Tech Solutions",
                    "location": "Hyderabad",
                    "salary": "5 LPA",
                    "skills": "Python, SQL",
                    "description": "Develop Python applications"
                },

                {
                    "job_id": "J002",
                    "title": "Data Engineer",
                    "company": "Data Corp",
                    "location": "Bangalore",
                    "salary": "7 LPA",
                    "skills": "Python, SQL, ETL",
                    "description": "Build data pipelines"
                },

                {
                    "job_id": "J003",
                    "title": "Software Developer",
                    "company": "Innovate Ltd",
                    "location": "Chennai",
                    "salary": "6 LPA",
                    "skills": "Java, Python",
                    "description": "Develop software applications"
                }

            ]

            self.jobs.extend(sample_jobs)
            save_data(JOBS_FILE, self.jobs)

    # ======================================
    # UTILITY FUNCTIONS
    # ======================================

    def generate_id(self, prefix, records, key):

        numbers = []

        for record in records:

            record_id = record.get(key, "")

            if record_id.startswith(prefix):

                try:
                    number = int(record_id[len(prefix):])
                    numbers.append(number)

                except ValueError:
                    pass

        next_number = max(numbers, default=0) + 1

        return f"{prefix}{next_number:03d}"

    def get_input(self, message):

        return input(message).strip()

    # ======================================
    # USER REGISTRATION
    # ======================================

    def register_user(self):

        print("\n========== USER REGISTRATION ==========")

        name = self.get_input("Enter your name: ")
        email = self.get_input("Enter email: ").lower()
        password = self.get_input("Enter password: ")

        if not name or not email or not password:

            print("All fields are required.")
            return

        for user in self.users:

            if user["email"] == email:

                print("Email already registered.")
                return

        user_id = self.generate_id(
            "U", self.users, "user_id"
        )

        user = {

            "user_id": user_id,
            "name": name,
            "email": email,
            "password": password,
            "role": "job_seeker"

        }

        self.users.append(user)

        save_data(USERS_FILE, self.users)

        print("\nRegistration successful!")
        print("Your User ID:", user_id)

    # ======================================
    # USER LOGIN
    # ======================================

    def login(self):

        print("\n========== LOGIN ==========")

        email = self.get_input("Enter email: ").lower()
        password = self.get_input("Enter password: ")

        for user in self.users:

            if (
                user["email"] == email
                and user["password"] == password
            ):

                print("\nLogin successful!")
                print("Welcome,", user["name"])

                return user

        print("Invalid email or password.")

        return None

    # ======================================
    # DISPLAY JOBS
    # ======================================

    def display_jobs(self, jobs=None):

        if jobs is None:
            jobs = self.jobs

        print("\n========== AVAILABLE JOBS ==========")

        if not jobs:

            print("No jobs available.")
            return

        for job in jobs:

            print("\nJob ID:", job["job_id"])
            print("Title:", job["title"])
            print("Company:", job["company"])
            print("Location:", job["location"])
            print("Salary:", job["salary"])
            print("Skills:", job["skills"])
            print("Description:", job["description"])
            print("-" * 40)

    # ======================================
    # SEARCH JOBS
    # ======================================

    def search_jobs(self):

        keyword = self.get_input(
            "\nEnter job title, company, or skill: "
        ).lower()

        results = []

        for job in self.jobs:

            searchable_text = (
                job["title"] + " "
                + job["company"] + " "
                + job["skills"] + " "
                + job["location"]
            ).lower()

            if keyword in searchable_text:

                results.append(job)

        if results:

            self.display_jobs(results)

        else:

            print("No matching jobs found.")

    # ======================================
    # APPLY FOR JOB
    # ======================================

    def apply_for_job(self, user):

        self.display_jobs()

        if not self.jobs:
            return

        job_id = self.get_input(
            "\nEnter Job ID to apply: "
        ).upper()

        selected_job = None

        for job in self.jobs:

            if job["job_id"] == job_id:

                selected_job = job
                break

        if selected_job is None:

            print("Invalid Job ID.")
            return

        for application in self.applications:

            if (
                application["job_id"] == job_id
                and application["user_id"] == user["user_id"]
            ):

                print("You have already applied for this job.")
                return

        application_id = self.generate_id(
            "A", self.applications, "application_id"
        )

        application = {

            "application_id": application_id,
            "user_id": user["user_id"],
            "job_id": job_id,
            "job_title": selected_job["title"],
            "company": selected_job["company"],
            "applied_date": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            "status": "Applied"

        }

        self.applications.append(application)

        save_data(
            APPLICATIONS_FILE,
            self.applications
        )

        print("\nApplication submitted successfully!")
        print("Application ID:", application_id)

    # ======================================
    # VIEW MY APPLICATIONS
    # ======================================

    def view_my_applications(self, user):

        print("\n========== MY APPLICATIONS ==========")

        user_applications = [

            application
            for application in self.applications
            if application["user_id"] == user["user_id"]

        ]

        if not user_applications:

            print("You have not applied for any jobs.")
            return

        for application in user_applications:

            print("\nApplication ID:",
                  application["application_id"])

            print("Job Title:",
                  application["job_title"])

            print("Company:",
                  application["company"])

            print("Applied Date:",
                  application["applied_date"])

            print("Status:",
                  application["status"])

            print("-" * 40)

    # ======================================
    # UPDATE PROFILE
    # ======================================

    def update_profile(self, user):

        print("\n========== UPDATE PROFILE ==========")

        new_name = self.get_input(
            "Enter new name (press Enter to keep current): "
        )

        new_password = self.get_input(
            "Enter new password (press Enter to keep current): "
        )

        for stored_user in self.users:

            if stored_user["user_id"] == user["user_id"]:

                if new_name:
                    stored_user["name"] = new_name

                if new_password:
                    stored_user["password"] = new_password

                user.update(stored_user)

                save_data(USERS_FILE, self.users)

                print("Profile updated successfully!")
                return

    # ======================================
    # ADMIN - ADD JOB
    # ======================================

    def add_job(self):

        print("\n========== ADD NEW JOB ==========")

        title = self.get_input("Enter job title: ")
        company = self.get_input("Enter company name: ")
        location = self.get_input("Enter location: ")
        salary = self.get_input("Enter salary: ")
        skills = self.get_input("Enter required skills: ")
        description = self.get_input("Enter job description: ")

        if not title or not company:

            print("Job title and company are required.")
            return

        job_id = self.generate_id(
            "J", self.jobs, "job_id"
        )

        job = {

            "job_id": job_id,
            "title": title,
            "company": company,
            "location": location,
            "salary": salary,
            "skills": skills,
            "description": description

        }

        self.jobs.append(job)

        save_data(JOBS_FILE, self.jobs)

        print("\nJob added successfully!")
        print("Job ID:", job_id)

    # ======================================
    # ADMIN - VIEW APPLICATIONS
    # ======================================

    def view_all_applications(self):

        print("\n========== ALL APPLICATIONS ==========")

        if not self.applications:

            print("No applications available.")
            return

        for application in self.applications:

            applicant_name = "Unknown"

            for user in self.users:

                if user["user_id"] == application["user_id"]:

                    applicant_name = user["name"]
                    break

            print("\nApplication ID:",
                  application["application_id"])

            print("Applicant:",
                  applicant_name)

            print("User ID:",
                  application["user_id"])

            print("Job Title:",
                  application["job_title"])

            print("Company:",
                  application["company"])

            print("Applied Date:",
                  application["applied_date"])

            print("Status:",
                  application["status"])

            print("-" * 40)

    # ======================================
    # ADMIN - UPDATE APPLICATION STATUS
    # ======================================

    def update_application_status(self):

        self.view_all_applications()

        if not self.applications:
            return

        application_id = self.get_input(
            "\nEnter Application ID: "
        ).upper()

        selected_application = None

        for application in self.applications:

            if (
                application["application_id"]
                == application_id
            ):

                selected_application = application
                break

        if selected_application is None:

            print("Application not found.")
            return

        print("\nAvailable statuses:")

        print("1. Applied")
        print("2. Under Review")
        print("3. Shortlisted")
        print("4. Interview")
        print("5. Selected")
        print("6. Rejected")

        choice = self.get_input(
            "Select new status: "
        )

        statuses = {

            "1": "Applied",
            "2": "Under Review",
            "3": "Shortlisted",
            "4": "Interview",
            "5": "Selected",
            "6": "Rejected"

        }

        if choice not in statuses:

            print("Invalid status choice.")
            return

        selected_application["status"] = statuses[choice]

        save_data(
            APPLICATIONS_FILE,
            self.applications
        )

        print("\nApplication status updated!")
        print("New Status:", statuses[choice])

    # ======================================
    # ADMIN - DELETE JOB
    # ======================================

    def delete_job(self):

        self.display_jobs()

        if not self.jobs:
            return

        job_id = self.get_input(
            "\nEnter Job ID to delete: "
        ).upper()

        selected_job = None

        for job in self.jobs:

            if job["job_id"] == job_id:

                selected_job = job
                break

        if selected_job is None:

            print("Job not found.")
            return

        confirm = self.get_input(
            "Confirm deletion? (yes/no): "
        ).lower()

        if confirm != "yes":

            print("Deletion cancelled.")
            return

        self.jobs.remove(selected_job)

        save_data(JOBS_FILE, self.jobs)

        print("Job deleted successfully!")

    # ======================================
    # JOB SEEKER MENU
    # ======================================

    def job_seeker_menu(self, user):

        while True:

            print("\n")
            print("=" * 45)
            print("         JOB SEEKER DASHBOARD")
            print("=" * 45)

            print("1. View All Jobs")
            print("2. Search Jobs")
            print("3. Apply for Job")
            print("4. View My Applications")
            print("5. Update Profile")
            print("6. Logout")

            choice = self.get_input(
                "\nEnter your choice: "
            )

            if choice == "1":

                self.display_jobs()

            elif choice == "2":

                self.search_jobs()

            elif choice == "3":

                self.apply_for_job(user)

            elif choice == "4":

                self.view_my_applications(user)

            elif choice == "5":

                self.update_profile(user)

            elif choice == "6":

                print("Logged out successfully.")
                break

            else:

                print("Invalid choice. Try again.")

    # ======================================
    # ADMIN MENU
    # ======================================

    def admin_menu(self, user):

        while True:

            print("\n")
            print("=" * 45)
            print("            ADMIN DASHBOARD")
            print("=" * 45)

            print("1. View All Jobs")
            print("2. Add New Job")
            print("3. View All Applications")
            print("4. Update Application Status")
            print("5. Delete Job")
            print("6. Logout")

            choice = self.get_input(
                "\nEnter your choice: "
            )

            if choice == "1":

                self.display_jobs()

            elif choice == "2":

                self.add_job()

            elif choice == "3":

                self.view_all_applications()

            elif choice == "4":

                self.update_application_status()

            elif choice == "5":

                self.delete_job()

            elif choice == "6":

                print("Logged out successfully.")
                break

            else:

                print("Invalid choice. Try again.")

    # ======================================
    # MAIN MENU
    # ======================================

    def run(self):

        while True:

            print("\n")
            print("=" * 45)
            print("      JOB PORTAL AND APPLICATION TRACKING")
            print("=" * 45)

            print("1. Register")
            print("2. Login")
            print("3. Exit")

            choice = self.get_input(
                "\nEnter your choice: "
            )

            if choice == "1":

                self.register_user()

            elif choice == "2":

                user = self.login()

                if user:

                    if user["role"] == "admin":

                        self.admin_menu(user)

                    else:

                        self.job_seeker_menu(user)

            elif choice == "3":

                print("Thank you for using Job Portal!")
                break

            else:

                print("Invalid choice. Try again.")


# ==========================================
# PROGRAM START
# ==========================================

if __name__ == "__main__":

    portal = JobPortal()
    portal.run()