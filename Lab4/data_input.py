import json
from file_related_function import FileExecution

class DataInput:

    def __init__(self):
        self.file_processing = FileExecution()

    def class_data_input(self, student_number):

        for i in range(student_number):
            stu_id = input("Student ID: ")
            name = input("Name: ")
            dob = input("Date of Birth: ")
            data_pattern_1 = {stu_id: {"name": name, "dob": dob, "course_enrolled": {}}}
            data_pattern_2 = {stu_id: {"course_data": {"gpa": 0, "mark": {}}}}
            self.file_processing.update_file(data_pattern_1, "student.json")
            self.file_processing.update_file(data_pattern_2, "mark.json")

    def course_data_input(self, number_of_course):

        for i in range(number_of_course):
            course_id = input("Course ID: ")
            course_name = input("Name: ")
            credit = int(input("Number of Credits: "))
            data_pattern = {course_id: {"name": course_name, "credit": credit, "student_list": {}}}
            self.file_processing.update_file(data_pattern, "course.json")




