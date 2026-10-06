Name = input("Enter your name: ")
Weight = float(input("Enter your weight in kilograms: "))
Height = float(input("Enter your height in meters: "))
line = "=================================="
BMI = Weight / (Height ** 2)

print(f"{line} \n \t BMI REPORT \n{line} \n ")
print(f"Name: {Name}")
print(f"Weight: {Weight} kg")
print(f"Height: {Height} m \n")
print(f"BMI: {BMI:.2f} \n{line}")
