import json


class MarkOutput:
    def __init__(self):
        pass


    def mark_output(self):
        course_id = input("Course id: ")
        output_list = []
        with open("data1.json", "r") as file:
            data = json.load(file)
        for student in data:
            if course_id in data[student]["Course"]:
                data_pattern = {data[student]["Name"]: data[student]["Course"][course_id]["mark"]}
                output_list.append(data_pattern)
        print(output_list)


    def student_ouput(self):
        list_stu = []
        with open("data1.json", "r") as file:
            data = json.load(file)
            for student in data:
                data_pattern = {data[student]["Name"]: student}
                list_stu.append(data_pattern)
        print(list_stu)

    def course_ouput(self):
        list_course = []
        with open("data1.json", "r") as file:
            data = json.load(file)
            course_dict = data[list(data.keys())[0]]["Course"];
            for id in course_dict:
                data_pattern = {course_dict[id]["name"]: id}
                list_course.append(data_pattern)
            print(list_course)
