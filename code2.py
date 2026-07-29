def report_decorator(func):
    def wrapper(*args,**kwargs):
        print("=" * 60)
        print("DYNAMIC REPORT GENERATOR".center(60))
        print("="*60)

        func(*args,**kwargs)

        print("=" * 60)
        print("END OF REPORT".center(60))
        print("=" * 60)

    return wrapper


class Report:
    company_namE="ABC Technologies Pvt. Ltd."

    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.contents = []

    def add_content(self,text):
        self.contents.append(text)

    @classmethod
    def change_company(cls,new_company):
        cls.company_name=new_company

    @staticmethod
    def line():
        print("-"* 60)

    def __str__(self):
        return f"Report Title:{self.title}\nAuthor:{self.author}"

    def __len__(self):
        return len(self.contents)

    @report_decorator
    def display_report(self):
        print("Company:",Report.company_name)
        print(self)

        Report.line()
        print("Report Contents:")

        for i, item in enumerate(self.contents, start=1):
            print(f"{i}.{item}")

        Report.line()
        print("Total Sections:", len(self))

r1 = Report("Advanced Python Practical Report", "Mandar Joshi")
r1.add_content("Completed Experiment No. 2 successfully.")
r1.add_content("Implemented Decorators, Class Methods, Static Methods and Magic Methods.")
r1.add_content("Learned Object-Oriented Programming concepts.")

print("\nChanging Company Name...\n")
Report.change_company("MIT ADT University")

# ---------------- Report 2 ----------------
r2 = Report("Employee Performance Report","Mandar Joshi")
r2.add_content("Attendance:98%")
r2.add_content("Projects Completed : 8")
r2.add_content("Rating:Excellent")

# ---------------- Report 3 ----------------
r3 = Report("Student Result Report","Mandar Joshi")
r3.add_content("Student Name:Rahul")
r3.add_content("CGPA:9.25")
r3.add_content("Result:Pass")

def show_reports():
    reports = {"1": r1, "2": r2, "3": r3}

    print("\nWhich report do you want to see?")
    print("1. Advanced Python Practical Report")
    print("2. Employee Performance Report")
    print("3. Student Result Report")
    print("A. All Reports")

    choice=input("Enter your choice (1/2/3/A):").strip().lower()

    if choice== "a":
        for key in reports:
            reports[key].display_report()
    elif choice in reports:
        reports[choice].display_report()
    else:
        print("Invalid choice. Please enter 1, 2, 3, or A.")


show_reports()