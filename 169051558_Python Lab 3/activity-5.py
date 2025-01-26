total_sum = 0
count = 0

# Start the loop
while total_sum < 100:
    user_input = input("Enter a number or press space (' ') to exit: ")
    
    # Check if the user entered a space
    if user_input == " ":
        break

    # Try to convert the input to a number
    try:
        number = float(user_input)  # Using float to handle decimal inputs
        total_sum += number
        count += 1
    except ValueError:
        print("Invalid input. Please enter a valid number or a space to exit.")

print(f"Total sum: {total_sum}")
print(f"Count of numbers entered: {count}")
