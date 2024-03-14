# input.py
def input_student_info(sms):
    num_students = int(input("Enter number of students: "))
    for _ in range(num_students):
        student_id = input("Enter student id: ")
        name = input("Enter student name: ")
        dob = input("Enter student date of birth: ")
        student = domains.person.Student(name, dob, student_id)
        sms.students.append(student)

    num_courses = int(input("Enter number of courses: "))
    for _ in range(num_courses):
        course_id = input("Enter course id: ")
        name = input("Enter course name: ")
        sms.courses[course_id] = name

        for student in sms.students:
            mark = input(f"Enter marks for {student.name} in {name}: ")
            student.enter_marks(course_id, mark)
