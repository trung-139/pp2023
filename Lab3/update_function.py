import json
from file_related_function import FileExecution

class Update:

    def __init__(self):
        self.file_processing = FileExecution()

    def update_student_list(self):

        course_id = input("Course ID: ")
        num_student_join = int(input("Number of Student join the course: "))
        stu_list = []
        for i in range(num_student_join):
            stu_id = input("Student ID: ")
            if self.file_processing.id_check(stu_id, "student.json"):
                stu_list.append(stu_id)
                with open("student.json", "r") as data_file:
                    stu_data = json.load(data_file)
                    course_list = stu_data[stu_id]["course_enrolled"]
                course_name = self.file_processing.data_searchup(course_id, "course.json")
                data_pattern_1 = {course_id: course_name}
                course_list.update(data_pattern_1)
                with open("student.json", "w") as data_file:
                    json.dump(stu_data, data_file, indent=4)

            else:
                print("This id is not registered")
        if len(stu_list) != 0:
            with open("course.json", "r") as file:
                course_data = json.load(file)
                list_data = course_data[course_id]["student_list"]

                for student_id in stu_list:
                    student_name = self.file_processing.data_searchup(student_id, "student.json")
                    data_pattern_2 = {student_id: student_name}
                    list_data.update(data_pattern_2)

            with open("course.json", "w") as file:
                json.dump(course_data, file, indent=4)

    def mark_update(self):
        course_id = input("Course ID: ")
        if self.file_processing.id_check(course_id, "course.json"):
            with open("mark.json", "r") as file:
                mark_data = json.load(file)
            course_name = self.file_processing.data_searchup(course_id, "course.json")
            for stu_id in mark_data:
                with open("student.json", "r") as data_file:
                    stu_data = json.load(data_file)
                    course_enrolled = stu_data[stu_id]["course_enrolled"]
                if course_id in course_enrolled:
                    course_enrolled_mark_list = mark_data[stu_id]["course_data"]["mark"]
                    stu_name = self.file_processing.data_searchup(stu_id, "student.json")
                    if course_id in course_enrolled_mark_list:
                        answer = input(f'{stu_name} has already have a mark of {mark_data[stu_id]["course_data"]["mark"][course_id]} '
                              f'for {course_name} course,Do you want to change it?y/n')
                        if answer == "y":
                            new_mark = int(input("New mark: "))
                            mark_data[stu_id]["course_data"]["mark"][course_id] = new_mark
                    else:
                        mark = int(input(f"Mark for {stu_name},with id of {stu_id}: "))
                        data_pattern = {course_id: mark}
                        mark_data[stu_id]["course_data"]["mark"].update(data_pattern)
            with open("mark.json", "w") as file:
                json.dump(mark_data, file, indent=4)
        else:
            print("This id is not registered")

    def gpa_cal (self):
        with open("mark.json", "r") as file:
            mark_data = json.load(file)


        for stu_id in mark_data:

            mark_dict = mark_data[stu_id]["course_data"]["mark"]
            course_id_list = []
            mark_list = []
            for course_id in mark_dict:
                course_id_list.append(course_id)
                mark_list.append(mark_dict[course_id])
            gpa = self.gpa_formula(course_id_list, mark_list)

            mark_data[stu_id]["course_data"]["gpa"] = gpa

            with open("mark.json", "w") as file:
                json.dump(mark_data, file, indent=4)

    def gpa_formula (self, course_list, mark_list):

        with open("course.json", "r") as file:
            course_data = json.load(file)

        course_credit_list = []
        total_credits = 0
        total_mark = 0
        for course_id in course_list:
            course_credit = course_data[course_id]["credit"]
            course_credit_list.append(course_credit)

        for index in range(len(mark_list)):
            total_mark += mark_list[index] * course_credit_list[index]
            total_credits += course_credit_list[index]

        gpa = total_mark / total_credits

        return gpa
