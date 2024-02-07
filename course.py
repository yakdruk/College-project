class Course:
    def __init__(self, course_code, course_name, lecturer):
        self.course_code = course_code
        self.course_name = course_name
        self.lecturer = lecturer
        self.students = []


class KlassLectures:
    def __init__(self, klass_name, lecturer, course):
        self.klass_name = klass_name
        self.lecturer = lecturer
        self.course = course

