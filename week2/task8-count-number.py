N = int(input("Enter a positive number N: "))

even_count = 0
odd_count = 0
total_sum = 0

for i in range(1, N + 1):
    total_sum += i
    
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f"Even numbers: {even_count}")
print(f"Odd numbers: {odd_count}")
print(f"Sum of all numbers: {total_sum}")