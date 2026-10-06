employee_name = input("Enter your name: ")
basic_salary = float(input("Enter your salary: "))
transport_allowance = float(input("Enter your transport: "))
food_allowance = float(input("Enter your food: "))
line = "========================================"

Gross_Salary = basic_salary + transport_allowance + food_allowance

print(f"{line} \n \t EMPLOYEE PAYSLIP \n{line} \n")
print(f"Employee: {employee_name} \n")
print(f"Basic Salary:  {basic_salary}")
print(f"Transport Allowance: {transport_allowance}")
print(f"Food Allowance: {food_allowance}")
print("----------------------------------------")
print(f"Gross Salary: {Gross_Salary}")
print(line)