# Student = [
# {
#     "student_id": 1
#     "name": "Gabi",
#     "age": 35,
#     "grade": {"Math": 85, "Physics": 78, "English": 92}},
# {
#     "student_id": 2
#     "name": "Susan",
#     "age": 45,
#     "grade": {"Math": 85, "Physics": 78, "English": 92}},
# {
#     "student_id": 3
#     "name": "Bree",
#     "age": 44,
#     "grade": {"Math": 100, "Physics": 100, "English": 100}},  ,
# ]
class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id=student_id
        self.name=name
        self.age=age
        self.grade=grade
    def __str__(self):
        return f"{self.student_id},{self.name}, {self.age}, {self.grade}"
    def to_dict(self):
         return {
             "student_id":self.student_id,
             "name":self.name, 
             "age":self.age,
             "grade":self.grade}
    