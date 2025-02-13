scores=[65,90,45,80,50,76,88,92,59,30]
result=[]

for score in scores:
    if score > 60:
       result.append((score,"pass"))
    else:
        result.append((score,"fail")) 
print(f"score:{score} {result}")