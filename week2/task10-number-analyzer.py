largest = None
smallest = None
total_sum = 0
even_count = 0
odd_count = 0

print("Please enter 10 numbers.")

for i in range(1, 11):
    num = int(input(f"Enter number {i}: "))
    
    total_sum += num
    
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
        
    if largest is None or num > largest:
        largest = num
        
    if smallest is None or num < smallest:
        smallest = num

average = total_sum / 10

print(f"Largest number: {largest}")
print(f"Smallest number: {smallest}")
print(f"Total sum: {total_sum}")
print(f"Average: {average}")
print(f"Even numbers: {even_count}")
print(f"Odd numbers: {odd_count}")