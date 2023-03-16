import json
class dataInput:
    def __init__(self):
        self.num_stud = int(input("Number of student: "))
        #self.stdInput()
    def stdInput(self):
        for i in range(self.num_stud):
            id=input(f"ID of student {i+1}")
            name=input(f"name of student {i+1}")
            DoB= input(f"Date of student {i+1}")
            data={id:{"Name":name,"DoB":DoB,"Course":{}}}
            self.jsoninput(data)
    def jsoninput(self,data):
        try:
            with open("data1.json","r") as file:
                old_data=json.load(file)
        except FileNotFoundError:
            with open("data1.json","w") as file:
                json.dump(data, file, indent=4)
        else:
            old_data.update(data)
            with open("data1.json","w") as file:
                json.dump(old_data,file,indent=4)
    def course_input(self):
         course_stud= int(input("Number of courses: "))
         for i in range (course_stud):
             id= input(f"ID of course {i+1}: ")
             name=input(f" name of course {i+1}: ")
             data= {id:{"name":name,"mark":0}}
             self.course_data(data)
    def course_data(self,data):
         with open("data1.json","r") as file:
             old_data=json.load(file)
         for stu in old_data:
             old_data.get(stu)["Course"].update(data)
         with open("data1.json","w") as file:
             json.dump(old_data,file,indent=4)
             
         
        
                        


             
        
                    

          
       




