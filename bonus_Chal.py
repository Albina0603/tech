scores=list(map(int,input("Введите список оценок через пробел").split()))
even_numbers = 0
odd_numbers = 0
result=[]
for score in scores:
    if score >=90:
        grade="A"
        result.append((scores,"pass"))
    elif score >=80:
        grade="B"
        result.append((scores,"pass"))
    elif score >=70:
        grade="C"
        result.append((scores,"pass"))
    elif score >=60:
        grade="D"
        result.append((scores,"pass"))
    else:
        grade="F"
        result.append((scores,"fail")) 

    print(f"балл:{score} оценка:{grade} Результат {result}")
    
    even_numbers+=score%2==0
    odd_numbers+=score%2!=0
    print(f"Четных оценок:{even_numbers}")
    print(f"Нечетных оценок:{odd_numbers}")
