def input_student_info():
    students = {}
    courses = {}

    num_students = int(input("Enter number of students: "))
    for i in range(num_students):
        student_id = input("Enter student id: ")
        name = input("Enter student name: ")
        dob = input("Enter student date of birth: ")
        students[student_id] = {'name': name, 'dob': dob, 'marks': {}}

    num_courses = int(input("Enter number of courses: "))
    for i in range(num_courses):
        course_id = input("Enter course id: ")
        name = input("Enter course name: ")
        courses[course_id] = name

        for student_id, student_info in students.items():
            mark = input(f"Enter marks for {student_info['name']} in {name}: ")
            students[student_id]['marks'][course_id] = mark

    return students, courses


def manage_students_courses():
    students, courses = input_student_info()

    def list_courses():
        print("Courses:")
        for id, name in courses.items():
            print(f"ID: {id}, Name: {name}")

    def list_students():
        print("Students:")
        for id, info in students.items():
            print(f"ID: {id}, Name: {info['name']}, DOB: {info['dob']}")

    def show_student_marks(course_id):
        print(f"Marks for course {courses[course_id]}:")
        for id, info in students.items():
            if course_id in info['marks']:
                print(f"{info['name']}: {info['marks'][course_id]}")
            else:
                print(f"{info['name']}: No marks entered")

    while True:
        print("1. List courses")
        print("2. List students")
        print("3. Show student marks for a course")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            list_courses()
        elif choice == 2:
            list_students()
        elif choice == 3:
            course_id = input("Enter course id: ")
            show_student_marks(course_id)
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please enter again.")

    list_students()
    list_courses()
    for course_id in courses:
        show_student_marks(course_id)


manage_students_courses()
 