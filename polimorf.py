from abc import ABC, abstractmethod

class Employees(ABC):   
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
    @abstractmethod
    def work(self):
        pass
        
    def display_info(self):
        print(f" Имя: {self.name} ,Возраст:{self.age} Зарплата: {self.salary}")
        
class Developer(Employees):
    def __init__(self, name, age, salary,programming_language):
        super().__init__(name, age, salary)
        self.programming_language = programming_language
        
    def work(self):
        print(f"{self.name} пишет код {self.programming_language}")
        
class Manager(Employees):
    def __init__(self, name, age, salary, team_size):
        super().__init__(name, age, salary)
        self.team_size = team_size
        
    def work(self):
        print(f"{self.name} управляет командой из {self.team_size} человек")
        
worker1 = Developer("Алекс" ,30 , 70000 , "Python")
worker2 = Manager("Екатерина" , 40 , 90000 , 10)

#Employees= [Developer("Алекс" ,30 , 70000 , "Python"),
  #         Manager("Екатерина" , 40 , 90000 , 10)]

worker1.display_info()
worker1.work()

worker2.display_info()
worker2.work()



