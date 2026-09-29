What This Project Solves

Keeping track of everything in a college, like students, teachers, staff, library books, and who comes in and out every day, gets messy really fast. When people rely on spreadsheets or paper registers, things get misplaced, attendance gets miscalculated, and tracking who borrowed what book becomes a headache.

This project is a simple, lightweight system built in Python that manages all of these day-to-day college tasks right from the terminal. Instead of dealing with heavy external databases, it saves everything cleanly into simple text files so it stays fast, portable, and easy to run anywhere.

Key Goals and What It Needs to Do

Managing People and Profiles
Students: Store basic details, fee records, and subject marks. The system automatically works out their average score and assigns them a final grade such as A+, A, B, C, D, or F.
Faculty: Keep track of professors, their departments, and contact info.
Support Staff: Maintain records for non-teaching staff across campus.

Library Operations
Keep a catalog of books including title, author, price, and publication year.
Handle issuing and returning books safely by checking if a student ID actually exists before lending anything out.

Daily Attendance and Check-in Logs
Attendance: Mark daily presence for students, teachers, and staff, and tally up how many days each person has attended.
Library Timings: Log exact entry and exit timestamps using the system clock whenever someone visits the library.

Under the Hood
Uses Object-Oriented Programming principles, where Student, Faculty, and Staff build on top of a shared Person base class.
Uses Python's built-in array module for handling numbers like test marks and attendance tallies efficiently.
Saves all data persistently into plain text files so no information is lost when you close the application.