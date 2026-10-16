import random
secret_number = random.randint(1, 10) 
attempts = 0

while attempts < 5:
    guess = int(input("Guess the number: "))
    attempts += 1
    
    if guess == secret_number:
        print("Congratulations!")
        print(f"You guessed the number in {attempts} attempts.")
        break

if guess != secret_number:
    print("Game Over!")
