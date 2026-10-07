first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
third_number = float(input("Enter the third number: "))
if first_number > second_number and first_number > third_number:
    print(f"The largest number is: {first_number}")
elif second_number > first_number and second_number > third_number:
    print(f"The largest number is: {second_number}")
elif third_number > first_number and third_number > second_number:
    print(f"The largest number is: {third_number}")
elif first_number == second_number and first_number > third_number:
    print(f"The largest number is: {first_number} and {second_number}")
elif first_number == third_number and first_number > second_number:
    print(f"The largest number is: {first_number} and {third_number}")
elif second_number == third_number and second_number > first_number:
    print(f"The largest number is: {second_number} and {third_number}")
else:
    print("All three numbers are equal.")