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
        self.marks[course_id] = mark


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

    def manage_students_courses(self):
        while True:
            print("1. List courses")
            print("2. List students")
            print("3. Show student marks for a course")
            print("4. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                self.list_courses()
            elif choice == 2:
                self.list_students()
            elif choice == 3:
                course_id = input("Enter course id: ")
                self.show_student_marks(course_id)
            elif choice == 4:
                break
            else:
                print("Invalid choice. Please enter again.")

        self.list_students()
        self.list_courses()
        for course_id in self.courses:
            self.show_student_marks(course_id)

sms = StudentManagementSystem()
sms.input_student_info()
sms.manage_students_courses()

