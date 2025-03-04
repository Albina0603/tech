class Student:
    def __init__(self,name,student_id,grades):
        self.name=name
        self.student_id=student_id
        self.grades=[]
        
    def add_grade(self,grades):
        self.grades.append(grades)
    
    def calculate_average(self):
        return sum (self.grades)/ len (self.grades)

    def display_info(self):
        average = self.calculate_average()
        print(f"Student Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print(f"Average grades: {average}")
        
        
        
student1=Student("Alice Johnson", 101, 97)  
student2=Student("Bob Smith",110, 88) 

student1.add_grade(99)
student2.add_grade(77)
student2.add_grade(73)
student1.add_grade(96)

student1.display_info()
student2.display_info()
    