grades = []


for c in range(5):
    while True:
        g = int(input("Enter Grade: "))
        if 40 <= g <= 100:
            grades.append(g)
            break    
        else:
            print("Grades must be between 40-100")


avg = sum(grades) / 5


i = 0
for g in grades:
    if g >= 75:
        i += 1


percentage = (i / 5) * 100


print("Average Grade: ", avg)
print("Grade Entered: ", grades)
print("Number of Students who passed: ", i)
print("Passing Percentage: ", percentage, "%")

        
     
        


