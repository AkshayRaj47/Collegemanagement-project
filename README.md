College Management System
A straightforward, menu-driven command-line tool written in Python to help manage college records, from student grades and faculty profiles to library books, daily attendance, and library visit logs.

How the Code Is Organized

The project folder is named collegemanagement and contains the following Python files:

person.py: Basic person class that stores name, age, and contact details.
student.py: Handles student details, grade calculations, and subject marks.
faculty.py: Stores professor and faculty profiles.
staff.py: Stores non-teaching staff profiles.
collegemanager.py: Contains all the main logic, file saving routines, and sub-menus.
main.py: The main entry point to launch the program.

What You Can Do

Students
Add, view, edit, or remove student profiles.
Automatically calculate average marks and assign letter grades.
Keep track of department, phone number, address, and fees.

Faculty and Staff
Manage profiles for both teaching faculty and support staff.
Keep contact details and departments organized.

Library
Maintain a list of all library books with pricing and release years.
Issue books to valid students and mark them as returned when brought back.
See a quick list of who currently has borrowed books.

Attendance and Visitor Tracking
Take daily attendance for students, faculty, and non-teaching staff.
Check attendance history and total present days for any ID.
Log library entry and exit times with automatic timestamps.

Requirements and Setup

You only need Python 3.7 or newer. There are no external packages or third-party libraries to install because everything runs using standard Python components like array, os, and datetime.

How to Run It:

Open your terminal or command prompt.

Navigate into the project folder using the command: cd collegemanagement

Start the application by running: python main.py

Saved Data Files

All your data is automatically created and stored in simple text files right inside your project folder:

students.txt: Holds student details, fees, and subject scores.
faculty.txt: Holds faculty member records.
staff.txt: Holds non-teaching staff records.
library_books.txt: Holds the full catalog of library books.
borrowers.txt: Holds active book loans.
student_attendance.txt: Holds student attendance history.
faculty_attendance.txt: Holds faculty attendance history.
staff_attendance.txt: Holds support staff attendance history.
library_entry_exit.txt: Holds time logs for library visits.

How It Works Behind the Scenes

Object-Oriented Design: Student, Faculty, and Staff inherit common properties like name, age, mobile, and address from a base Person class.
Built-in Arrays: Numeric data like grades and presence counts are processed using Python's array module for clean calculations.
Built-in Checks: Before issuing a book or taking attendance, the system checks the text files first to ensure the ID entered belongs to a valid person.
