random_number = int(input("Enter a number: "))
if random_number > 0:
    print(f"{random_number} is positive number")
elif random_number < 0:
    print(f"{random_number} is negative number")
else:
    print(f"{random_number} is zero")

    
if random_number % 2 == 0:
    print(f"{random_number} is an even number.")
else:
    print(f"{random_number} is an odd number.")