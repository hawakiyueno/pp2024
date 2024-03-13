import curses
import math
import numpy as np


class Person:
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob


class Student(Person):
    def __init__(self, name, dob, student_id):
        super().__init__(name, dob)
        self.student_id = student_id
        self.marks = {}

    def enter_marks(self, course_id, mark):
        rounded_mark = math.floor(float(mark))  # Round-down mark with floor()
        self.marks[course_id] = rounded_mark

    def calculate_gpa(self, credits):
        if not self.marks:
            return 0.0
        marks_array = np.array(list(self.marks.values()))
        weighted_sum = np.sum(marks_array * credits)
        total_credits = np.sum(credits)
        return round(weighted_sum / total_credits, 2)


class StudentManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = {}

    def input_student_info(self):
        num_students = int(input("Enter number of students: "))
        for _ in range(num_students):
            student_id = input("Enter student id: ")
            name = input("Enter student name: ")
            dob = input("Enter student date of birth: ")
            student = Student(name, dob, student_id)
            self.students.append(student)

        num_courses = int(input("Enter number of courses: "))
        for _ in range(num_courses):
            course_id = input("Enter course id: ")
            name = input("Enter course name: ")
            self.courses[course_id] = name

            for student in self.students:
                mark = input(f"Enter marks for {student.name} in {name}: ")
                student.enter_marks(course_id, mark)

    def list_courses(self):
        print("Courses:")
        for course_id, name in self.courses.items():
            print(f"ID: {course_id}, Name: {name}")

    def list_students(self):
        print("Students:")
        for student in self.students:
            print(f"ID: {student.student_id}, Name: {student.name}, DOB: {student.dob}")

    def show_student_marks(self, course_id):
        print(f"Marks for course {self.courses[course_id]}:")
        for student in self.students:
            if course_id in student.marks:
                print(f"{student.name}: {student.marks[course_id]}")
            else:
                print(f"{student.name}: No marks entered")

    def calculate_and_display_gpa(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                credits = np.array([1.0] * len(self.courses))  # Assume equal credits for each course
                gpa = student.calculate_gpa(credits)
                print(f"GPA for {student.name}: {gpa}")
                return
        print(f"Student with ID {student_id} not found.")

    def sort_students_by_gpa(self):
        credits = np.array([1.0] * len(self.courses))  # Assume equal credits for each course
        self.students.sort(key=lambda student: student.calculate_gpa(credits), reverse=True)


def main(stdscr):
    curses.curs_set(0)  # Hide the cursor
    stdscr.clear()

    sms = StudentManagementSystem()

    stdscr.addstr(2, 5, "Welcome to the Student Management System!", curses.A_BOLD)
    stdscr.refresh()

    stdscr.addstr(4, 5, "Press any key to continue...")
    stdscr.getch()

    stdscr.clear()

    sms.input_student_info()

    stdscr.clear()
    stdscr.addstr(2, 5, "Student Management System Menu", curses.A_BOLD)

    while True:
        stdscr.addstr(4, 5, "1. List courses")
        stdscr.addstr(5, 5, "2. List students")
        stdscr.addstr(6, 5, "3. Show student marks for a course")
        stdscr.addstr(7, 5, "4. Calculate and display GPA for a student")
        stdscr.addstr(8, 5, "5. Sort students by GPA")
        stdscr.addstr(9, 5, "6. Exit")

        stdscr.addstr(11, 5, "Enter your choice: ")
        stdscr.refresh()

        choice = stdscr.getch() - ord('0')

        stdscr.clear()

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
