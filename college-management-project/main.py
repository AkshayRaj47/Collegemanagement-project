from collegemanager import CollegeManager
def main():
    manager=CollegeManager()
    while True:
        print("COLLEGE MANAGEMENT SYSTEM")
        print("1.Manage Students")
        print("2.Manage Faculty / Teachers")
        print("3.Manage Non-Teaching Staff")
        print("4.Manage Library System")
        print("5.Attendance & Library Entry/Exit Logs")
        print("6.Exit Program")
        choice=input("Enter your choice (1-6):").strip()
        if choice=="1":
            manager.manageStudents()
        elif choice=="2":
            manager.manageFaculty()
        elif choice=="3":
            manager.manageStaff()
        elif choice=="4":
            manager.manageLibrary()
        elif choice=="5":
            manager.manageAttendanceAndLogs()
        elif choice=="6":
            print("\nExiting College Management System. Goodbye!")
            break
        else:
            print("Invalid selection! Please enter a number between 1 and 6.")
if __name__ == "__main__":
    main()
