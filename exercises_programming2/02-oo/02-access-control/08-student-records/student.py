class Student:
    def __init__(self, name):
        self.name = name
        self.__courses = {}

    @staticmethod
    def calculate_letter_grade(score):
        if score >= 90:
            return 'A'
        elif score >= 80:
            return 'B'
        elif score >= 70:
            return 'C'
        elif score >= 60:
            return 'D'
        else:
            return 'F'

    def add_course(self, course_name, score):
        score_letter = Student.calculate_letter_grade(score)
        self.__courses[course_name] = score_letter

    def get_courses(self):
        return self.__courses