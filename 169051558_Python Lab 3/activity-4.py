# Step 1: Declare two Boolean variables
# ----
is_sunny = True
is_raining = False

# Step 2: Demonstrate logical operations (AND, OR, NOT)
# Logical AND
# ----
print("Is it sunny and raining?", is_sunny and is_raining)

# Logical OR
# ----
print("Is it sunny or raining?", is_sunny or is_raining)

# Logical NOT
# ----
print("Is it not sunny?", not is_sunny)

# Step 3: Use a Boolean variable in a conditional statement
# ----
# Conditional statement with logical operation
# ----
if is_sunny:
    print("It's a sunny day!")
else:
    print("It's not sunny today.")
