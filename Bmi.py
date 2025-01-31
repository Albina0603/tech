height =float (input("Введите ваш рост:"))
weight =float (input("Введите ваш вес:"))

height_m = height/100

bmi=weight/(height_m**2)

print(f"Ваш bmi:{weight/(height_m **2)}")

if bmi < 18.5:
    print ("underweight")
elif 18.5 < bmi < 24.9:
    print ("normalweight")
elif 25 < bmi < 29.9:
    print ("overweight")
elif 30 < bmi < 34.9:
    print ("obesity class 1")
elif 35 < bmi < 39.9:
    print ("obesity class 2")
elif bmi >= 40:
    print("obesity class 3")
else:
    print("Too muchh")
    