score=int(input("Введите ваш балл:"))

if score < 50:
    print ("Ваша итоговая оценка:0")
elif 50 < score < 59:
    print ("Ваша итоговая оценка:F")
elif 60 < score < 69:
    print ("Ваша итоговая оценка:D")
elif 70 < score < 79:
    print ("Ваша итоговая оценка:C")
elif 80 < score < 89:
    print ("Ваша итоговая оценка:B")
elif 90 < score < 100:
    print("Ваша итоговая оценка:A")
else:
    print("Не аттестован")
    