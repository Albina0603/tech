import random

x = random.randint(1, 100)
while (guess := int(input("Угадай число:"))) != x:
 print(" (Горячо!" if abs (guess - x) <10 else "Холодно!")
print("Вы угадали!")