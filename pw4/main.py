# main.py
import curses
import input
import output
import domains.sms

def main(stdscr):
    output.initialize_curses()
    output.clear_screen(stdscr)

    sms = domains.sms.StudentManagementSystem()

    output.show_message(stdscr, "Welcome to the Student Management System!", 2, 5, curses.A_BOLD)
    output.show_message(stdscr, "Press any key to continue...", 4, 5)
    stdscr.getch()

    output.clear_screen(stdscr)

    input.input_student_info(sms)

    output.clear_screen(stdscr)
    output.show_message(stdscr, "Student Management System Menu", 2, 5, curses.A_BOLD)

    while True:
        output.show_message(stdscr, "1. List courses", 4, 5)
        output.show_message(stdscr, "2. List students", 5, 5)
        output.show_message(stdscr, "3. Show student marks for a course", 6, 5)
        output.show_message(stdscr, "4. Calculate and display GPA for a student", 7, 5)
        output.show_message(stdscr, "5. Sort students by GPA", 8, 5)
        output.show_message(stdscr, "6. Exit", 9, 5)

        choice = output.get_choice(stdscr)

        output.clear_screen(stdscr)

        if choice == 1:
            sms.list_courses()
        elif choice == 2:
            sms.list_students()
        elif choice == 3:
            course_id = input("Enter course id: ")
            sms.show_student_marks(course_id)
        elif choice == 4:
            student_id = input("Enter student id: ")
            sms.calculate_and_display_gpa(student_id)
        elif choice == 5:
            sms.sort_students_by_gpa()
            print("Students sorted by GPA.")
        elif choice == 6:
            break
        else:
            print("Invalid choice. Please enter again.")

    sms.list_students()
    sms.list_courses()
    for course_id in sms.courses:
        sms.show_student_marks(course_id)

if __name__ == "__main__":
    curses.wrapper(main)
