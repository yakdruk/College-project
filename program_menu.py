from college import College
from student import Student
from staff import Staff
from course import Course
from test import Test
from test_type import TestType


class ProgramMenu:
    def __init__(self):
        self.college = None

    def create_college(self):
        name = input("Enter the name of the college: ")
        city = input("Enter the city of the college: ")
        self.college = College.build_college(name, city)
        print(f"\nWelcome to {name} College Management System!\n")

    def run(self):
        if not self.college:
            self.create_college()

        while True:
            print("College Management System Menu:")
            print("1. Add Lecturer")
            print("2. Remove Lecturer")
            print("3. Add Course")
            print("4. Remove Course")
            print("5. Add Student")
            print("6. Remove Student")
            print("7. Print Lecturer Details")
            print("8. Print Student Details")
            print("9. Print Course Details")
            print("10. Admit Student to Course")
            print("11. Remove Student from Course")
            print("12. Create Test for Student")
            print("13. Print Student Tests")
            print("14. Print All Course Tests")
            print("15. Get Final Grade")
            print("16. Get Student Average Grade in Course")
            print("17. Get Student Average Grade Overall")
            print("18. Get Course Average Grade")
            print("19. Display College Details")
            print("20. Exit")

            choice = input("\nEnter your choice (1-20): ")
            if choice == "1":
                if self.college:
                    name = input("Enter the lecturer name: ")
                    age = int(input("Enter the lecturer age: "))
                    gender = input("Enter the lecturer gender: ")
                    staff_id = input("Enter the staff ID: ")
                    lecturer = Staff(name, age, gender, staff_id)
                    self.college.add_lecturer(lecturer)
                    print(f"Lecturer {name} added.")
                else:
                    print("Please create a college first.")
            elif choice == "2":
                if self.college:
                    staff_id = input("Enter the staff ID of the lecturer to remove: ")
                    lecturer = next((lec for lec in self.college.lecturers if lec.staff_id == staff_id), None)
                    if lecturer:
                        self.college.remove_lecturer(lecturer)
                        print(f"Lecturer {lecturer.name} removed.")
                    else:
                        print("Lecturer not found.")
                else:
                    print("Please create a college first.")

            elif choice == "3":
                if self.college:
                    course_code = input("Enter the course code: ")
                    course_name = input("Enter the course name: ")
                    lecturer_staff_id = input("Enter the staff ID of the lecturer for the course: ")
                    lecturer = next((lec for lec in self.college.lecturers if lec.staff_id == lecturer_staff_id), None)
                    if lecturer:
                        course = Course(course_code, course_name, lecturer)
                        self.college.add_course(course)
                        print(f"Course {course_code} - {course_name} added.")
                    else:
                        print("Lecturer not found.")
                else:
                    print("Please create a college first.")

            elif choice == "4":
                if self.college:
                    course_code = input("Enter the course code of the course to remove: ")
                    course = next((crs for crs in self.college.courses if crs.course_code == course_code), None)
                    if course:
                        self.college.remove_course(course)
                        print(f"Course {course.course_name} removed.")
                    else:
                        print("Course not found.")
                else:
                    print("Please create a college first.")
            elif choice == "5":
                if self.college:
                    name = input("Enter the student name: ")
                    age = int(input("Enter the student age: "))
                    gender = input("Enter the student gender: ")
                    student_id = input("Enter the student ID: ")
                    student = Student(name, age, gender, student_id)
                    self.college.add_student(student)
                    print(f"Student {name} added.")
                else:
                    print("Please create a college first.")
            elif choice == "6":
                if self.college:
                    student_id = input("Enter the student ID of the student to remove: ")
                    student = next((std for std in self.college.students if std.student_id == student_id), None)
                    if student:
                        self.college.remove_student(student)
                        print(f"Student {student.name} removed.")
                    else:
                        print("Student not found.")
                else:
                    print("Please create a college first.")
            elif choice == "7":
                if self.college:
                    staff_id = input("Enter the staff ID of the lecturer: ")
                    lecturer = next((lec for lec in self.college.lecturers if lec.staff_id == staff_id), None)
                    if lecturer:
                        self.college.print_lecturer_details(lecturer)
                    else:
                        print("Lecturer not found.")
                else:
                    print("Please create a college first.")
            elif choice == "8":
                if self.college:
                    student_id = input("Enter the student ID: ")
                    student = next((std for std in self.college.students if std.student_id == student_id), None)
                    if student:
                        self.college.print_student_details(student)
                    else:
                        print("Student not found.")
                else:
                    print("Please create a college first.")
            elif choice == "9":
                if self.college:
                    course_code = input("Enter the course code: ")
                    course = next((crs for crs in self.college.courses if crs.course_code == course_code), None)
                    if course:
                        self.college.print_course_details(course)
                    else:
                        print("Course not found.")
                else:
                    print("Please create a college first.")
            elif choice == "10":
                if self.college:
                    student_id = input("Enter the student ID: ")
                    course_code = input("Enter the course code: ")
                    student = next((std for std in self.college.students if std.student_id == student_id), None)
                    course = next((crs for crs in self.college.courses if crs.course_code == course_code), None)
                    if student and course:
                        print(self.college.admit_student_to_course(student, course))
                        # Add the option to enroll the student in the course
                        enroll_choice = input("Do you want to enroll the student in this course? (y/n): ").lower()
                        if enroll_choice == "y":
                            print(student.enroll_in_course(course))
                    else:
                        print("Student or course not found.")
                else:
                    print("Please create a college first.")
            elif choice == "11":
                if self.college:
                    student_id = input("Enter the student ID: ")
                    course_code = input("Enter the course code: ")
                    student = next((std for std in self.college.students if std.student_id == student_id), None)
                    course = next((crs for crs in self.college.courses if crs.course_code == course_code), None)
                    if student and course:
                        # Add the option to withdraw the student from the course
                        withdraw_choice = input(
                            "Do you want to withdraw the student from this course? (y/n): ").lower()
                        if withdraw_choice == "y":
                            print(student.withdraw_from_course(course))
                        print(self.college.remove_student_from_course(student, course))
                    else:
                        print("Student or course not found.")
                else:
                    print("Please create a college first.")
            elif choice == "12":
                if self.college:
                    student_id = input("Enter the student ID: ")
                    course_code = input("Enter the course code: ")
                    test_type_name = input("Enter the test type name: ")
                    test_weight = float(input("Enter the test weight: "))
                    grade = float(input("Enter the test grade: "))

                    student = next(
                        (stu for stu in self.college.students if
                         isinstance(stu, Student) and stu.student_id == student_id),
                        None)
                    course = next((crs for crs in self.college.courses if crs.course_code == course_code), None)

                    if student and course:
                        # Check if the student is enrolled in the course before adding the test
                        if course in student.enrolled_courses:
                            test_type = TestType(test_type_name, test_weight)
                            test = Test(grade, course, student, test_type)
                            student.tests.append(test)
                            print(f"Test created and added for {student.name} in {course.course_name}.")
                        else:
                            print(f"Error: {student.name} is not enrolled in the course {course.course_name}.")
                    else:
                        print("Error: Student or course not found.")
                else:
                    print("Please create a college first.")
            elif choice == "13":
                if self.college:
                    student_id = input("Enter the student ID: ")
                    course_code = input("Enter the course code: ")
                    student = next((std for std in self.college.students if std.student_id == student_id), None)
                    course = next((crs for crs in self.college.courses if crs.course_code == course_code), None)
                    if student and course:
                        self.college.print_student_tests(student, course)
                    else:
                        print("Student or course not found.")
                else:
                    print("Please create a college first.")
            elif choice == "14":
                if self.college:
                    self.college.print_all_course_tests()
                else:
                    print("Please create a college first.")
            elif choice == "15":
                if self.college:
                    student_id = input("Enter the student ID: ")
                    course_code = input("Enter the course code: ")
                    student = next((std for std in self.college.students if std.student_id == student_id), None)
                    course = next((crs for crs in self.college.courses if crs.course_code == course_code), None)
                    if student and course:
                        print(self.college.get_final_grade(student, course))
                    else:
                        print("Student or course not found.")
                else:
                    print("Please create a college first.")
            elif choice == "16":
                if self.college:
                    student_id = input("Enter the student ID: ")
                    course_code = input("Enter the course code: ")
                    student = next((std for std in self.college.students if std.student_id == student_id), None)
                    course = next((crs for crs in self.college.courses if crs.course_code == course_code), None)
                    if student and course:
                        print(self.college.get_student_average_grade_in_course(student, course))
                    else:
                        print("Student or course not found.")
                else:
                    print("Please create a college first.")
            elif choice == "17":
                if self.college:
                    student_id = input("Enter the student ID: ")
                    student = next((std for std in self.college.students if std.student_id == student_id), None)
                    if student:
                        print(self.college.get_student_average_grade_overall(student))
                    else:
                        print("Student not found.")
                else:
                    print("Please create a college first.")
            elif choice == "18":
                if self.college:
                    course_code = input("Enter the course code: ")
                    course = next((crs for crs in self.college.courses if crs.course_code == course_code), None)
                    if course:
                        print(self.college.get_course_average_grade(course))
                    else:
                        print("Course not found.")
                else:
                    print("Please create a college first.")
            elif choice == "19":
                if self.college:
                    self.college.display_details()
                else:
                    print("Please create a college first.")
            elif choice == "20":
                print("Exiting the College Management System. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 20.")
