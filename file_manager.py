import json
from student import Student
FILE_NAME = "students.json"
def save_students(students):    
    with open(FILE_NAME , 'w') as file:
        
     for student in students:   
def add_students():
    try:
        with open(FILE_NAME, 'r') as file:
        content = file.read()
    except FileNotFoundError:
        return()
