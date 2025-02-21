students = [
{
    "name": "Alice",
    "subjects": ("Math", "Physics", "English"),
    "scores": {"Math": 85, "Physics": 78, "English": 92}},
{
    "name": "Bob",
    "subjects": ("Math", "Biology", "English"),
    "scores": {"Math": 72, "Biology": 88, "English": 80}},
{
    "name": "Charlie",
    "subjects": ("Math", "Physics", "Chemistry"),
    "scores": {"Math": 90, "Physics": 95, "Chemistry": 85}},

]


def display_students(data):
    for student in data:
        name = student["name"]
        subjects = ", ".join(student["subjects"])
        print(f" {name} is enrolled in: {subjects}")
    
def get_average_score(name, students):
    for student in students:
        if student["name"] ==name:
            scores=student["scores"].values()
            return sum (scores)/ len (scores)       
    return None       
   
def find_top_student(students):
    top_s= None
    high_score = 0
    for student in students:
            scores=student["scores"].values()
            average= sum (scores)/ len (scores) 
                   
            if average>high_score: 
                high_score = average
                top_s = student["name"]               
    return top_s 

def failed_students(students,passing_score):
    failed=[]
    for student in students:
        for score in student["scores"].values():
            if score < passing_score:
                failed.append(student["name"])
                break
    return failed

def unique_subjects(students):
    subjects=set()
    for student in students:
        subjects.update(student["scores"].keys())
    return subjects    
        
display_students(students)
print(get_average_score("Alice", students))
print(find_top_student(students))
print(failed_students(students,passing_score=75))
print(unique_subjects(students))


