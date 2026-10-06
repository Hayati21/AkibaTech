Student_name = input("Enter the student's name: ")
Python_score = float(input("Enter the student's Python score: "))
English_score = float(input("Enter the student's English score: "))
Mathematics_score = float(input("Enter the student's Mathematics score: "))
line = "=================================="
dots = "----------------------------------------"
Average_score = (Python_score + English_score + Mathematics_score)/3
print(f"{line} \n \t STUDENT RESULT \n {line}")
print(f"Student: {Student_name}")
print(f"Python: {Python_score}")
print(f"English: {English_score}")
print(f"Mathematics: {Mathematics_score}")
print(f"{dots}")
print(f"Average: {Average_score}")