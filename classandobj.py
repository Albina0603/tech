class Student:
    def __init__(self,name,student_id,grades):
        self.name=name
        self.student_id=student_id
        self.grades=[]
        
    def add_grade(self,grades):
        self.grades.append(grades)
    
    def calculate_average(self):
        return sum (self.grades)/ len (self.grades)
    def get_best_grade(self): 
        return max(self.grades) if self.grades else None
    def get_worst_grade(self): 
        return min(self.grades) if self.grades else None
    def display_info(self):
        average = self.calculate_average()
        best_grade =self.get_best_grade()
        worst_grade =self.get_worst_grade()
        print(f"Student Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print(f"Average grades: {average}")
        print(f"Best grade:{best_grade}")
        print(f"Worst grade:{worst_grade}")

class StudentManager:
    def __init__(self):
        self.students=[]

    def add_student(self,student):
        self.students.append(student)        
    def get_top_students(self):
        return max(self.students,key=lambda student: student.calculate_average())   
    def get_lowest_student(self): 
        return min(self.students,key=lambda student: student.calculate_average())
    
    def display_all_students(self):
        if not self.students:
            print("Список стдуентов пуст")
        for student in self.students:
            student.display_info()
            print(f"Best student:{self.get_top_students()}")
            print(f"Worst student:{self.get_lowest_student()}")
student1=Student("Alice Johnson", 101, 97)  
student2=Student("Bob Smith",110, 88) 

student1.add_grade(97)
student2.add_grade(77)
student2.add_grade(73)
student1.add_grade(96)
student2.add_grade(98)
student1.add_grade(96)

student1.display_info()
student2.display_info()

manager =StudentManager()
manager.add_student(student1)
manager.add_student(student2)
manager.display_all_students()
    