start_num = int(input("Enter initial number between 1 and 100: "))
end_num = int(input("Enter final number between 1 and 100: "))

for num in range(start_num, end_num + 1):
    if not (1 <= num <= 100):
        print("Invalid input")
        break
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    
    else:
        print(num)