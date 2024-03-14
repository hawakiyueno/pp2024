# domains/person.py
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
