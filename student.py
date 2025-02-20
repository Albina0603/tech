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
                top_scores = student["name"]
               
    return top_scores 
        
display_students(students)
print(get_average_score("Alice", students))
print(find_top_student(students))


