correct_pin = "1234"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    user_pin = input("Enter your PIN: ")
    attempts += 1
    
    if user_pin == correct_pin:
        print("PIN accepted. Access granted!")
        break
    else:
        attempts_left = max_attempts - attempts
        print("Incorrect PIN.")
        
        if attempts_left > 0:
            print(f"Attempts remaining: {attempts_left}\n")
        else:
            print("No attempts remaining. Account locked!")