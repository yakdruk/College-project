class College:
    def __init__(self):
        self.lecturers = []
        self.courses = []
        self.students = []
        self.name = ""
        self.city = ""

    @classmethod
    def build_college(cls, name, city):
        college = cls()
        college.name = name
        college.city = city
        return college

    def add_lecturer(self, lecturer):
        self.lecturers.append(lecturer)

    def remove_lecturer(self, lecturer):
        if lecturer in self.lecturers:
            self.lecturers.remove(lecturer)
            return f"{lecturer.name} removed from the list of lecturers."
        else:
            return "Error: Lecturer not found in the list."

    def add_course(self, course):
        self.courses.append(course)

    def remove_course(self, course):
        if course in self.courses:
            self.courses.remove(course)
            return f"{course.course_name} removed from the list of courses."
        else:
            return "Error: Course not found in the list."

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)
            return f"{student.name} removed from the list of students."
        else:
            return "Error: Student not found in the list."

    def print_lecturer_details(self, lecturer):
        if lecturer in self.lecturers:
            print(f"Lecturer Details:\n{lecturer.get_details()}")
        else:
            print("Error: Lecturer not found in the list.")

    def print_student_details(self, student):
        if student in self.students:
            print(f"Student Details:\n{student.get_details()}")
        else:
            print("Error: Student not found in the list.")

    def print_course_details(self, course):
        if course in self.courses:
            print(f"Course Details:\nCode: {course.course_code}\nName: {course.course_name}")
            print(f"Lecturer: {course.lecturer.get_details()}")
        else:
            print("Error: Course not found in the list.")

    def admit_student_to_course(self, student, course):
        if student in self.students and course in self.courses:
            course.students.append(student)
            return f"{student.name} admitted to {course.course_name}."
        else:
            return "Error: Student or course not found."

    def remove_student_from_course(self, student, course):
        if student in self.students and course in self.courses:
            if student in course.students:
                course.students.remove(student)
                return f"{student.name} removed from {course.course_name}."
            else:
                return "Error: Student not enrolled in the course."
        else:
            return "Error: Student or course not found."

    def print_student_tests(self, student, course):
        if student in self.students and course in self.courses:
            student_tests = [test for test in student.tests if test.course == course]
            if student_tests:
                print(f"Tests and Grades for {student.name} in {course.course_name}:")
                for test in student_tests:
                    print(f"{test.test_type.type_name}: {test.grade}")
            else:
                print(f"No tests found for {student.name} in {course.course_name}.")
        else:
            print("Error: Student or course not found.")

    def print_all_course_tests(self):
        for course in self.courses:
            print(f"Tests and Grades for {course.course_name}:")
            for student in course.students:
                student_tests = [test for test in student.tests if test.course == course]
                if student_tests:
                    print(f"{student.name}:")
                    for test in student_tests:
                        print(f"  {test.test_type.type_name}: {test.grade}")
                else:
                    print(f"{student.name}: No tests found.")
            print()

    def get_final_grade(self, student, course):
        if student in self.students and course in self.courses:
            student_tests = [test.grade for test in student.tests if test.course == course]
            if student_tests:
                final_grade = sum(student_tests) / len(student_tests)
                return f"Final grade for {student.name} in {course.course_name}: {final_grade}"
            else:
                return f"No tests found for {student.name} in {course.course_name}."
        else:
            return "Error: Student or course not found."

    def get_student_average_grade_in_course(self, student, course):
        if student in self.students and course in self.courses:
            student_tests = [test.grade for test in student.tests if test.course == course]
            if student_tests:
                average_grade = sum(student_tests) / len(student_tests)
                return f"Average grade for {student.name} in {course.course_name}: {average_grade}"
            else:
                return f"No tests found for {student.name} in {course.course_name}."
        else:
            return "Error: Student or course not found."

    def get_student_average_grade_overall(self, student):
        if student in self.students:
            all_student_tests = [test.grade for test in student.tests]
            if all_student_tests:
                overall_average = sum(all_student_tests) / len(all_student_tests)
                return f"Overall average grade for {student.name}: {overall_average}"
            else:
                return f"No tests found for {student.name}."
        else:
            return "Error: Student not found."

    def get_course_average_grade(self, course):
        if course in self.courses:
            all_course_tests = [test.grade for student in course.students for test in student.tests if
                                test.course == course]
            if all_course_tests:
                course_average = sum(all_course_tests) / len(all_course_tests)
                return f"Average grade for {course.course_name}: {course_average}"
            else:
                return f"No tests found for {course.course_name}."
        else:
            return "Error: Course not found."

    def display_details(self):
        print(f"College Details:\nName: {self.name}\nCity: {self.city}")
        print("\nList of Lecturers:")
        for lecturer in self.lecturers:
            print(lecturer.get_details())

        print("\nList of Courses:")
        for course in self.courses:
            print(f"Course: {course.course_code} - {course.course_name}")

        print("\nList of Students:")
        for student in self.students:
            print(student.get_details())
        print()
