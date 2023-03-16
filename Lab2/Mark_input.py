import json
class Mark_input:
    def __init__(self):
        self.mark_input()
    def mark_input(self):
        stu_id=input("ID of student")
        with open("data1.json","r") as file:
            old_data=json.load(file)
        if stu_id in old_data:
            course_id = input("ID of course: ")
            if course_id in old_data[stu_id]["Course"]:
                mark = input("Input mark: ")
                old_data[stu_id]["Course"][course_id]["mark"]=mark
        with open("data1.json","w") as file:
            json.dump(old_data,file,indent=4)


