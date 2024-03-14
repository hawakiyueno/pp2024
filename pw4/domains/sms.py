# domains/sms.py
import numpy as np

class StudentManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = {}

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
