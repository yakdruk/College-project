from person import Person
from test import Test


class Student(Person):
    def __init__(self, name, age, gender, student_id):
        super().__init__(name, age, gender)
        self.student_id = student_id
        self.tests = []
        self.enrolled_courses = []

    def add_test(self, grade, course, test_type):
        if course in self.enrolled_courses:
            new_test = Test(grade, course, self, test_type)
            self.tests.append(new_test)
            return f"Test added for {self.name} in {course.course_name}."
        else:
            return f"Error: {self.name} is not enrolled in the course {course.course_name}."

    def get_details(self):
        return f"Student: {self.name}, Age: {self.age}, ID: {self.student_id}"

    def enroll_in_course(self, course):
        self.enrolled_courses.append(course)
        return f"{self.name} enrolled in the course: {course.course_name}"

    def withdraw_from_course(self, course):
        if course in self.enrolled_courses:
            self.enrolled_courses.remove(course)
            return f"{self.name} withdrew from the course: {course.course_name}"
        else:
            return f"{self.name} was not enrolled in the course: {course.course_name}"
