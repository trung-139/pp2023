from data_input import DataInput
from update_function import Update

data_input = DataInput()
update = Update()


# num_stu = int(input("Number of student"))
# data_input.class_data_input(num_stu)
# data_input.course_data_input(num_stu)

update.update_student_list()
update.mark_update()
update.gpa_cal()

