import math
import datetime

current_datetime =datetime.datetime.now()
sqrt_value = math.sqrt(25)
pi_value = math.pi
cos_value = math.cos(math.radians(45))


print("Квадратный корень из25:",sqrt_value)
print("Значение числа П:",pi_value)
print("Косинус 45 градусов:",cos_value)


with open('result.txt' , 'w') as file :
    sqrt_value = math.sqrt(25)
    file.write(f"koren is chisla 25 {sqrt_value}\n")
    
    pi_value = math.pi
    file.write(f"znachenii chisla P:{pi_value}\n")
    
    cos_value = math.cos(math.radians(45))
    file.write(f"Kosinus 45 gradusov: {cos_value}\n")
    
with open('result.txt' , 'a') as file:
    file.write(f"Data i Vremya: {current_datetime}\n")

try:
    with open('result.txt', 'r') as file:
        content= file.read()
except FileNotFoundError:
    print("File not fonud")

